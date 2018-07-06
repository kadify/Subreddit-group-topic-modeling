# reddit = praw.Reddit(client_id=####CLIENTID####,
#                      client_secret=####CLIENTSECRET####,
#                      user_agent='string')
import praw
import numpy as np
from textblob import TextBlob





class comments_to_dict(object):

    def __init__(self, redditID, subreddits, limit=2, verbose=True):
        self.redditID = redditID
        self.subreddits = subreddits
        self.limit = limit
        self.verbose = verbose

    def iterator(self):
        '''
            Iterates over list of subreddits and returns dictionary of subreddit
            comments for each specified subreddit.
        '''
        self.subreddit_dict = {}
        for i in self.subreddits:
            self.subreddit_dict[i] = self.compiler(i)
        return self.subreddit_dict

    def _getreplies(self, comment):
        '''
        Retrieves replies to specified comment on reddit
        '''

        self.commentsList.append(comment)
        if not hasattr(comment, "replies"):
            replies = comment.comments()
            if self.verbose: print("fetching (" + str(len(self.commentsList)) + " comments fetched total)")
        else:
            replies = comment.replies
        for child in replies:
            self._getreplies(child)

    def getAll(self, commentId):
        '''
        Retrieves and creates list of all replies from subreddit up to a specified limit
        '''
        submission = self.redditID.submission(commentId)
        submission.comments.replace_more(limit=self.limit)
        comments = submission.comments[:]
        self.commentsList = []
        for comment in comments:
            self._getreplies(comment)
        return self.commentsList


    def tabler(self, _id):
        '''
        Returns dictionary of replies for specified comment
        '''
        comments = {}
        for ind, i in enumerate(self.res):
            if i.parent().id == _id:
                comments[ind] = i
        return comments

    def PRAW_tree(self, commentID):
        '''
        Returns dictionary list of replies for specified comment
        '''
        reply_list = {}
        for i in self.res:
            comments = self.tabler(i.id)
            reply_list[i] = comments
        return reply_list

    def compiler(self, sub):
        '''
        Returns complete dictionary of comments with replies key being main comment and
        value being replies to that comment
        '''
        subreddit = self.redditID.subreddit(sub)
        dict_total = {}
        for commentID in subreddit.hot(limit=self.limit):
            self.res = self.getAll(commentID)
            reply_list = self.PRAW_tree(commentID)
            dict_total.update(reply_list)
        return dict_total

    
