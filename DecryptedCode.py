# decrypt.py

import cv2

def decrypt(image_path, password, original_message_length): # Added original message length
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")

    c = {i: chr(i) for i in range(256)}

    message = ""
    n = 0
    m = 0
    z = 0

    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(original_message_length): # Decrypt only up to the original message length
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % img.shape[2]
        print("Decrypted message:", message)
    else:
        print("Incorrect passcode.")


if __name__ == "__main__":
    image_path = input("Enter encrypted image path: ")
    password = input("Enter passcode: ")
    original_message_length = int(input("Enter the length of the original message: ")) # Get the length

    try:
        decrypt(image_path, password, original_message_length)
    except Exception as e:
        print(f"Error during decryption: {e}")
