#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2231965603-IsaCkLL2FX2kgRfjajyKv26nfrOrEYou2oY****"
access_token_secret = "AnRILzhT6emwJ0YfyvrxsTTxF2B2z2h4yDTrLFDnw****"
consumer_key = "Ye2egIZgXFmk77WYHifVE****"
consumer_secret = "OeV1gyVOH8wxCRjaow0lartcQqgEiwbQnEm6lQs9KltWkk****"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by keywords
    stream.filter(track=['discount', 'promotion', 'freebie', 'coupon', 'slickdeal', 'dealmoon', 'dealsea', 'doctorofcredit'])