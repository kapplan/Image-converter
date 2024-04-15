from PIL import Image
import os
import imghdr

# Set the input and output folder paths
input_folder = '/Users/apple/PycharmProjects/pythonProject3/visualisations'
output_folder = '/Users/apple/PycharmProjects/pythonProject3/visualisations'

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)

    # Check if the file is a regular file and is an image (regardless of extension)
    if os.path.isfile(file_path) and imghdr.what(file_path) is not None:
        # Open and convert the image to JPEG
        image = Image.open(file_path)
        jpeg_image = image.convert("RGB")

        # Create the output filename by adding a .jpg extension
        output_filename = os.path.splitext(filename)[0] + ".jpg"

        # Save the JPEG image to the output folder
        jpeg_image.save(os.path.join(output_folder, output_filename))

        # Close the images
        image.close()
        jpeg_image.close()

        # Delete the original PNG file
        os.remove(file_path)

print("Conversion complete.")
