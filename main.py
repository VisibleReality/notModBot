"""
Discord bot to annoy Solace

© VisibleReality
"""
import discord
import logging

client = discord.Client()

logging.basicConfig(level = logging.INFO)


# On bot ready (connected and logged in)
@client.event
async def on_ready ():
	print(f"Logged in as {client.user}")


# On message received
@client.event
async def on_message (message: discord.Message):
	if message.author.id == 511818194424561674:
		await message.add_reaction("<:notmod:837275584924221470>")


# Start the bot
with open("token.txt") as tokenFile:
	token = tokenFile.read().strip()
client.run(token)
