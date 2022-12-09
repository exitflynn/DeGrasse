import discord, requests, json

client = discord.Client(intents=discord.Intents.all())

bot_key = ""

@client.event
async def on_ready():
    print("How do you do fellow kids?")

@client.event
async def on_message(message):
    sendmsg = "👀"
    # ignore messages from the bot itself
    print(message.content)
    if message.author == client.user:
        return
    if "?" in message.content:
        sendmsg = "The universe is under no obligation to make sense to you."
        nasa_api_key = ""
    elif "space" in message.content:
        url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
        resp = requests.get(url)
        data = json.loads(resp.text)
        imgurl = data['hdurl']
        sendmsg = imgurl
    await message.channel.send(sendmsg)

client.run(bot_key)
