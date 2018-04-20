
import spacy
import gensim.models
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess


class cleanup(object):

    def __init__(self, reddit_dict, desiredsub):
        self.reddit_dict = reddit_dict
        self.desiredsub  = desiredsub
        self.getcomments()

    def getcomments(self):
        comments = list()
        for k, i in self.reddit_dict[self.desiredsub].items():
            comments.append(k.body)
        self.comments = comments

    def comments(self):
        return self.comments

    def getwords(self):
        words = []
        for sentence in self.comments:
            for word in sentence.split():
                # define punctuation
                punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

                # remove punctuation
                no_punct = ""
                for char in word:
                    if char not in punctuations:
                        no_punct = no_punct + char

                if len(no_punct) < 2:
                    pass
                else:
                    words.append(no_punct)
        return words

    def lemmatize(self, texts):
        lemmas = []
        brackets = '''[]'''
        grammar_type=['NOUN', 'ADJ', 'VERB', 'ADV']
        nlp = spacy.load('en', disable=['parser', 'ner'])
        for ind, sentence in enumerate(texts):
            if ind % 1000 == 0:
                print('Lemmatizing...', ind, 'out of', len(texts))
            doc = nlp(' '.join(sentence))
            lemmas.append([token.lemma_ for token in doc if token.pos_ in grammar_type])
        print('Done')
        return lemmas

    def remove_stopwords(self, words):
        stop_words = stopwords.words('english')
        stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'com'
                            'www', 'http', 'https', 'bot'])
        removed = []
        for word in simple_preprocess(str(words)):
            if word not in stop_words:
                removed.append([word])
        return removed

    def lemms_cleanup(self, lemms):
        clean_lemms = []
        brackets = '''[]'''
        for i in lemms:
            if i == []:
                pass
            else:
                no_punct = ""
                for char in i:
                    if char not in brackets:
                        no_punct = no_punct + char
                clean_lemms.append(no_punct)
        return clean_lemms

    def _processing(self, removed):
        processed = gensim.models.Phrases(removed, min_count=5, threshold=100)
        processed_mod = gensim.models.phrases.Phraser(processed)
        return [processed_mod[doc] for doc in removed]

    def returnlemms(self):
        words = self.getwords()
        removed = self.remove_stopwords(words)
        texts = self._processing(removed)
        lemms = self.lemmatize(texts)
        clean_lemms = self.lemms_cleanup(lemms)
        return clean_lemms
