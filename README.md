# BOTAN Satellite
![Botan-satellite-image](https://db-satnogs.freetls.fastly.net/media/satellites/DSC_3451_M7LlLPt.JPG)
The BOTAN satellite is
an ultra-small satellite built by students at the Chiba Institute of Technology in Japan. It is equipped with a camera and amateur radio capabilities, and its mission is to photograph specific features on Earth, such as pumice rafts and aurora borealis.
# 🛰️ BOTAN Image Decoder
BOTAN Satellite Frame Decoder is a Python-based tool that reads raw image transmission frames from the BOTAN CubeSat and reconstructs them into a complete JPEG image.

The satellite transmits its image data as hex-encoded or binary frame packets, which are stored in a CSV file during signal reception. This program parses those frames, detects valid JPEG headers and end markers, and rebuilds the original image automatically. 

Cam data format is given below,
![Botan-satellite-Cam-Format](https://lh3.googleusercontent.com/sitesv/AICyYdapstuaL7YKF5-WUeBBqj8BXBQOtCiqNh7QtH4BCSLoIKlW0-u1QtFmGgXpgGL7tZisAVSkqtyubVUqrqYAJ3L9Fvvucy_LUQriZF5ZrddTGeE1Y5lCE-kRMpe5SWQzE6_44lBtiRsCyMAXTBwea7VRsQT70_mF8btSArGkM_ASlJp5Q6PaDsNu635Dx2F3WLq_knVg-cgAtJPN3r5i5-1Pyccbw1QH3tPmHr0=w1280)
# 🚀 Features
📄 Reads frame data from CSV file (hex or binary format)

🧩 Automatically detects JPEG start (FFD8) and end (FFD9) markers

🖼️ Reconstructs the full image from fragmented frames

🔍 Detects missing/corrupted frames and allows zero or neutral-fill recovery

🌈 Supports color correction to fix green-tinted or incomplete images

💾 Outputs recovered image as .jpg

# 🧰 Requirements
Python 3.8+

Libraries:

# 🧾 Example Usage
# 🖼️ Output Example
# 📚 License
This project is licensed under the MIT License — free for personal and research use.
