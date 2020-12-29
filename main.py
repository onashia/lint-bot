
# load packages
import discord
import os
import requests
import json

# connect to discord
client = discord.Client()

# get anime quote from an api
def get_anime_quote():
  response = requests.get("https://animechanapi.xyz/api/quotes/random")
  output = json.loads(response.text)
  data = output['data']
  # format quote as "quote" ~ author
  quote = "\"" + data[0]['quote'] + "\" *~ " + data[0]['character'] + "*"
  return(quote)

# get inspirational quote from an api
def get_inspirational_quote():
  response = requests.get("https://zenquotes.io/api/random")
  output = json.loads(response.text)
  quote = "\"" + output[0]['q'] + "\" *~ " + output[0]['a'] + "*"
  return(quote)

# when bot is ready write console response
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# when user writes specific message lint-kun will respond
@client.event
async def on_message(message):
  # do not respond if user is lint-kun
  if message.author == client.user:
    return

  # respond to $hello
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  # respond to $help
  if message.content.startswith('$help'):
    await message.channel.send('No thank you.')
  # respond to $quote
  if message.content.startswith('$quote'):
    quote = get_anime_quote()
    await message.channel.send(quote)
  # respond to $inspiration
  if message.content.startswith('$inspiration'):
    quote = get_inspirational_quote()
    await message.channel.send(quote)


# start lint-kun
client.run(os.getenv('TOKEN'))