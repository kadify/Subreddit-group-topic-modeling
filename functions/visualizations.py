from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pyLDAvis.sklearn
from cleanup import cleanup
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


class visualizations(object):

    def __init__(self, comments, num_topics):
        self.comments = comments
        self.num_topics = num_topics

        self.stop_words = stopwords.words('english')
        self.stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'com'
                            'www', 'http', 'https', 'bot'])

    def get_umass_coherence_scores(self, M=5):
        """
        computes UMass coherence scores for all latent topics
        input:
        - M (int): # of top words to consider when computing UMass score
        returns:
        - list of coherence scores for each latent topic
        """

        scores = []
        for top_words_in_topic in self.top_words_in_topics:
            scores.append(self._get_umass_coherence_metric(top_words_in_topic,
                                                           M))

        return scores

    def _get_umass_coherence_metric(self, top_words_in_topic, M=5):
        """
        helper function for get_umass_coherence_scores() that simply computes
        the UMass coherence score for a single topic
        input:
        - top_words_in_topic (list of strings): top words in a particular topic
        - M (int): # of top words to consider when computing UMass score
        returns:
        - UMass coherence score (float) for a particular topic
        """

        terms_to_sum = []
        tf_idf = self.tf_idf
        tf_idf[tf_idf != 0] = 1

        for m in range(1, M):
            word_m = top_words_in_topic[m]
            word_m_index = self.vocab[word_m] # index of col corresponding to
                                              # this word in TF-IDF
            tfidf_column_for_word_m = tf_idf[:,word_m_index].todense()\
                                                            .astype(int)
            for l in range(0, m-1):
                word_l = top_words_in_topic[l]
                word_l_index = self.vocab[word_l]
                num_docs_with_word_l = tf_idf[:,word_l_index].sum()
                tfidf_column_for_word_l = tf_idf[:,word_l_index].todense()\
                                                                .astype(int)
                num_docs_with_both_words = (tfidf_column_for_word_m
                                            & tfidf_column_for_word_l).sum()
                result = (num_docs_with_both_words + 1)/num_docs_with_word_l
                terms_to_sum.append(result)

        coherence_score = np.sum(np.log(np.array(terms_to_sum)))

        return coherence_score

    def LDA(self, topics, htmlname):

        topics = topics

        vectorizer = CountVectorizer(min_df=5, max_df=0.9,
                                     stop_words=self.stop_words, lowercase=True,
                                     token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')
        data_vectorized = vectorizer.fit_transform(comments)

        # Build a Latent Dirichlet Allocation Model
        lda_model = LatentDirichletAllocation(n_topics=topics, max_iter=1000, learning_method='online')
        lda_Z = lda_model.fit_transform(data_vectorized)


        panel = pyLDAvis.sklearn.prepare(lda_model, data_vectorized, vectorizer, mds='tsne')
        pyLDAvis.save_html(panel, htmlname)

    def topic_error(self, solver='mu', max_iter=100):


        vector = TfidfVectorizer(strip_accents='ascii',tokenizer=self._tweet_tokenizer,
                              stop_words=self.stop_words, max_df=0.8, max_features=5000,
                              ngram_range=(1,1))
        self.tf_idf = vector.fit_transform(self.comments)

        nmf = NMF(n_components=self.num_topics, max_iter=max_iter, solver=solver)

        reconstruction_error = []
        for topicnum in self.num_topics:
            nmf = NMF(n_components=topicnum, max_iter=max_iter, solver=solver)
            nmf.fit(self.tf_idf, max_iter=max_iter)
            reconstruction_error.append(nmf.reconstruction_err)

        plt.figure()
        plt.title('NMF Reconstruction Error vs. Number of Topics\n' + '(With {} Iterations)'.format(max_iter))
        plt.xlabel('Number of Topics')
        plt.ylabel('NMF Reconstruction Error')
        plt.scatter(self.num_topics, reconstruction_errs)

    def word_coherence(self, max_iter=100, solver='mu', M=5):

        vector = TfidfVectorizer(strip_accents='ascii',
                              stop_words=self.stop_words, max_df=0.8, max_features=5000,
                              ngram_range=(1,1))

        self.tf_idf = vector.fit_transform(self.comments)


        scores_list = []
        for topicnum in self.num_topics:
            nmf = NMF(n_components=topicnum, max_iter=max_iter, solver=solver)
            nmf.fit(self.tf_idf)
            coherence_scores = nmf.get_umass_coherence_scores(M)
            scores_list.append(coherence_scores)


        plt.subplots(5,2,figsize=[14,14])
        i = 1
        for num_topics, scores in zip(self.num_topics_list,scores_list):
            plt.subplot(2,5,i)
            plt.ylabel('UMass Coherence Score', size=10)
            plt.ylim([-30,-5])
            plt.title('Number of Topics = {}'.format(num_topics), size=12)
            sns.boxplot(y=scores)
            i+=1
        plt.tight_layout()

    def create_wordcloud(lemms):
        '''
        INPUT : lemmatized string
        OUTPUT: returns wordcloud
              : saves a figure of a wordcloud in working directory
        '''
        wordcloud = WordCloud().generate(lemms)
        dpi=300
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        # lower max_font_size
        wordcloud = WordCloud(max_font_size=40).generate(lemms)
        plt.figure(figsize=(12, 8),dpi=dpi, facecolor='w', edgecolor='k')
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        # plt.savefig('wordmap_temp.png', dpi=dpi)
