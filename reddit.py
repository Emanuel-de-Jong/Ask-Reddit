import praw
from praw.models import MoreComments
import reddit_login

reddit = praw.Reddit(
    user_agent='windows:analyzer:v0.1 (by u/KillBottt)',
    client_id=reddit_login.client_id,
    client_secret=reddit_login.client_secret,
    username=reddit_login.username,
    password=reddit_login.password)

print(reddit.user.me())
print(reddit.read_only)

for submission in reddit.subreddit('askreddit').top('day', limit=1):
    title = submission.title
    comments = list(submission.comments)


file = open("comments.txt", "w+")
for i in range(10):
    comment = comments[i]

    if isinstance(comment, MoreComments):
        continue

    file.write('--------------------\n')
    file.write(comment.body + '\n')

file.close()
