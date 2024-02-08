from PIL import Image
import base64
import requests
from io import BytesIO
import json


def encode_image_url_to_base64(image_url):
    # Fetch the image from the URL
    response = requests.get(image_url)
    response.raise_for_status()

    # Read the binary data of the image
    image_binary = response.content

    # Encode the binary data to base64
    base64_encoded = base64.b64encode(image_binary)

    # Convert bytes to string
    base64_string = base64_encoded.decode('utf-8')

    # Return the base64 string
    return base64_string

def decode_base64_to_image(base64_string, output_path):
    # Decode the base64 string to binary data
    image_binary = base64.b64decode(base64_string)

    # Create an Image object from binary data
    image = Image.open(BytesIO(image_binary))

    # Save the image to the specified output path
    image.save(output_path)

# Example usage with image URLs
image_urls = [
    'https://logohistory.net/wp-content/uploads/2022/10/Facebook-Logo-2019.png',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREEKwkGAASovqJRScxhasZu2mgmRORlSFOdA&usqp=CAU',
    # Add more image URLs as needed
]

# Load existing saved data from .spp file if it exists
try:
    with open('decoded_images.spp', 'r') as spp_file:
        decoded_data = json.load(spp_file)
except FileNotFoundError:
    decoded_data = {}

for url in image_urls:
    encoded_string = encode_image_url_to_base64(url)
    output_path = f"{image_urls.index(url)}_decoded_image.png"
    decode_base64_to_image(encoded_string, output_path)

    # Save decoded string and image URL to the dictionary
    decoded_data[output_path] = {'base64_string': encoded_string, 'image_url': url}

# Save the updated dictionary to .spp file
with open('decoded_images_data.json', 'w') as spp_file:
    json.dump(decoded_data, spp_file, indent=2)
