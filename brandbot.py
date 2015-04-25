#!/usr/bin/env python

# This uses tweepy because it offers Rewtweet capability

import tweepy
import time

_skip = "Skipping tweet by @"
_rt = "Retweeted tweet by @"

def retweeted(api, s, my_id):
    rts = api.retweets(s.id)
    if len(rts) > 0:
        for rt in rts:
            if rt.user.id == my_id:
                ret = True
                break
            else:
                ret = False
    else:
        ret = False
    return ret

def tweet_by_me(api, s, my_id):
    if s.user.id == my_id:
        ret = True
    else:
        ret = False
    return ret

def main():
    # setup shit
    consumer_key = "v8xVBZlXBp2AJoWI3VjDjzDkC"
    consumer_secret = "Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D"
    access_token_key = "3173564472-f1pPsQ12GdB9xpyeYDxQjFPAzz4wcdvXm7w99RS"
    access_token_secret = "UqWqkjS09qRkx3zV8UDIBoFLUosaodbEpvm6COHUha107"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    
    # Our User ID
    my_id = api.me().id
    
    # infinite loop
    while True:
        search = api.search("\"#brand\"")
        for s in search:
            # Have we already RTed or is it by us?
            if retweeted(api, s, my_id) or tweet_by_me(api, s, my_id):
                print _skip + s.user.screen_name
            else:
                # RT that dank shit bruh
                api.retweet(s.id)
                print _rt + s.user.screen_name

            # follow the user just because fuck that user
            api.create_friendship(s.user.id)

        time.sleep(300)

if __name__ == "__main__":
    main()
