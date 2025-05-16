import os
import discord
from discord.ext import commands
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

# Initialize OpenAI client (new SDK style)
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_KEY"),
    organization=os.getenv("OPENAI_ORG")
)

@client.event
async def on_ready():
    print('Logged in')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.endswith('?'):
        try:
            # Build chat-based message history
            chat_response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are David, a self-assured, sarcastic assistant created by "
                            "<@201227461407670272> and <@Shadowzfire>. You answer questions "
                            "reluctantly and often mock or insult the user in a humorous way."
                        )
                    },
                    {
                        "role": "user",
                        "content": message.content
                    }
                ],
                temperature=0.6,
                max_tokens=100,
                top_p=0.8,
                frequency_penalty=0.3,
                presence_penalty=0.1
            )

            await message.reply(chat_response.choices[0].message.content.strip())

        except Exception as e:
            print(e)
            await message.reply("Oops. I tried to think, but it hurt.")

    await client.process_commands(message)

client.run(os.getenv("DISCORD_TOKEN"))
