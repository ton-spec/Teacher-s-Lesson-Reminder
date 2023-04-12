

import datetime
from gtts import gTTS
import os
import time

# Define the timetable dictionary
timetable = {
    "Wednesday": {
        "8:00-8:40": "FORM 4-GEOGRAPHY",
        "8:40-9:20": "FORM 3- HISTORY",
        "9:20-10:00": "BREAK",
        "10:00-10:40": "FORM 4",
        "10:40-11:20": "FORM 1",
        "11:20-12:00": "FORM 2",
        "12:00-12:40": "FORM 3",
        "12:40-13:20": "FORM 4",
        "13:20-14:00": "FORM 1",
        "14:00-14:40": "FORM 2",
        "14:40-15:00": "FORM 3",
        "15:00-15:40": "FORM 4",
        "15:40-16:20": "FORM 2",
        "16:20-17:00": "FORM 3"
        # ... rest of the timetable
    },
    "Thursday": {
        # ... Tuesday timetable
    },
    "Friday": {
        # ... Wednesday timetable
    },
    # ... rest of the days
}

current_day = datetime.datetime.now().strftime("%A") # get the current day's name

# Check if the day name is valid
if current_day not in timetable:
    print("Invalid day name!")
else:
    while True:  # repeat forever
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        # Loop through the timetable to find the matching class
        for day, classes in timetable.items():
            if day == current_day:
                for time_range, class_name in classes.items():
                    start_time, end_time = time_range.split("-")
                    if start_time <= current_time <= end_time:
                        message = f"On {day}, you have {class_name} from {time_range}."
                        tts = gTTS(message)
                        tts.save('message.mp3')
                        os.system('mpg321 message.mp3')
                        os.remove('message.mp3')
                        break
        time.sleep(30)  # wait for 30 seconds
