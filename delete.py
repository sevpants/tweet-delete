import yaml
import twitter
import csv
from datetime import datetime


# Load in twitter secrets from yaml file
with open('tweeter.yaml', 'r') as stream:
    contents = stream.read()
    config = yaml.load(contents, Loader=yaml.BaseLoader)

# Authenticate tweeter using yaml file
print('AUTHENTICATE TWITTER')

api = twitter.Api(
                consumer_key=config['twitter']['consumer_key'],
                consumer_secret=config['twitter']['consumer_secret'],
                access_token_key=config['twitter']['access_token_key'],
                access_token_secret=config['twitter']['access_token_secret'],
                sleep_on_rate_limit=True
                )

print(api.VerifyCredentials())


# Search the last 200 tweets
print('RETRIEVING ALL STATUSES EVER POSTED...UP TO 200 STATUSES')
timeline = api.GetUserTimeline(count=200)


# Export timeline to csv and use UTF-8 encoding to handle emojis in tweets
print('EXPORTING TIMELINE TO CSV')

with open('tweets.csv', 'w', newline='', encoding='UTF-8') as csvfile: 
    status_writer = csv.writer(csvfile)
    status_writer.writerow(
                        [
                            'id',
                            'created_at',
                            'favorite_count',
                            'retweet_count',
                            'text'
                        ]
                    )
    for status in timeline:
        status_writer.writerow(
                        [
                            status.id,
                            datetime.strptime(status.created_at, '%a %b %d %H:%M:%S %z %Y'),
                            status.favorite_count,
                            status.retweet_count,
                            status.text
                        ]
                    )

print('CSV FILE GENERATED')
    

# for analysis of the timeline, please check out the python notebook in the root of the repo


# delete all tweets
# for status in timeline:
#     f"Destroying status {status.id}"
#     api.DestroyStatus(status.id)
#     print("STATUS DESTROYED SUCCESSFULLY")


# print("The timeline has now been purged.")
