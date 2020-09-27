from PIL import Image
import os

for f in os.listdir('pictures'):
		with Image.open(f'pictures/{f}') as im:
			im2 = im.resize((600, 600))
			im2.save(f'hpictures/{f}.png')
