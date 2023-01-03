import requests, json
# Astronomy Picture of the Day
async def apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    resp = requests.get(url)
    data = json.loads(resp.text)
    imgurl = data['hdurl']
    msg_string = imgurl
    return msg_string