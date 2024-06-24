import os
from PIL import Image

# Get the current working directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Iterate over all files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(current_directory, filename)
        image = Image.open(image_path)

        # Define the coordinates for cropping
        left = 0
        top = 0  # Height of the header to be removed
        right = image.width
        bottom = image.height - 10  # Height of the bottom part to be removed

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image with the same name
        cropped_image.save(image_path)

        print(f'{filename} cropped and saved successfully.')