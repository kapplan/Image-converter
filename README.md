# Image Format Converter

## Overview
This project includes a Python script that automates the conversion of images from various formats (like PNG) to JPEG. It is designed to help streamline workflows that involve handling multiple image files by ensuring all images in a directory are standardized to the JPEG format. The script also cleans up the original files after conversion to optimize storage.

## Features
- **Format Conversion:** Converts images to JPEG format.
- **Automatic Deletion:** Removes original image files post-conversion to free up space.
- **Directory Handling:** Processes all images in a specified input directory and saves the outputs to an optionally different directory.

## Installation

### Prerequisites
- Python 3.6 or newer.
- Pillow library for image handling.

To run this script, you will need Python installed on your system. If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

You also need to install the Pillow library, which can be done via pip:

```
pip install Pillow
```
## Usage
- **Set Up Your Directories:**
Modify the input_folder and output_folder paths in the script to match the directories you are working with.

- **Run the Script:**
Execute the script to convert all images in the input_folder to JPEG format and save them in the output_folder. Original files will be deleted to save space.

Example command to run the script:
```
python image_converter.py
```
Ensure that the script file image_converter.py is in your current working directory or provide the path to where the script is located.

## How It Works
The script performs the following steps:

1. Checks each file in the input directory to confirm it is an image.
2. Opens each image and converts it to JPEG format.
3. Saves the JPEG image in the specified output directory.
4. Removes the original image file from the input directory.

## Dependencies
Pillow: Used for opening, converting, and saving images.

## Contributing
Feel free to fork this project and contribute by submitting a pull request. I appreciate your input.

