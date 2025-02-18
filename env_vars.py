import os
images = os.getenv('IMAGES')
excels = os.getenv('EXCELS')
output = os.getenv('OUTPUT')

for dir in [images, excels, output]:
    if not os.path.exists(dir):
        os.makedirs(dir)
