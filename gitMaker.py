import sys 

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "output.gif", save_all=True, append_images=[images[1]], duration = 200, loop=0
)


#To run this program add the pictures you want to animate in the terminal
#EXAMPLE; python3 gifMaker.py picture1.png picture2.png

