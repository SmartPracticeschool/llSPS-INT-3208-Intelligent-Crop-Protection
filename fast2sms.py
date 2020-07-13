import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"AoG6FDNZMByHXcJri5z792RUx0vOfeLaQd4ngk3STWYVElCjwhCYW2sE74wAKg3iGban9ZJ1hdym0HQD","sender_id":"FSTSMS","message":"The crop was filled with insects","language":"english","route":"p","numbers":"7993554909,6303494845"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
