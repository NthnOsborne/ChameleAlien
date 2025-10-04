import discord, os
import responses

async def send_message(message, user_message):
  response = responses.get_response(user_message)
  # DM
  await message.author.send(response)

def run_discord_bot():
  Token = os.environ["BOT_TOKEN"]
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    print(f'{client.user} is now running')

  @clinet.event
  async def on_message(message):
    if message.author == client.user:
      return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" ({channel})')
