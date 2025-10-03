# Background Removal with Python
A simple Python project to remove the background from images using the rembg library, along with NumPy and Pillow.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Working](#project-working)
- [Installation](#installation)
- [Future Enhancements](#future-enhancements)
- [License](#license)


## Features

- Removes background from any image with a single function
- Lightweight and easy to use
- Supports multiple image formats (JPG, PNG, etc.)
- Can be extended for batch image processing  

## Tech Stack

- Python 3.9+
- [rembg](https://github.com/danielgatis/rembg)
- [NumPy](https://github.com/numpy/numpy)
- [Pillow (PIL)](https://github.com/python-pillow/Pillow)

## Project Working
Project Working

The project works by using the rembg library, which is built on deep learning models trained to separate foreground objects from the background in an image.

- You provide an input image (JPEG/PNG).
- The model detects the main subject (person/object).
- The background is automatically removed, leaving only the subject.
- The output is saved as a transparent PNG image.

## Installation

 1. Clone the repository: git clone https://github.com/Bharath8071/bg-remove-python-prj.git
 2. Navigate to the project directory: `cd bg-remove-python-prj`


## Future Enhancements

- Add batch background removal for folders of images
- Build a simple GUI/web app for drag-and-drop image processing
- Support video background removal

## License

This project is licensed under the MIT License. See the LICENSE file for details.
