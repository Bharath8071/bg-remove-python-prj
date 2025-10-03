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
- NumPy
- Pillow (PIL)

## Project Working

This project detects objects **based on their color** using your webcam in real-time.  

1. **Set Color**  
   - Open the `set_colour` module and define the target color by updating the color code (RGB/HSV).  

2. **Live Camera Input**  
   - The program uses your webcam to capture video frames continuously.  

3. **Color Detection**  
   - Each frame is analyzed to find pixels matching the target color.  
   - A mask is applied to isolate the colored regions.  

4. **Object Highlighting**  
   - Detected objects are outlined with bounding boxes or highlighted in the frame.  

5. **Real-Time Output**  
   - The processed video is displayed live with the detected colored objects.  
   - You can change the target color anytime by updating the `getcolour` module.


## Installation

 1. Clone the repository: git clone https://github.com/Bharath8071/Colour_Detector_Prj.git
 2. Navigate to the project directory: `cd Colour_Detector_Prj`


## Future Enhancements

-Expand color dataset (more shades, custom colors)
-Build a GUI or web interface
-Support clustering for dominant color detection

## License

This project is licensed under the MIT License. See the LICENSE file for details.
