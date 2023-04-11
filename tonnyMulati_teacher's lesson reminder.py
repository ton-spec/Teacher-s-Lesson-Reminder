
from gtts import gTTS
import os
import datetime
import time
# Define the timetable dictionary
timetable = {

    "Monday": {
        
        "8:00  - 8:40 ": "FORM 4- GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": " FIRST BREAK",
        "9:30  - 10:10 ": "FORM 4-MATHS",
        "10:10  - 10:50 ": "FORM 1- KISWAHILI",
        "10:50  - 11:20 ": "TEA BREAK",
        "11:20  - 12:00 ": "FORM 3- ENGLISH",
        "12:00  - 12:40 ": "FORM 4- PHYSICS",
        "12:40  - 13:20 ": "FORM 1- LUNCH BREAK",
        "13:20  - 14:00 ": "FORM 3- BUSINESS STUDIES", 
        "14:00  - 14:40 ": "FORM 3- AGRICULTURE",
        "14:40  - 14:50 ": "FORM 4- AFTERNOON  SHORT BREAK",
        "14:50  - 15:30 ": "FORM 2- BIOLOGY",
        "15:30  - 16:10 ": "FORM 3- GEOGRAPHY! ",
        "16:10  - 17:45 ": "GAMES"
   
    },


  "Tuesday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": " FIRST BREAK",
        "9:30  - 10:10 ": "FORM 4-MATHS",
        "10:10  - 10:50 ": "FORM 1- KISWAHILI",
        "10:50  - 11:20 ": "TEA BREAK",
        "11:20  - 12:00 ": "FORM 3- ENGLISH",
        "12:00  - 12:40 ": "FORM 4- PHYSICS",
        "12:40  - 13:20 ": "FORM 1- LUNCH BREAK",
        "13:20  - 14:00 ": "FORM 3- BUSINESS STUDIES", 
        "14:00  - 14:40 ": "FORM 3- FRENCH",
        "14:40  - 14:50 ": "FORM 4- AFTERNOON  SHORT BREAK",
        "14:50  - 15:30 ": "FORM 2- BIOLOGY",
        "15:30  - 16:10 ": "FORM 3- GEOGRAPHY! ",
        "16:10  - 17:45 ": "CLUBS"

    },
    
    
    "Wednesday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": " FIRST BREAK",
        "9:30  - 10:10 ": "FORM 4-MATHS",
        "10:10  - 10:50 ": "FORM 1- KISWAHILI",
        "10:50  - 11:20 ": "TEA BREAK",
        "11:20  - 12:00 ": "FORM 3- ENGLISH",
        "12:00  - 12:40 ": "FORM 4- PHYSICS",
        "12:40  - 13:20 ": "FORM 1- LUNCH BREAK",
        "13:20  - 14:00 ": "FORM 3- BUSINESS STUDIES", 
        "14:00  - 14:40 ": "FORM 3- COMPUTER STUDIES",
        "14:40  - 14:50 ": "FORM 4- AFTERNOON  SHORT BREAK",
        "14:50  - 15:30 ": "FORM 2- BIOLOGY",
        "15:30  - 16:10 ": "FORM 3- GEOGRAPHY! ",
        "16:10  - 17:45 ": "DEBATES"

    },
      "Thursday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": " FIRST BREAK",
        "9:30  - 10:10 ": "FORM 4-MATHS",
        "10:10  - 10:50 ": "FORM 1- KISWAHILI",
        "10:50  - 11:20 ": "TEA BREAK",
        "11:20  - 12:00 ": "FORM 3- ENGLISH",
        "12:00  - 12:40 ": "FORM 4- PHYSICS",
        "12:40  - 13:20 ": "FORM 1- LUNCH BREAK",
        "13:20  - 14:00 ": "FORM 3- BUSINESS STUDIES", 
        "14:00  - 14:40 ": "FORM 3- HEBREW",
        "14:40  - 14:50 ": "FORM 4- AFTERNOON  SHORT BREAK",
        "14:50  - 15:30 ": "FORM 2- BIOLOGY",
        "15:30  - 16:10 ": "FORM 3- GEOGRAPHY! ",
        "16:10  - 17:45 ": "MOVEMENTS"

    },
    
      "Friday": {
        
        "8:00  - 8:40 ": "FORM 4-GEOGRAPHY",
        "8:40  - 9:20 ": "FORM 3- CHEMISTRY",
        "9:20  - 9:30 ": " FIRST BREAK",
        "9:30  - 10:10 ": "FORM 4-MATHS",
        "10:10  - 10:50 ": "FORM 1- KISWAHILI",
        "10:50  - 11:20 ": "TEA BREAK",
        "11:20  - 12:00 ": "FORM 3- ENGLISH",
        "12:00  - 12:40 ": "FORM 4- PHYSICS",
        "12:40  - 13:20 ": "FORM 1- LUNCH BREAK",
        "13:20  - 14:00 ": "FORM 3- BUSINESS STUDIES", 
        "14:00  - 14:40 ": "FORM 3- MUSIC",
        "14:40  - 14:50 ": "FORM 4- AFTERNOON  SHORT BREAK",
        "14:50  - 15:30 ": "FORM 2- BIOLOGY",
        "15:30  - 16:10 ": "FORM 3- GEOGRAPHY! ",
        "16:10  - 17:45 ": "CLUBS AND SOCIETIES"
       
    }
 
}

def speak(text):
    # Create an instance of gTTS and save the audio file
    tts = gTTS(text=text, lang='en')
    tts.save('audio.mp3')

    # Use the os module to play the audio file
    os.system('mpg321 audio.mp3')
     # Delete the audio file after speaking
    os.remove('audio.mp3')

# Get user input for the current day
dey = input("Enter the current day's name. e.g. Monday: ")

# Get current time
now = datetime.datetime.now()
k = now.strftime("%H:%M")

# Loop through the timetable to find the matching class
while True:
    for day, classes in timetable.items():
        if day == dey:
            for time_range, class_name in classes.items():
                start_time, end_time = time_range.split(" - ")
                if start_time <= k <= end_time:
                    text = f"On {day}, you have {class_name} from {time_range}."
                    speak(text)
                    time.sleep(300)  # Wait for 5 minutes before speaking again
                    break
    else:
        speak("Sorry! You have no lessons at the moment.")
        break
              
