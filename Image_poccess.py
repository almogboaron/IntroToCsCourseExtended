from PIL import Image #need to install PIL/PILLOW
import random
import math
import cmath   # complex numbers



###########################################################
# basics
###########################################################

# Open image
img = Image.open("./guess.bmp")

# Turn the image to 256 grey level (0-255)
img = img.convert('L')

# Get image properties
##print(img.size)
##print(img.mode)
##print(img.histogram())

# Display
##img.show()

# Crop
##region = img.crop((200,400,220,450))
##region.show()
##w, h = img.size
##region2 = img.crop((10,10,h-10, w-10))
##region2.show()


# Rotate
##rot = img.rotate(45)
##rot.show()


#save
#img.save("./name.bmp", "bmp") #name, format


# Load image data into matrix for pixel-wize manipulation
##mat = img.load()
##for x in range(20):
##    for y in range(20):
##        mat[x,y] = 255
##img.show()

###########################################################
# synthetic images
###########################################################

def create_img(w, h, op):
    ''' create a wXh image
        assign pixel x,y with op(x,y) '''
    img = Image.new(mode='L', size=(w,h), color=255)
    mat = img.load()

    for x in range(w):
        for y in range(h):
            mat[x,y] = op(x,y)

    return img

WHITE = 255
BLACK = 0

##rnd_img = create_img(256, 256, lambda x,y: random.randint(0,255))
###rnd_img.show()
##
##ver_lines = create_img(100, 300, lambda x,y: BLACK if x%10==0 else WHITE)
##ver_lines.show()
##
##n=512
##
##diagonal = create_img(n, n, lambda x,y: BLACK if x-y==0 else WHITE)
###diagonal.show()
##
##framed_diagonal = create_img(n, n, lambda x,y: BLACK if x==0 or y==0 or x==n-1 or y==n-1 or x==y or x+y==n-1 else WHITE)
###framed_diagonal.show()
##
##what = create_img(n, n, lambda x,y,c=1: (c*(x-y))%256)
##what.show()
##
##circles = create_img(n, n, lambda x,y,c=1: (c*(x**2 + y**2)) % 256)
##circles.show()
##
##product = create_img(n, n, lambda x,y,c=1: (c*x*y) % 256)
##product.show()
##
##surprise = create_img(n, n, lambda x,y: (int(100*math.sin(32*cmath.phase(complex(x,y)))))%256)
##surprise.show()
##
##surprise2 = create_img(n, n, lambda x,y: (int(100*math.sin(32*cmath.phase(complex(x-256,y-256)))))%256)
##surprise2.show()


###########################################################
# manipulating images
###########################################################

def process_img(img, op):
    ''' process image img (PIL.Image object)
        assign pixel x,y with some operator op
        op operats on the matrix representing the original image
        and the current location x,y '''

    w,h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    for x in range(w):
        for y in range(h):
            new_mat[x,y] = op(mat, x, y)

    return new_img

img = Image.open("./guess.bmp").convert('L')


##
##white_square = process_img(img, lambda mat, x, y: WHITE if x<100 and y<100 else mat[x,y])
##white_square.show()
##
##color_shifted = process_img(img, lambda mat, x, y, k=30: mat[x,y]+k)
##color_shifted.show()
##
##negative = process_img(img, lambda mat, x, y: 256-mat[x,y])
##negative.show()
##
##w,h = img.size
##upside_down = process_img(img, lambda mat, x, y: mat[x,h-y-1])
##upside_down.show()
##




###########################################################
## Useful utility - tiling images
###########################################################

def tile(*images):
    ''' Join several images horizontally for easy display.
        Assume all images are of the same size
        The * means a variable number of parameters '''
    w,h = images[0].size
    n = len(images) #number of images
    new = Image.new('L',(w*n+n,h), 'white') #+n for some space between images

    for i in range(len(images)):
        new.paste(images[i], (w*i+i,0)) #+i for some space between images

    return new

