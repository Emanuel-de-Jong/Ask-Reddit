import praw
import reddit_login

reddit = praw.Reddit(
    user_agent='windows:analyzer:v0.1 (by u/KillBottt)',
    client_id=reddit_login.client_id,
    client_secret=reddit_login.client_secret,
    username=reddit_login.username,
    password=reddit_login.password)

print(reddit.user.me())
print(reddit.read_only)
#commit from IDE test