'''
this program will do the data augmentation for cifar 10 dataset
'''

import numpy as np
import skimage.io
import skimage.transform


def mirror(image):
    total_cols = image.shape[1]
    mirror_img = np.copy(image)
    for idx in range(total_cols/2):
        mirror_img[:,total_cols-1-idx,:] = image[:,idx,:]
        mirror_img[:,idx,:] = image[:,total_cols-1-idx,:]
    return mirror_img

def rotate(image,rad):
    return skimage.transform.rotate(image, rad,resize=True)

def random_crop(image):
    # cropped size will have at least 80% of the original image
    margin_size = np.random.choice(int(image.shape[0] * 0.25), 1)
    cropped_size = image.shape[0]-margin_size
    vpos = np.random.choice(margin_size, 1)
    hpos = np.random.choice(margin_size, 1)
    cropped_img = np.copy(image[vpos:vpos+cropped_size,hpos:hpos+cropped_size,:])
    return skimage.transform.resize(cropped_img,image.shape)

def color_jitter(image):
    pass


Image_Path = '/Users/atom/Documents/Course/Comp 540/FinalProject/cifar10_data/train/'
images_labels_txt = '/home/atom/cifar10/mydata/images_labels.txt'

# augment_fraction will define the fraction being augment
augment_fraction = 0.1

# total number of image files in the image directory
train_image_num = 50000

aug_idxs = np.random.choice(train_image_num, 1, replace=False)

for augidx in aug_idxs:
    filename = str(augidx)+'.png'
    image = skimage.io.imread(Image_Path+filename)
    # do some transform here
    print image.shape

    skimage.io.imshow(image)
    skimage.io.show()

    test_img = random_crop(image)
    skimage.io.imshow(test_img)
    skimage.io.show()


