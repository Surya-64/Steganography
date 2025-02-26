# Secure Data Hiding in Image Using Steganography
This project provides a simple tool for encrypting and decrypting text messages within images using steganography.

## Overview

This tool allows you to hide secret messages inside image files. It uses a basic Least Significant Bit (LSB) steganography technique, where the bits of the message are embedded into the least significant bits of the image's pixel values. This makes the changes to the image visually imperceptible.

## Features

* **Encryption:** Encrypts a text message into an image.
* **Decryption:** Decrypts a hidden message from an image.
* **Passcode Protection:** Adds a basic passcode to prevent unauthorized decryption.
* **Clear Error Handling:** Provides informative error messages.
* **Cross-Platform Compatibility:** Uses OpenCV, which is compatible with Windows, macOS, and Linux.
  
## LSB Steganography Technique

This project utilizes the Least Significant Bit (LSB) steganography technique. Here's a brief explanation:

* **How it Works:**
    * Digital images are composed of pixels, and each pixel has color values (typically Red, Green, and Blue - RGB).
    * These color values are represented in binary form.
    * The LSB technique modifies the rightmost bit(s) of these binary values.
    * Since the rightmost bits have the least impact on the overall color, the changes are very subtle and often undetectable by the human eye.
    * In this implementation, each character of the secret message is converted to it's ASCII integer value. That value is then stored in the least significant portion of the image pixel's color values.

## Getting Started

### Prerequisites

* Python 3.x
* OpenCV (`cv2`) library: Install using `pip install opencv-python`
* Use the latest version of Operating System like Windows 10 or higher

### Usage

1.  **Clone the repository:**

    ```bash
    git clone [[(https://github.com/Surya-64/Steganography.git)]
    cd [Steganography]
    ```

2.  **Encryption:**

    ```bash
    python encrypt.py
    ```

    * Follow the prompts to enter the image path, secret message, and passcode.
    * The encrypted image will be saved as `encryptedImage.png`.

3.  **Decryption:**

    ```bash
    python decrypt.py
    ```

    * Follow the prompts to enter the encrypted image path, passcode, and the original message length.
    * The decrypted message will be displayed in the console.

### Example

1.  Encrypt a message:

    ```bash
    python encrypt.py
    Enter image path: mypic.jpg
    Enter secret message: This is a secret message.
    Enter a passcode: mysecretpass
    Image encrypted and saved as encryptedImage.png
    ```

2.  Decrypt the message:

    ```bash
    python decrypt.py
    Enter encrypted image path: encryptedImage.png
    Enter passcode: mysecretpass
    Enter the length of the original message: 25
    Decrypted message: This is a secret message.
    ```

### Important Considerations

* **Message Length:** The length of the message must be shorter than the available pixel space in the image. The decryption script requires the original message length as input.
* **Image Format:** PNG format is recommended to avoid compression artifacts that can corrupt the hidden message.
* **Security:** This implementation provides basic steganography. It is not intended for high-security applications.

### Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
