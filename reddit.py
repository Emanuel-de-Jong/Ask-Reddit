import praw
import reddit_login


reddit = None
post = None


def init(subreddit='askreddit', sort='top', time='day'):
    global reddit
    reddit = praw.Reddit(
        user_agent='windows:analyzer:v0.1 (by u/KillBottt)',
        client_id=reddit_login.client_id,
        client_secret=reddit_login.client_secret,
        username=reddit_login.username,
        password=reddit_login.password)

    if sort == 'new':
        submissions = reddit.subreddit(subreddit).new(limit=1)
    elif sort == 'hot':
        submissions = reddit.subreddit(subreddit).hot(limit=1)
    elif sort == 'rising':
        submissions = reddit.subreddit(subreddit).rising(limit=1)
    elif sort == 'top':
        submissions = reddit.subreddit(subreddit).top(time, limit=1)
    elif sort == 'controversial':
        submissions = reddit.subreddit(subreddit).controversial(time, limit=1)

    global post
    for submission in submissions:
        post = submission


def get_top_level_comments(comment_count=10):
    comments = post.comments
    comments.replace_more(limit=0)

    if comment_count > len(comments):
        comment_count = len(comments)

    comment_list = []
    for i in range(comment_count):
        comment = comments[i]

        comment_list.append(
            {
                "author": comment.author.name,
                "body": comment.body,
                "created_utc": comment.created_utc,
                "is_submitter": comment.is_submitter,
                "score": comment.score
            }
        )

    return comment_list
