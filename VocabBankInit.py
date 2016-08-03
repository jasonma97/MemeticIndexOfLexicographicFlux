import praw
from DANKDATABASE import DANKB
from operator import itemgetter


COMMENT_LIMIT = 420
THRESHOLD = 42
NUM_POSTS = 25
NUM_NORMIE_POSTS = 10
SUBREDDIT = 'circlejerk+ledootgeneration+montageparodies+4chan+blackpeopletwitter'
NORMIE = 'all'

def flatten(submission):
    submission.replace_more_comments(limit = COMMENT_LIMIT, threshold =THRESHOLD)
    flat_coms = praw.helpers.flatten_tree(submission.comments)
    #flat_coms = submission.get_all_comments
    return flat_coms
    

def printComments(submission):
    flat_coms = flatten(submission)
    for comment in flat_coms:
        print comment
       
def countOccurences(elem, L):
	return L.count(elem)
	
def getUnique(L):
	unique = []
	for elem in L:
		if elem not in unique:
			unique.append(elem)
	return unique
	
def count(L):
	'''
		returns a list of unique elements
		and the number of occurrences in list
	'''
	unique = getUnique(L)
	bigDict = [[elem, countOccurences(elem, L)] for elem in unique]
	return bigDict
	
def makeBank(submissions, normie):
    f = open("C:\Users\WenJian\Documents\Jason's HMC Work\Hackathon\DANKBANKFINAL.txt", 'w')
    penis = open("C:\Users\WenJian\Documents\Jason's HMC Work\Hackathon\FUCKINGNORMIES.txt", 'w')
    bigD = ""
    for submission in submissions:
        flat_coms = flatten(submission)
        for comment in flat_coms:
            bigD += str(comment) + " "
    occurrences = count(str.split(bigD))
    
    smallD = ""
    for REEEEE in normie:
        normie_flat_coms = flatten(REEEEE)
        for spork in normie_flat_coms:
            smallD += str(spork)
    normieWords = count(str.split(smallD))
    sorted_Normie = sorted(normieWords, key = itemgetter(1))
    reverseNormie = sorted_Normie[::-1]
    sortedNormie = reverseNormie[0:69]
    for x in range(len(sortedNormie)):
            penis.write(str(sortedNormie[len(sortedNormie) - x - 1][0]) + " : " + str(sortedNormie[len(sortedNormie) - x - 1][1]) + "\n")
    normieKey = [REE[0] for REE in normieWords]
    
    occurrences2 = occurrences[:]
    for word in occurrences2:
        if word[0] in normieKey:
            occurrences.remove(word)
     
    sortedWords = sorted(occurrences, key = itemgetter(1))
    for x in range(len(sortedWords)):
        if x > 690:
            print "\n\n\nDONE BITCH\n\n\n"
            break
        else:
            f.write(str(sortedWords[len(sortedWords) - x - 1][0]) + " : " + str(sortedWords[len(sortedWords) - x - 1][1]) + "\n")
    f.close()
    penis.close()
            
  
     
    
def initDankBank():
    r = praw.Reddit(user_agent = 'my_dank_application')
    submissions = r.get_subreddit(SUBREDDIT).get_top_from_month(limit = NUM_POSTS)
    normie = r.get_subreddit(NORMIE).get_top_from_month(limit = NUM_POSTS)
    makeBank(submissions, normie)
        
initDankBank()

   


        
#print "DANK LEVEL: " + str(dankCounter(flat_coms))
        



