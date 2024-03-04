# image_to_ascii_converter

A simple Python application that converts images into cool ASCII art.

## Features

* Converts images of various formats (e.g., JPG, PNG) into text-based ASCII art.
* Saves the generated ASCII art to a .txt file.

## Installation

**Prerequisites:**

* Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* Pillow (PIL) library: `pip install Pillow`

**Clone/Download:**

* Clone this repository: `git clone https://github.com/joohnnyvv/image_to_ascii_converter.git`
* Or download the code directly.

## Usage

1. Make sure you have an image you want to convert in the `images` directory.
   * Optionally, create subfolders within the `images` directory to organize your images. 
2. Run the script from your terminal: `python main.py`
3. Enter the image name (and optional subfolder path):
   * Example: `my_picture.jpg`
   * Example with subfolder: `my_images/my_picture.jpg`
4. Your ASCII art will be saved accordingly in `results` directory  

## Customization

* Explore the code in `main.py` to modify:
   * The string of ASCII characters used.
   * Brightness calculation formulas for different effects. 

## Contributing

Feel free to submit issues or pull requests if you'd like to suggest improvements or fixes. 
