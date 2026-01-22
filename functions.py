from datetime import *


def get_time():
    return datetime.now()

def check_if_time():
    if get_time().hour == 12:
        return True