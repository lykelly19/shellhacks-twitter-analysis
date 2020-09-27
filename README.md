# Shell Hacks 2020 - #TweetHappy Twitter App

## Inspiration
Twitter is one of the largest social media platforms in the world, and it engages millions of users around the globe in important conversations. Twitter is where social change sparks. In order to ensure civility on the platform and encourage more people to join in on these important conversations, we need to ensure that Twitter is a safe and inclusive space.     

It can take a long time before a flagged tweet is reviewed. Instead of removing the tweet after it has been posted and many have seen it, **what if we prevent the tweet from being sent in the first place?** And secondly, **what if we could hide potentially toxic tweets from the user?**

Our proposed solution focuses on those two key questions.  

## What it does
I created a web app with Flask (Python/HTML/CSS) and deployed it with Heroku. The web app has a simple and intuitive UI design and incorporates digitally drawn images of birds that are used strategically to help foster a safer space.    

The app emulates how a **safe mode feature** in Twitter would work like.    

The Python backend queries Twitter's API in which it posts tweets and retrieves the user's timeline and search results.  

**#TweetHappy and User Timeline**   
When the user tweets something from the app I created, the tweet is analyzed and a simple report is sent to the user. I used **VADER sentiment analysis** in order to evaluate whether the tweet is positive, neutral, or negative. The quantitative compound score and qualitative score from the VADER sentiment analysis are displayed to the user. The VADER sentiment analysis scale goes from -1 to 1, meaning most negative to most positive respectively. **If the tweet is negative, the user is warned of the potential consequences of their tweet and is highly encouraged to revise it.** The user can look at the scores and determine what their best course of action should be and see how potentially toxic their tweet may be.     

When the user decides to tweet their message, the user returns to the home page and the tweet should be shown in the user timeline.  

**#SafeSearch**  
Conversations can quickly get heated, and sometimes all we need during these difficult times is positivity. Through #SafeSearch, users can search as they would in Twitter. The backend queries the API with the search string and retrieves several tweets in return. VADER sentiment analysis is also run through these tweets, and **tweets that are determined to be negative are not included in the feed**. The tweets were embedded to the app using Twitter's oEmbed.   

## Accomplishments that we're proud of
Completing a project in such a short period of time, finally fixing a bunch of bugs and errors, successfully creating a simulated Twitter app with Flask, and successfully deploying a demo version with Heroku.   

## What we learned
How to sustain through and stay motivated throughout a project, how to really use Flask as a beginner user (gained a much better understanding of it and learned how forms from the HTML side work with the backend in Python), and how to use the new oEmbed endpoint with Twitter API v2 that recently released.   

## What's next for #TweetHappy
Incorporating sentiment analysis for the different languages on the platform and trying out different sentiment analysis methods   
