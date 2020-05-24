import yaml
import twitter


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


# return le tweets

# delete le tweets


