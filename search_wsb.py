from psaw import PushshiftAPI
import datetime 

api = PushshiftAPI()

start_time = int(datetime.datetime(2022, 6, 18).timestamp())

submissions = list(api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=1000))

for submission in submissions:

    # filter title for words that start with a '$'
    # split title into seperate words
    words = submission.title.split()
    # print(words)

    # filter words for $ words:
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    # print list of cashtags if list is not 0
    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)