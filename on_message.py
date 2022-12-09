import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("How do you do fellow kids?")

@client.event
async def on_message(message):
    # ignore messages from the bot itself
    if message.author == client.user:
        return
    print("i detect a message!")
    await message.channel.send("👀")

client.run("MTA1MDc2MDM0ODEyMDEyNTQ2MA.GnhaVJ.cfwat1MtU1fwB6tyQ-wNE5lMSKVR1WO7_Xa-hI")
