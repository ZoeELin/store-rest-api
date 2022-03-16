import argparse
import base64
import requests

# click_time = {}
# production_url = 'http://www.zoe-lin.me'
production_url = 'http://127.0.0.1:5000'

parser = argparse.ArgumentParser()
parser.add_argument("long_url")
args = parser.parse_args()
# print(args.long_url)


 # URL and Filename Safe Base64 Encoding
urlSafeEncodedBytes = base64.urlsafe_b64encode(args.long_url.encode("utf-8"))
urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")

# print(urlSafeEncodedStr)
#
# print("http://www.zoe-lin.me/transform/" + urlSafeEncodedStr)

r = requests.post(production_url + "/transform/" + urlSafeEncodedStr)

# print(r.json())
# print(r.headers)
# print(r.content)
print(f"{production_url}/{r.json()}")
