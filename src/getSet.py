import requests

def get(link):
    url = link
    r = requests.get(url)
    return r.text


