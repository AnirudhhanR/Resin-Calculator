from datetime import datetime, timedelta
import math


def calculate_resin(resin_increment, target_time, max_resin):
    resin_per_increment = 8

    current_time = datetime.now()
    target_hour, target_minute = map(int, target_time.split(':'))
    target_time_today = current_time.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    

    if target_time_today < current_time:
        target_time_today += timedelta(days=1)
    
    minutes_to_play = (target_time_today - current_time).total_seconds() / 60
    increments_needed = minutes_to_play / resin_per_increment
    total_resin = resin_increment + increments_needed
    total_resin = max(0, min(total_resin, max_resin))
    return total_resin

MAX_RESIN = 200
resin_input = int(input("Enter current resin: "))
target_time = input("Enter target play time (24-hour format HH:MM): ")
resin_at_play_time = calculate_resin(resin_input, target_time, MAX_RESIN)
resin_at_play_time = math.floor(resin_at_play_time)
print(f"Resin at {target_time}: {resin_at_play_time}")
