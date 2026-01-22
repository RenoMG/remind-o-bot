import os
from datetime import *
from dotenv import load_dotenv

load_dotenv()

def get_time():
    return datetime.now()

def check_if_time():
    if get_time().hour == 23:
        return True

def get_time_until():
    flight_time = datetime(int(os.getenv('YEAR')), int(os.getenv('MONTH')), int(os.getenv('DAY')), int(os.getenv('HOUR')), int(os.getenv('MIN')), int(os.getenv('SEC')))
    delta = flight_time - datetime.now()

    total_sec = int(delta.total_seconds())
    days, remainder = divmod(total_sec, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days < 0:
        return "JAPAN TRIP IS ONGOING, TURN OFF THE DAMN BOT!"
    
    return f"{days}d {hours}h {minutes}m {seconds}s"

print(get_time().hour)