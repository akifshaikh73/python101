def scan_tweet(handle,tweet):
    if(handle == "@realdonaldtrump"):
        return "fake news!!"
    words = ["5G","COVID","Bill Gates","Fauci","vaccine"]    
    matchcount=0
    tweet = tweet.lower()
    
    for word in words:
        #if(tweet.find(word.lower()) > 0):
        if(word.lower() in tweet):
           matchcount=matchcount+1
    
    
    if(matchcount >= 3):
        return "fake news!!"
    return "legit"                


print(scan_tweet("@realdonaldtrump","sober tweet"))
print(scan_tweet("@biden","sober tweet"))
print(scan_tweet("@random","if you take the vaccine , you will become a 5G tower. Fauci and Bill gates will become millionaires"))