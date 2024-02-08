# img2byte

## Overview
`img2byte` is a Python script that decodes images from URLs to base64 strings, saves them to the current directory, and records the decoded data along with the image URLs in a JSON file.

## Dependencies
- [Pillow (PIL Fork)](https://pillow.readthedocs.io/en/stable/)
- [requests](https://docs.python-requests.org/en/latest/)

## Usage
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

2. Run script:
    ```bash
    python img2byte.py

 Check the generated decoded_images_data.json file for the decoded strings and corresponding image URLs.


# Functionality

    The script fetches images from specified URLs.
    Encodes the binary image data to base64 strings.
    Saves the decoded images to the current directory.
    Records the decoded data along with the image URLs in a JSON file.

# Additional Information

    Existing decoded data is loaded from decoded_images_data.json if the file exists.
    The script appends new decoded data to the existing records.
    Each decoded image is saved with a filename like 0_decoded_image.png, 1_decoded_image.png, etc.