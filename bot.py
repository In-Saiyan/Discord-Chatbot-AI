from email import message
import call
import discord
import os
import dotenv
dotenv.load_dotenv()

token = os.getenv("TOKEN")
channel = int(os.getenv("CHANNELID"))
client = discord.Client()
call.start(train=False)

@client.event
async def on_ready():
    print(f"Logged in as : {client.user} with ID: {client.user.id}")

@client.event
async def on_message(msg):
    if msg.channel.id != channel or msg.author.bot:
        return 0
    else:
        await msg.reply(call.get(msg.content))
client.run(token)