import yaml
import twitter
from textblob import TextBlob


# load in twitter sekrits
with open('tweeter.yaml', 'r') as stream:
    contents = stream.read()
    config = yaml.load(contents, Loader=yaml.BaseLoader)

# authenticate tweeter
api = twitter.Api(
                consumer_key=config['twitter']['consumer_key'],
                consumer_secret=config['twitter']['consumer_secret'],
                access_token_key=config['twitter']['access_token_key'],
                access_token_secret=config['twitter']['access_token_secret'],
                sleep_on_rate_limit=True
                )

print(api.VerifyCredentials())
# search tweets
statuses = api.GetUserTimeline()
status_dict = {}

# for status in statuses:
#     if status.text


print('retrieving all tweets ever posted')



# run sentiment analysis


# remove negative tweets


# delete le tweets


