# encrypt.py

import cv2
import os

def encrypt(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    d = {chr(i): i for i in range(256)}  # Handle extended ASCII
    c = {i: chr(i) for i in range(256)}

    m = 0
    n = 0
    z = 0

    if len(message) > img.shape[0] * img.shape[1] * img.shape[2]:
        raise ValueError("Message too long to fit in image.")


    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n = (n + 1) % img.shape[0] # Wrap around rows
        m = (m + 1) % img.shape[1] # Wrap around columns
        z = (z + 1) % img.shape[2] # Wrap around color channels


    encrypted_image_path = "encryptedImage.png" # Changed to png for better quality
    cv2.imwrite(encrypted_image_path, img)
    print(f"Image encrypted and saved as {encrypted_image_path}")

    # Optional: Open the image (platform-specific)
    # os.system(f"start {encrypted_image_path}")  # Windows
    # os.system(f"open {encrypted_image_path}")   # macOS
    # os.system(f"xdg-open {encrypted_image_path}") # Linux


if __name__ == "__main__":
    image_path = input("Enter image path: ")
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ") # Password is not actually used in encryption, but it's used in decryption.
    try:
        encrypt(image_path, message, password)
    except Exception as e:
        print(f"Error during encryption: {e}")
