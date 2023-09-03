# Small Python Scripts

This is a small collection of some useful Python scripts.

# Prerequisites
1. python:
  * download python from https://www.python.org/downloads/
2. pip install scipy 
  * run this command in cmd (on Windows, for example)
  * this is used by "audio_files_sort.py"

## audio_files_sort.py

### Script Description
Sort your audio file by length of the audio into folders. This will create two folder "long" and "short" and will move the .wav files inside of them. If the .wav is longer than 3s it will go to "long", if it's shorter then it will go to "short". This script needs to be in the same folder as the .wav files you want to sort. Your folder should look something like this:

  * sound1.wav
  * sound2.wav
  * sound3.wav
  * audio_files_sort.py

### How To Use

1. Place the "audio_files_sort.py" script in the same folder you have your .wav files that you want to sort.
2. Run the "audio_files_sort.py" script.
3. Press "Enter" at the end of the script if prompted.
   
Edit your length accordingly in the scripts for your needs.

## audio_file_rename_001.py

### Script Description

This script renames all the .wav files following a pattern like "BMB_001", "BMB_002" etc. This takes all files from the current folder and all its subfolders.

### How To Use

1. Place the "audio_file_rename_001.py" script in the same folder you have your .wav files that you want to rename.
2. Run the "audio_file_rename_001.py" script.
3. Press "Enter" at the end of the script if prompted.

