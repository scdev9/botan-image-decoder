"""
Copyright © 2025 Shamika Chathuranga.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
(the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import re
from pathlib import Path

# extract_botan_frames.py

input_file = "botan.csv"
output_file = "filtered_frames.txt"
camdata_file="camdata.txt"
img_data_file="test.txt"
final_jpg_data="jpg.txt"
sorted_data="sorted_data.txt"


# reference frame 
target_prefix = "94A662B29"
ref_len = 166
callsign_len=38
frames=0
img_no=0
lines = []
filtered_frames="filtered_frames.txt"


def sorted_output(input_file):
    
    # Read and parse lines
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
           
            if len(parts) >= 2:
                try:
                    key = int(parts[0], 16)  # Convert hex to integer
                    lines.append((key, line))
                    
                except ValueError:
                    pass  # Skip lines that don't start with valid hex
    
    # Sort by hex key
    lines.sort(key=lambda x: x[0])
    
    # Keep only unique keys
    unique_lines = []
    seen_keys = set()
    for key, line in lines:
        if key not in seen_keys:
            unique_lines.append(line)
            seen_keys.add(key)
    
    # Write sorted unique lines to output file
    with open(sorted_data, "w") as f:
        for line in unique_lines:
            f.write(line + "\n")
    print(f"✅ Sorted unique lines saved to {sorted_data}")
   


def camdata(filtered_frames):
    frames=0
    with open(filtered_frames,"r") as infile,open(camdata_file,"w") as outfile:
         for line in infile:
             part=line[callsign_len:].strip()
             outfile.write(part+"\n")
             frames+=1
    print(f"✅ Done! CAM Data frames saved to '{camdata_file}',{frames} Frames Saved!")
             
def data_process(camdata_file):
     frames=0
     with open(camdata_file, "r") as infile, open(img_data_file, "w") as outfile:
      for line in infile:
        part1 = line[:6].strip()
        part2=line[6:].strip()

        
        if part1.startswith(img_no):
            outfile.write(part1+" "+part2+ "\n")
            frames+=1
     print(f"✅ Done! Image frames saved to '{img_data_file}',{frames} Frames Saved!")
     sorted_output(img_data_file)




def image_process():

    with open(sorted_data,"r") as f,open(final_jpg_data, "w") as d:
        for line in f:
            x=line[7:].strip()
            d.write(x+"\n")
    
    
    
    print(f"✅ Final jpg data saved to {final_jpg_data}")

    # Read all hex text from file
    data = Path(final_jpg_data).read_text()

    # Remove spaces, newlines, etc.
    data = re.sub(r'[^0-9A-Fa-f]', '', data)

    # Convert to bytes
    raw = bytes.fromhex(data)

    # Find all JPEG frames between FF D8 and FF D9
    frames = []
    start = 0

    while True:
       soi = raw.find(b'\xFF\xD8', start)
       if soi == -1:
           print("❌ Not found jpg start marker")
           break
       
       print("✅ Found! jpg start marker")

       eoi = raw.find(b'\xFF\xD9', soi)
       if eoi == -1:
           print("❌ Not found jpg end marker")
           break
       
       print("✅ Found! jpg end marker")
   
       frames.append(raw[soi:eoi + 2])
       start = eoi + 2
   
    

    print(f"Extracted {len(frames)} JPEG frames.")

    # Save them as individual image files
    for i, frame in enumerate(frames):
      with open(f"frame_{i:03d}.jpg", "wb") as f:
        f.write(frame)



             



with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        parts = line.strip().split("|")
        if len(parts) < 2:
            continue

        frame_data = parts[1].strip()  # the hex data part (between pipes)
        if frame_data.startswith(target_prefix) and len(frame_data) == ref_len:
            outfile.write(frame_data + "\n")
            frames+=1

print(f"✅ Done! Filtered frames saved to '{output_file}',{frames} Frames Saved!")


camdata(filtered_frames)
img_no=input("Enter Image Number:")
data_process(camdata_file)
image_process()