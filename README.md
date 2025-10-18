# BOTAN Satellite
![Botan-satellite-image](https://db-satnogs.freetls.fastly.net/media/satellites/DSC_3451_M7LlLPt.JPG)
The BOTAN satellite is
an ultra-small satellite built by students at the Chiba Institute of Technology in Japan. It is equipped with a camera and amateur radio capabilities, and its mission is to photograph specific features on Earth, such as pumice rafts and aurora borealis.
# 🛰️ BOTAN Image Decoder
BOTAN Satellite Frame Decoder is a Python-based tool that reads raw image transmission frames from the BOTAN CubeSat and reconstructs them into a complete JPEG image.

The satellite transmits its image data as hex-encoded or binary frame packets, which are stored in a CSV file during signal reception. This program parses those frames, detects valid JPEG headers and end markers, and rebuilds the original image automatically. 

Cam data format is given below,<img width="1280" height="436" alt="cam" src="https://github.com/user-attachments/assets/4cc40ff3-9373-42d0-bf40-3f638482e373" />

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
In terminal run this command:
````

python3 main.py

````


Output:

<img width="617" height="178" alt="Screenshot From 2025-10-18 18-41-46" src="https://github.com/user-attachments/assets/e1a7c33d-99a7-4f86-bbd0-dd1774a2399f" />

Enter Image Number (Eg:90)
Output:

<img width="617" height="178" alt="Screenshot From 2025-10-18 18-42-06" src="https://github.com/user-attachments/assets/d6795035-ebfe-424b-9d33-088fb0446d26" />


# 🖼️ Output Example
![botan90](https://github.com/user-attachments/assets/364f054f-7ca9-4dc2-a36e-bc5644a69199)

# 📚 License
This project is licensed under the MIT License — free for personal and research use.
