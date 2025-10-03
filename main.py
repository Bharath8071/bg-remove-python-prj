import rembg
import numpy as np
from PIL import Image

# Load image
image = np.array(Image.open(r'E:\programming\data\fr_photo.jpg'))

# Remove background
output = rembg.remove(image)

# Save output
Image.fromarray(output).save('E:\programming\data\output1.png')
