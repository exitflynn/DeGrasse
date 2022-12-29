import discord, requests, json, argparse
from config import bot_key
parser = argparse.ArgumentParser()

parser.add_argument("-k", "--key", help="NASA API Key")
args = parser.parse_args()
api_key = args.key

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("This bot is now ready. How do you do fellow kids?")

@client.event
async def on_message(message):
    # ignore messages from the bot itself
    print(message.content)
    if message.author == client.user:
        return
    if "?" in message.content:
        sendmsg = "The universe is under no obligation to make sense to you."
    elif "space" in message.content:
        if not api_key:
            sendmsg = "I'd have loved to show you a really awesome space image right about now but alas you didn't pass any API key. You can pass one using the `-k` or the `--key` flag."
        else:
            url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
            resp = requests.get(url)
            data = json.loads(resp.text)
            imgurl = data['hdurl']
            sendmsg = imgurl
    await message.channel.send(sendmsg)

client.run(bot_key)
