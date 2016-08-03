import praw
from time import sleep

COMMENT_LIMIT = 420
THRESHOLD = 69
DATABASE = "C:\Users\WenJian\Documents\Jason's HMC Work\Hackathon\DANKBANKMONTH.txt"
NUM_POSTS = 10
SUBREDDIT = 'all'

def readDankBank():
    f = open(DATABASE, 'r')
    DB = []
    for line in f:
        DB += [str.split(line)]
    for item in DB:
        item.remove(':')
    bigDict = {}
    for elem in DB:
        if elem[0].lower() not in bigDict:
            bigDict[elem[0].lower()] = int(elem[1])
        else:
            bigDict[elem[0].lower()] = int(elem[1]) + bigDict[elem[0].lower()]
    f.close()
    return bigDict

def flatten(submission):
    submission.replace_more_comments(limit = COMMENT_LIMIT, threshold =THRESHOLD)
    flat_coms = praw.helpers.flatten_tree(submission.comments)
    #flat_coms = submission.get_all_comments
    return flat_coms    
            
def dankCounter():
    r = praw.Reddit(user_agent = 'my_dank_application')
    submissions = r.get_subreddit(SUBREDDIT).get_hot(limit = NUM_POSTS)
    DANKB = readDankBank()
    dank = 0
    flat_coms = []
    for submission in submissions:
        flat_coms += flatten(submission)
        
    words = []
    for comment in flat_coms:
        words += str.split(str(comment))
    for word in words:
        if word in DANKB:
            dank += DANKB[word]
    return dank, len(words)

print "Counting Dankness of " + str(SUBREDDIT)
dankLevel,words = dankCounter()
print "DANK LEVEL: " + str(dankLevel)
dankLevel *= 1.0
print "DANK METER READING: " + str((dankLevel/words)) + "%"

    


