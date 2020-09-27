from flask import Flask, request, render_template, redirect, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import os
import requests
import json

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))
base_url = "https://publish.twitter.com/oembed"

# Create API object
api = tweepy.API(auth, wait_on_rate_limit_notify=True)

my_tweet = ""

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/input', methods = ['POST'])
def analyze():
    global my_tweet
    my_tweet = request.form['my-tweet']
    score = analyzer.polarity_scores(my_tweet)
    sentiment_message = ""
    sentiment_message2 = ""
    polarity_text = ""

    if score['compound'] < 0:
        sentiment_message = "Please consider revising your tweet. Harmful language may be hurtful to users of the platform."
        sentiment_message2 = "Let's make sure we have #HealthyConversations on Twitter."
        polarity_text = "Negative"
        return render_template('tweet-negative.html', score=score['compound'], my_tweet=my_tweet, polarity_text=polarity_text, sentiment_message=sentiment_message, sentiment_message2=sentiment_message2)
    elif score['compound'] == 0:
        sentiment_message = "Your tweet should be good to go!"
        polarity_text = "Neutral"
        return render_template('tweet-positive-neutral.html', score=score['compound'], my_tweet=my_tweet, polarity_text=polarity_text, sentiment_message=sentiment_message, sentiment_message2=sentiment_message2)
    else:
        sentiment_message = "Your tweet should be good to go. Thanks for spreading some positivity!"
        polarity_text = "Positive"
        return render_template('tweet-positive-neutral.html', score=score['compound'], my_tweet=my_tweet, polarity_text=polarity_text, sentiment_message=sentiment_message, sentiment_message2=sentiment_message2)


@app.route('/tweet', methods = ['POST'])
def tweet_it():
    api.update_status(my_tweet)
    return render_template('index.html')


@app.route('/search', methods = ['POST'])
def search_it():
    search_string = request.form['search-string']
    counter = 0
    blocked = 0
    html_string1 = ''
    html_string2 = ''
    html_string3 = ''
    html_string4 = ''
    html_string5 = ''
    html_string6 = ''
    html_string7 = ''
    html_string8 = ''
    html_string9 = ''
    html_string10 = ''

    for tweet in tweepy.Cursor(api.search, q=search_string, tweet_mode="extended").items(5):
        url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        payload = {'url': url}
        response = requests.get(base_url, params=payload)
        data = json.loads(response.text)

        score = analyzer.polarity_scores(tweet.full_text)
        if score['compound'] < 0:
            blocked += 1
            continue

        counter += 1

        if counter == 1: html_string1 = data['html']
        elif counter == 2: html_string2 = data['html']
        elif counter == 3: html_string3 = data['html']
        elif counter == 4: html_string4 = data['html']
        elif counter == 5: html_string5 = data['html']
        elif counter == 6: html_string6 = data['html']
        elif counter == 7: html_string7 = data['html']
        elif counter == 8: html_string8 = data['html']
        elif counter == 9: html_string9 = data['html']
        elif counter == 10: html_string10 = data['html']

    note = 'Negative tweets were removed in this search'

    print(blocked)
    search_message = 'Search results for: ' + search_string
    return render_template('search.html', search_message=search_message, note=note, html_string1=html_string1, html_string2=html_string2, html_string3=html_string3, html_string4=html_string4, html_string5=html_string5, html_string6=html_string6, html_string7=html_string7, html_string8=html_string8, html_string9=html_string9, html_string10=html_string10)


@app.route('/search_results', methods = ['POST'])
def find_it():
    return render_template('search.html')


if __name__ == "__main__":
    app.run()
