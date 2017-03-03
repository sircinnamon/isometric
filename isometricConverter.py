from PIL import Image
import sys
import math
img = Image.open(sys.argv[1])
print(img.format, img.size, img.mode)
#rotate 45 deg counter-clockwise
img = img.rotate(45,expand=1)
#scale width to 173.2% (converts 90 deg angles to 120 deg)
scaled_width = int(math.floor(img.size[0] * 1.732))
img = img.resize((scaled_width, img.size[1]))
img.save("iso.png","PNG")