## Underlying topic exploration from 33 subreddits
---
### Question

*Is there a noticable difference between the general discussions occuring across different car brand subreddits?*
  
  
### Goals
> The goals of this capstone were to explore the underlying topics expressed in thread posts across 33 different car subreddits. Topic Modeling was completed across all subreddits and used to visualize any patterns in the discussions occuring across each subreddit. The end goal was to determine if there was an apparent difference in the conversations happening between the different subreddits.
___


                                                                                                              *[Top](#underlying-topic-exploration-from-33-subreddits)*
___

### Data
Using a Python Reddit API Wrapper ([PRAW](https://praw.readthedocs.io/en/latest/)), subreddit thread comments were scraped, resulting in approximately ~XXXXXX comments. Topic models were created to determine the general underlying topics being discussed by the community posting in each subreddit.

The following subreddits were compared:

* [r/BMW](https://www.reddit.com/r/BMW/)
* [r/Audi](https://www.reddit.com/r/Audi/)
* [r/Kia](https://www.reddit.com/r/Kia/)
* [r/Mercedes](https://www.reddit.com/r/Mercedes_Benz/)
* [r/Porsche](https://www.reddit.com/r/Porsche/)
* [r/Hyundai](https://www.reddit.com/r/Hyundai/)
* [r/Ford](https://www.reddit.com/r/Ford/)
* [r/Kia](https://www.reddit.com/r/Kia/)
* [r/Chevy](https://www.reddit.com/r/Chevy/)
* [r/Honda(& Acura)](https://www.reddit.com/r/Honda/)
* [r/Toyota](https://www.reddit.com/r/Toyota/)
* [r/TeslaMotors](https://www.reddit.com/r/TeslaMotors/)
* [r/Lexus](https://www.reddit.com/r/Lexus/)
* [r/Volvo](https://www.reddit.com/r/Volvo/)
* [r/Jeep](https://www.reddit.com/r/Jeep/)
* [r/Dodge](https://www.reddit.com/r/Dodge/)
* [r/Chrysler](https://www.reddit.com/r/Chrysler/)
* [r/Nissan](https://www.reddit.com/r/Nissan/)
* [r/Infiniti](https://www.reddit.com/r/Infiniti/)
* [r/Fiat](https://www.reddit.com/r/Fiat/)
* [r/Lamborghini](https://www.reddit.com/r/Lamborghini/)
* [r/Ferrari](https://www.reddit.com/r/Ferrari/)
* [r/AstonMartin](https://www.reddit.com/r/AstonMartin/)
* [r/Maserati](https://www.reddit.com/r/Maserati/)
* [r/Lotus](https://www.reddit.com/r/Lotus/)
* [r/Mitsubishi](https://www.reddit.com/r/Mitsubishi/)
* [r/Mclaren](https://www.reddit.com/r/Mclaren/)
* [r/GMC](https://www.reddit.com/r/GMC/)
* [r/Cadillac](https://www.reddit.com/r/Cadillac/)
* [r/Buick](https://www.reddit.com/r/Buick/)
* [r/Mazda](https://www.reddit.com/r/Mazda/)
* [r/RangeRover](https://www.reddit.com/r/RangeRover/)
* [r/Jaguar](https://www.reddit.com/r/Jaguar/)

                                                                                                              *[Top](#underlying-topic-exploration-from-33-subreddits)*
___



### Steps taken so far
* Scrape data from 33 different car manufacturer subreddits
* Use Stemming, Lemmatization, and remove Stopwords
* Use Topic Modeling to get general consensus of topics being discussed using TFIDF NMF (Non-Negative Matrix Factorization), TFIDF Clustering, and LDA (Latent Dirichlet Allocation)
  #### To Do:
  > * <strike>Attempt NMF reconstruction error for number of topics (see which is best)</strike>
  >  * <strike>Umass Topic coherence measurement for NMF as well</strike>
  > * Finalize topic modeling functions, put into class
  > * Apply function to all subreddit corpora
  > * Determine metric to compare topics between different subreddits
  > * *Perhaps use to make predictive model to determine what topics someone is posting about from unseen comments?* **Probably not**
  


#### Next steps:
1. Find generalized topics for each subreddit (iterating multiple times to make sure the topics are in fact representative of the documents). 
2. Compare topics between the subreddits. Are they the same topics? Is one topic obviously discussing different things?
3. Clean up code and make interesting plots/graphics.



