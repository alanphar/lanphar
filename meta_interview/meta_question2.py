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

So then I mentioned to the interviewer my idea to leverage a heap. However, I struggled to implement.

Post interview I decided to go with my original thought using a dictionary:
    Create O(1)
    Upvote O(1)
    Top25 O(N log N) where N is number of threads

I added a update attribute so that if repeated Top25 is called without new threads or upvotes,
Top25 would return in O(1) while using O(25) additional space

If Top25 needed to be faster than N log N I would then implement a AVL or red black self balancing Binary Search Tree
    slowing down creating and inserting to O(log N) balanced and O(N) worst
"""
from operator import itemgetter


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
        else:
            self.top_25 = sorted(self.threads.items(), key=itemgetter(1), reverse=True)[:25]
            self.updated = False
            return self.top_25

# The Test
my_class = MetaReddit()

for x in range(100):
    my_class.create_thread(threadID=x)


for x in range(0, 100, 4):
    if x % 8 == 0:
        limit = 1000 + x
    else:
        limit = x + 100

    for _ in range(limit):
        my_class.upvote_thread(threadID=x)

print(my_class.top25())
