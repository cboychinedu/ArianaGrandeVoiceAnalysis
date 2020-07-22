#!/usr/bin/env python3 

# Author: 
# Description: This script was created for converting mp3 audio files into 
# Wave format for further preprocessing. 

# Importing the necessary modules 
import os 
from os import path 
from pydub import AudioSegment 

# Getting the path to the working directory 
path = os.getcwd()

# Setting the path to the mp3 audio files 
# Getting the path to Ariana mp3 songs 
ArianaFolder = "Ariana" 
# Joining path for all Ariana songs 
ArianaPath = os.path.sep.join([path, ArianaFolder])
# Converting the mp3 songs into wav format 
files = os.listdir(ArianaPath) 
# Getting the count 
first_count = 1
# Getting the full path to ariana songs 
for songs in sorted(files): 
    # Getting the full path to ariana songs 
    source = os.path.sep.join([ArianaPath, songs])
    # Converting the mp3 to wav 
    sound = AudioSegment.from_mp3(source) 
    # Exporting the converted mp3 files to a new folder 
    wavName = "ArianaWav/00{}.wav".format(first_count) 
    sound.export(wavName, format="wav")

    # Increasing the count by 1 
    first_count += 1 


# Setting the path to the mp3 audio files 
# Getting the path to Others mp3 sounds 
Others = "Others" 
# Joining the path for all the songs in the directory 
Others_songs = os.path.sep.join([path, Others])
# Converting the mp3 songs into a wav format 
others_files = os.listdir(Others_songs) 
# Setting the value for count as one 
second_count = 1 
# Getting the full path to the other songs directory 
for songs in sorted(others_files): 
    # Getting the full path to the songs 
    source = os.path.sep.join([Others_songs, songs])
    # Converting the mp3 files into wav format 
    sound = AudioSegment.from_mp3(source) 
    # Exporting the converted wav files to the new folder 
    wavName = "OthersWav/00{}.wav".format(second_count) 
    sound.export(wavName, format="wav") 
    # Increase the count by 1 
    second_count += 1 

# Displaying details 
print("[INFO] Conversion Completed with the following: \n"); 
print("Count For Ariana: ", first_count); 
print("Count For Unknown: ", second_count); 





