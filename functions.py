import requests, json
# Astronomy Picture of the Day
async def apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    resp = requests.get(url)
    data = json.loads(resp.text)
    try:
        imgurl = data['hdurl']
    except:
        imgurl = data['url']
    msg_string = imgurl
    return msg_string
    
# MArse rover 
async def marse(api_key):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key={api_key}"
    resp = requests.get(url)
    data = json.loads(resp.text)
    try:
        imgurl = data['hdurl']
    except:
        imgurl = data['url']
    msg_string = imgurl
    return msg_string