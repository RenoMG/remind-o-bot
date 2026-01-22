import os, discord
from functions import check_if_time, get_time_until
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@tasks.loop(seconds=5)
async def japan_reminder():
    if check_if_time():
        channel = client.get_channel(int(os.getenv('CHANNEL')))
        countdown_embed = discord.Embed(
            title="Daily Japan Reminder!",
            type="rich",
            description=f"Time until JAPAN:\n**{get_time_until()}**",
            color=discord.Colour.random()
        )
        countdown_embed.set_image(url="https://media.discordapp.net/attachments/1334389884470956075/1463782087843643427/paid-advance-seat-reservation.png")
        await channel.send(f"@everyone DAILY JAPAN TIME UPDATE!")
        await channel.send(embed=countdown_embed)

@japan_reminder.before_loop
async def before_reminder():
    await client.wait_until_ready()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    japan_reminder.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$japan'):
        countdown_embed = discord.Embed(
            title="Daily Japan Reminder!",
            type="rich",
            description=f"Time until JAPAN:\n**{get_time_until()}**",
            color=discord.Colour.random()
        )
        countdown_embed.set_image(url="https://media.discordapp.net/attachments/1334389884470956075/1463782087843643427/paid-advance-seat-reservation.png")
        await message.channel.send(embed=countdown_embed)

client.run(os.getenv('TOKEN'))