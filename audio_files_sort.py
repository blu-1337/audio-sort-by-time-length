import os
from scipy.io import wavfile
from scipy.io.wavfile import WavFileWarning
import wave
import warnings # add this import

warnings.filterwarnings("ignore", category=WavFileWarning)

script_dir = os.path.dirname(os.path.realpath(__file__))

long_folder = os.path.join(script_dir, 'long')  
short_folder = os.path.join(script_dir, 'short')

warnings.filterwarnings("ignore", category=WavFileWarning)

if not os.path.exists(long_folder):
    os.makedirs(long_folder)
    
if not os.path.exists(short_folder):   
    os.makedirs(short_folder)
    
for filename in os.listdir():
  if filename.lower().endswith('.wav') and wave.open(os.path.join(script_dir, filename)):
    try:
      rate, data = wavfile.read(os.path.join(script_dir, filename))
      duration = len(data) / rate  
      
      if duration > 3:
        os.rename(os.path.join(script_dir, filename), os.path.join(long_folder, filename))
      else:
        os.rename(os.path.join(script_dir, filename), os.path.join(short_folder, filename))
        
    except Exception as e:
      print(f"Error reading {filename}: {e}")

print("Separation complete!")

input("Press Enter to exit...")


