#The crazy reddit message alert by u/sam0s
import praw
newlist = []

#USE YUR OWN USERNAME
r = praw.Reddit(user_agent='sam0s')

sub=r.get_submission(submission_id='4g3nhe')#REDDIT POST SHORT URL GOES HERE
sub.replace_more_comments(limit=10000, threshold=10)
flat_comments = praw.helpers.flatten_tree(sub.comments)
for c in flat_comments:
    if c.body.startswith('/u'):
        newlist.append((str(c).split(" "))[0])

for f in newlist:
    if '\n' in f:
        newlist[newlist.index(f)]=(f.split('\n'))[0]

newlist = list(set(newlist))

print newlist
print len(newlist)


#PLUG YO INFO IN HERE
r.login('usr', 'pass')


#SEND YOUR CUSTOM MESSAGE TO EVERYONE WHO ENTERS WITH A "/u/username"
for x in newlist:
    r.send_message(x[3:], 'HEY FELLAS!')
