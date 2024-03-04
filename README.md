# image_to_ascii_converter

A simple Python application that converts images into cool ASCII art.

## Features

* Converts images of various formats (e.g., JPG, PNG) into text-based ASCII art.
* Saves the generated ASCII art to a .txt file.

## Installation

** Prerequisites:**

* Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* Pillow (PIL) library: `pip install Pillow`

** Clone/Download:**

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

## Examples

![mona](https://github.com/joohnnyvv/image_to_ascii_converter/assets/110868938/973f2de1-7045-427e-9d32-5e0d22e7a306) 
<img width="386" alt="Screenshot 2024-03-04 at 01 57 04" src="https://github.com/joohnnyvv/image_to_ascii_converter/assets/110868938/0ebbc707-69d2-4f9f-8839-a35a41d80dbf">
![cute_kitty](https://github.com/joohnnyvv/image_to_ascii_converter/assets/110868938/66ebe3c2-ef65-44fd-8da1-6e7264a6be13)
<img width="386" alt="Screenshot 2024-03-04 at 01 58 46" src="https://github.com/joohnnyvv/image_to_ascii_converter/assets/110868938/36eabf78-3d00-42a0-a90d-353cb652b858">

## Contributing

Feel free to submit issues or pull requests if you'd like to suggest improvements or fixes. 
