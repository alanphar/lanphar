"""This question was asked during a technical interview for Meta SWE Product.

Stated a hypothetical to re-create a redit in memory.
Asked to create 3 methods for a class that already existed
1. createThread(threadID)
2. upVoteThread(threadID)
3. top25()
where top 25 would return the top 25 threads in terms of up votes

My first reaction was to store the information in a dictionary. (hash)
    so that creating and upvoting were O(1) operations. However I thought this may not be efficient for top25
    as sorting every time its called would be O(n log n)
So then I mentioned to the interviewer my idea to leverage a heap. However, I struggled to answer what to do once
all items had been popped from heap after one top25 call.

"""
from operator import gettatter

class MetaReddit:
    threads = dict()
    updated = False
    top_25 = []

    def create_thread(self, threadID):
        if threadID not in self.threads:
            self.threads[threadID] = 0
            self.updated = True

    def upvote_thread(self, threadID):
        self.threads[threadID] += 1
        self.updated = True

    def top25(self):
        if not self.updated:
            return self.top_25
