from tweety.bot import Twitter
import time
import regex as re
import subprocess



CODE_SIZE = 10

regex_pattern = r"(?<=Text\s)\b\w{10}\b"
global previous_tweet
previous_tweet = 'adam'

def send_imessage(text, recipient):
    apple_script = f'''
    tell application "Messages"
        send "{text}" to buddy "{recipient}" of (service 1 whose service type is iMessage)
    end tell
    '''

    subprocess.run(["osascript", "-e", apple_script])

def run_code():
    app = Twitter()
    username = "ChipotleTweets"
    global previous_tweet
    
    user = app.get_user_info(username)
    all_tweets = app.get_tweets(username)
    
    try:
        tweet = all_tweets[0].text
        print(all_tweets[0].text)
        matches = re.findall(regex_pattern, tweet)
        for code in matches:
            print("Extracted code:", code)
        if (tweet != previous_tweet):
            print('new!')
            send_imessage(code,"888222")
            send_imessage(code,"4")
        previous_tweet = tweet
        
    except IndexError:
        print("Index out of range. Skipping this iteration.")
    

# Define the total number of iterations (1.5 hours = 5400 seconds / 2 seconds per iteration)
total_iterations = 5400

# Run the code every 2 seconds for the specified duration
for i in range(total_iterations):
    run_code()
    time.sleep(1)
