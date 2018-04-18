## Underlying topic exploration from 33 subreddits ... 
---

### Goals
> The goals of this capstone were to explore the underlying topics expressed in thread posts across 33 different car subreddits. Topic Modeling was completed across all subreddits and used to demonstrate any patterns in the discussions occuring across each subreddit. The end goal was to determine if there was a quantifiable difference in the conversations happening between the differen subreddits since they are related (each subreddit was a car manufacturer subreddit).

### Data
Using a Python Reddit API Wrapper ([PRAW](https://praw.readthedocs.io/en/latest/)), subreddit thread comments were scraped, and topic models were created to determine the general underlying topics being discussed by the community posting in each subreddit.

### Steps taken so far
* Scrape data from 33 different car manufacturer subreddits
* Use Stemming, Lemmatization, and remove Stopwords
* Use Topic Modeling to get general consensus of topics being discussed using TFIDF NMF (Non-Negative Matrix Decomposition), TFIDF Clustering, and LDA (Latent Dirichlet Allocation)
  > To Do:
  > * Attempt NMF reconstruction error for number of topics (see which is best)
  > * Finalize topic modeling functions, put into class
  > * Apply function to all subreddit corpora
  > * Determine metric to compare topics between different subreddits
  


#### Next steps:
1. Find generalized topics for each subreddit (iterating multiple times to make sure the topics are in fact representative of the documents). 
2. Compare topics between the subreddits. Are they the same topics? Is one topic obviously discussing different things?
3. Clean up code and make interesting plots/graphics.
