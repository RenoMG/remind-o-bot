import time, os, discord
from functions import check_if_time, get_time, get_time_until
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

    channel = client.get_channel(int(os.getenv('CHANNEL')))

    while True: 
        time.sleep(5)
        if check_if_time:
            countdown_embed = discord.Embed(
                title="Daily Japan Reminder!",
                type="rich",
                description=f"Time until JAPAN:\n{get_time_until()}"
            )
            countdown_embed.set_thumbnail(url="https://media.discordapp.net/attachments/1334389884470956075/1463782087843643427/paid-advance-seat-reservation.png?ex=697314cd&is=6971c34d&hm=99a5b2deb88e1d2de0b2e902014e74955a03796b93670c686812279ca99db079&=&format=webp&quality=lossless")
            await channel.send(embed=countdown_embed)

client.run(os.getenv('TOKEN'))
