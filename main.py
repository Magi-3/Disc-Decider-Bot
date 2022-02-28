import discord
import random as rd
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!yesorno'):
        x = rd.randrange(1, 3, )
        if x == 1:
            await message.channel.send('Yes')
        else:
            await message.channel.send('No')

    if msg.startswith('!help'):
        await message.chanel.send('Hi, Im the bot that decides, to use me type "!yesorno" and your question then')


keep_alive()


client.run()
