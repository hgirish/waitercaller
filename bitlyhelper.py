import config
import urllib
import json

TOKEN = config.bitly_oauth_token
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"
class BitlyHelper:

    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urllib.request.urlopen(url).read().decode('utf-8')
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(str(e))