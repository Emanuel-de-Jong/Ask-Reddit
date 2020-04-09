import copy
import praw
import reddit_login


reddit = None
post = None


def init(subreddit='askreddit', sort='top', time='day', row=1):
    global reddit
    reddit = praw.Reddit(
        user_agent='windows:analyzer:v0.1 (by u/KillBottt)',
        client_id=reddit_login.client_id,
        client_secret=reddit_login.client_secret,
        username=reddit_login.username,
        password=reddit_login.password)

    if sort == 'new':
        submissions = reddit.subreddit(subreddit).new(limit=row)
    elif sort == 'hot':
        submissions = reddit.subreddit(subreddit).hot(limit=row)
    elif sort == 'rising':
        submissions = reddit.subreddit(subreddit).rising(limit=row)
    elif sort == 'top':
        submissions = reddit.subreddit(subreddit).top(time, limit=row)
    elif sort == 'controversial':
        submissions = reddit.subreddit(subreddit).controversial(time, limit=row)

    global post
    for submission in submissions:
        post = submission


def get_top_level_comments(comment_count=99, seperate_body_sentences=True, sort='best'):
    temp_post = copy.deepcopy(post)
    temp_post.comment_sort = sort
    temp_post.comments.replace_more(limit=0)

    comments = temp_post.comments

    if comment_count > len(comments):
        comment_count = len(comments)

    comment_list = []
    for i in range(comment_count):
        comment = comments[i]

        comment_list.append(
            {
                "author": comment.author.name,
                "created_utc": comment.created_utc,
                "is_submitter": comment.is_submitter,
                "score": comment.score
            }
        )

        body = comment.body

        if seperate_body_sentences:
            d = '. '
            body = [s + d for s in body.split(d) if s]

        comment_list[i]['body'] = body

    return comment_list
