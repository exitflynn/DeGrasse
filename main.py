import discord, argparse
import config, functions

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
    print(message.content)
    # ignore messages from the bot itself
    if message.author == client.user:
        return
    msg_string = "..."

    if "?" in message.content:
        msg_string = "The universe is under no obligation to make sense to you."
        await message.channel.send(msg_string)
        
    if "space" in message.content:
        print(1)
        msg_string = await functions.apod(api_key)
        await message.channel.send(msg_string)
    
    else:
    	await message.channel.send(msg_string)

client.run(config.bot_token)
