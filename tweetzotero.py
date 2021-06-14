from bs4 import BeautifulSoup
from keys import *
import webbrowser
import pyautogui
import requests
import argparse
import tweepy
import time

def fetch_urls_in_tweet(api, status_id):
    status = api.get_status(status_id, tweet_mode="extended")
    try:
        content = status.retweeted_status.full_text
    except AttributeError:  
        content = status.full_text
    urls = [i for i in content.split() if i.lower().startswith(("https://", "buff.ly", "t.co", "bit.ly"))]
    return urls

def request_url(short_url):
    try:
        extended = requests.get(short_url, timeout=5)
        return extended.url
    except Exception as e: 
        print(e)

def get_extended_url(api, tweet_list):
    all_urls = list()
    all_urls.extend(fetch_urls_in_tweet(api=api, status_id=i) for i in tweet_list)
    all_urls = [item for sublist in all_urls for item in sublist]
    extended_urls = [request_url(i) for i in all_urls]
    save_list(inlist=extended_urls)
    return extended_urls

def save_list(inlist):
    url_list = [i for i in inlist if i is not None]
    with open('all_urls.txt', 'w') as fh:
        for item in url_list:
            fh.write("%s\n" % item)

def save_to_zotero(url):
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(10)


def run(tweet_ids):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    extended_urls = get_extended_url(api=api, tweet_list=tweet_ids)
    for url in extended_urls:
        try:
            save_to_zotero(url=url)
        except Exception as e: 
            print(e)


parser = argparse.ArgumentParser(description='Save Twitter Bookmarked Papers to Zotero')
parser.add_argument('-i','--input', help='Provide input', required=True)
args = parser.parse_args()

if args.input:
    try:
        with open(args.input, "r") as handle:
            tweet_ids=[i.split(',')[0].split('/')[-1] for i in handle.readlines()[1:]]
        run(tweet_ids=tweet_ids)
    except Exception as e: 
        print(e)
else:
    print('Provide an input file') 