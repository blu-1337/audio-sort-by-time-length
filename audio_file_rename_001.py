import os

# Define prefix
prefix = "BMB_"

# Get all wav files recursively  
files = []
for root, dirs, fnames in os.walk('.'):
    for fname in fnames:
        if fname.lower().endswith('.wav'):
            files.append(os.path.join(root, fname)) 

# Rename files            
count = 1
for filename in files:  
    dirname = os.path.dirname(filename)
    basename, ext = os.path.splitext(os.path.basename(filename))
    
    new_name = os.path.join(dirname, prefix + str(format(count, '03d')) + ext)
    
    print(f"Renaming {filename} to {new_name}")
    os.rename(filename, new_name)
    count += 1
    
print(f"Renamed {len(files)} files")

input("Press Enter to exit...")
