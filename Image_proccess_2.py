from PIL import Image  # need to install PIL/PILLOW
import random
from images_with_PIL import tile, process_img

##################
# color constants
##################
WHITE = 255
BLACK = 0

img = Image.open("./guess.bmp").convert('L')


####################
## Noise formation
####################

def add_gaussian_noise(img, sigma=10):
    ''' Generates Gaussian noise with mean 0 and SD sigma.
        Adds indep. noise to pixel, keeping values in 0..255 '''

    def g_noise_op(mat, x, y):
        g_noise = round(random.gauss(0, sigma))  # get gauusian noise with mean=0 and SD=sigma
        return min(max(mat[x, y] + g_noise, 0), 255)

    return process_img(img, g_noise_op)


def add_SP_noise(img, p=0.01):
    ''' Generates salt and pepper noise: Each pixel is "hit" independently
        with probability = p.
        If hit, it has 50:50 chance of becoming white or black '''

    def sp_noise_op(mat, x, y):
        sp_noise = BLACK if random.random() < 0.5 else WHITE  # 50:50
        r = random.random()
        if r < p:  # noise occurs with prob. p
            return sp_noise
        else:
            return mat[x, y]

    return process_img(img, sp_noise_op)


####################
## Denoising
####################

def local_op(img, op, kx=1, ky=1):
    ''' For every pixel x,y of img
        apply operator op on list containing pixels
        in a rectangular neighborhood x-kx...x+kx, y-ky...y+ky '''
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    for x in range(w):
        for y in range(h):
            # get 4 corners, do not exceed image boundaries
            left = max(x - kx, 0)
            up = max(y - ky, 0)
            right = min(x + kx, w - 1)
            down = min(y + ky, h - 1)

            # flatten 2D neighborhood into 1D list
            neighbors_list = [mat[xx, yy] for xx in range(left, right + 1) for yy in range(up, down + 1)]
            # apply op in list and assign result to pixel x,y
            new_mat[x, y] = op(neighbors_list)

    return new_img


def local_means(img, kx=1, ky=1):
    mean = lambda lst: round(sum(lst) / len(lst))  # average (mean) of lst
    return local_op(img, mean, kx, ky)


def local_medians(img, kx=1, ky=1):
    median = lambda lst: sorted(lst)[len(lst) // 2]  # median of lst
    return local_op(img, median, kx, ky)


####################
## Runs
####################

"""
img = Image.open("./guess.bmp").convert('L') #Eifer tower
dirty_gauss = add_gaussian_noise(img, 5)
dirty_SP = add_SP_noise(img, 0.05)

# Display noisy images
#tile(img, dirty_gauss, dirty_SP).show()

fix_gauss_by_means = local_means(dirty_gauss, 2, 2)
fix_gauss_by_medians = local_medians(dirty_gauss, 1, 1)

# Display denoising gaussian noise
tile(img, dirty_gauss, fix_gauss_by_means, fix_gauss_by_medians).show()


fix_SP_by_means = local_means(dirty_SP, 1, 1)
fix_SP_by_medians = local_medians(dirty_SP, 1, 1)

# Display denoising SP noise
tile(img, dirty_SP, fix_SP_by_means, fix_SP_by_medians).show()
"""

"""
#code for matrix illustration of local denoising methods
im = Image.new('L', (4,4),'black')
im = im.convert('L')

mat = im.load()
mat[0,0] = 9
mat[0,3] = 200
mat[2,2] = 5

print("current image:")
for i in range(4):
    for j in range(4):
        print(mat[i,j], end=",")
    print("")

print("")

print("Local means:")
im2 = local_means(im)
mat2 = im2.load()
for i in range(4):
    for j in range(4):
        print(mat2[i,j], end=", ")
    print("")

print("")

print("Local medians:")	
im3 = local_medians(im)
mat3 = im3.load()
for i in range(4):
    for j in range(4):
        print(mat2[i,j], end=", ")
    print("")
"""

### Example for cleaning a small 4x4 rectange
"""
im = Image.open("./guess.bmp") #Eifer tower
im = im.convert('L')
mat = im.load()

for i in range(100, 104):
  for j in range(100, 104):
    mat[i,j] = 255

im1 = local_medians(im,1,1)
im2 = local_medians(im,2,2)
im3 = local_medians(im,3,3)

tile(im, im1, im2, im3).show()

im1 = local_medians(im,1,1)
im2 = local_medians(im1,1,1)

tile(im, im1, im2).show()

im1 = local_medians(im,1,1)
im2 = local_medians(im1,2,2)

tile(im, im1, im2).show()
"""

### Example for cleaning a narrow strip
"""
im = Image.open("./guess.bmp") #Eifer tower
im = im.convert('L')
mat = im.load()

for i in range(100, 120):
    mat[i,100] = 255

im1 = local_medians(im,0,1)
tile(im, im1).show()
"""

