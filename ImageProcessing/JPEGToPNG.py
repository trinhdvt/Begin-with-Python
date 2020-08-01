import sys
import os
from PIL import Image

ROOT = os.getcwd()


def check_resource(resource):
    if not os.path.exists(resource):
        print(resource)
        print("Resources folder not exist")
        sys.exit()


def mkdir(dir_name):
    try:
        os.mkdir(ROOT + dir_name)
    except OSError:
        # print(error)
        pass


def convert(resource, output):
    os.chdir(ROOT + output)
    img_path = os.listdir(ROOT + resource)
    for path in img_path:
        img = Image.open(ROOT + resource + "/" + path)
        img.save(path.replace(".jpg", ".png"), "png")


args = sys.argv
if len(args) != 3:
    print("Args are wrong")
    sys.exit()

resource_dir = args[1]
output_dir = args[2]

check_resource(resource_dir)
mkdir(output_dir)
convert(resource_dir, output_dir)
