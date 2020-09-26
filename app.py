from flask import Flask, request, render_template, redirect, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/input', methods = ['POST'])
def analyze():
    my_tweet = request.form['my-tweet']
    score = analyzer.polarity_scores(my_tweet)
    sentiment_message = ""
    polarity_text = ""

    if score['compound'] < 0:
        sentiment_message = "Are you sure you would like to tweet this? Harmful language may be hurtful to users of the platform. Please consider tweeting something else."
        polarity_text = "Negative"
    elif score['compound'] == 0:
        sentiment_message = "Your tweet should be good to go!"
        polarity_text = "Neutral"
    else:
        sentiment_message = "Your tweet should be good to go. Thanks for spreading some positivity!"
        polarity_text = "Positive"

    return render_template('tweet.html', score=score['compound'], my_tweet=my_tweet, polarity_text=polarity_text, sentiment_message=sentiment_message)

@app.route('/tweet', methods = ['POST'])
def tweet_it():
    return render_template('timeline.html')


if __name__ == "__main__":
    app.run()
