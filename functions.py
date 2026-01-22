import os, zoneinfo
from datetime import *
from dotenv import load_dotenv

load_dotenv()

def get_time_until():
    pst = zoneinfo.ZoneInfo("America/Los_Angeles")

    flight_time = datetime(
        int(os.getenv('YEAR')), 
        int(os.getenv('MONTH')), 
        int(os.getenv('DAY')), 
        int(os.getenv('HOUR')), 
        int(os.getenv('MIN')), 
        int(os.getenv('SEC')),
        tzinfo=pst
        )
    delta = flight_time - datetime.now(pst)

    total_sec = int(delta.total_seconds())
    days, remainder = divmod(total_sec, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days < 0:
        return "JAPAN TRIP IS ONGOING, TURN OFF THE DAMN BOT!"
    
    return f"{days}d {hours}h {minutes}m {seconds}s"