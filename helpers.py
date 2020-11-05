from app.models import ShortUrl
import random 

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

def generate_shortlink():
    shortlink = ""
    while (True):
        shortlink = ''.join(random.choice(chars) for i in range(4))
        shorturl = ShortUrl.query.filter_by(shortlink=shortlink).first()
        if shorturl is None:
            break
    return shortlink

def is_valid_url(url):
    if len(url) != 0:
        return True
    return False
