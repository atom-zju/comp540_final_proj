'''
this program will do the data augmentation for cifar 10 dataset
'''

import numpy as np
import skimage.io
import skimage.transform
from shutil import copyfile


def mirror(image):
    total_cols = image.shape[1]
    mirror_img = np.copy(image)
    for idx in range(total_cols/2):
        mirror_img[:,total_cols-1-idx,:] = image[:,idx,:]
        mirror_img[:,idx,:] = image[:,total_cols-1-idx,:]
    return mirror_img


def rotate(image):
    # degree range of rotation
    rotate_range = 11
    rad = np.random.choice(rotate_range, 1) - rotate_range/2
    rotate_img = skimage.transform.rotate(image, rad,resize=False)
    if(rotate_img.shape != image.shape):
        print "shape incorrect in rotate"
    return rotate_img


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


Image_Path = '/home/atom/cifar10/data/train/'
images_labels_path = '/home/atom/cifar10/mydata/'
image_labels_file_name = 'images_labels'
# augment_fraction will define the fraction being augment
augment_fraction = 0.1

# original number of image files in the image directory
train_image_num = 50000

# total number of image files in the image directory
next_image_num = 50001

# define how many data set replicates do you want to make
data_replica = 5

# open the original image labels file
with open(images_labels_path+image_labels_file_name+'.txt') as f:
    train_image_labels = f.readlines()

for rep_i in range(data_replica):
    copyfile(images_labels_path+image_labels_file_name+'.txt',
             images_labels_path+image_labels_file_name+'_rep_'+str(rep_i)+'.txt')
    # open the replicate image labels file
    rep_image_label_file = open(images_labels_path+image_labels_file_name+'_rep_'+str(rep_i)+'.txt','a')

    # do the mirror
    # int(augment_fraction*train_image_num)
    aug_idxs = np.random.choice(train_image_num, int(augment_fraction*train_image_num), replace=False)+1
    for augidx in aug_idxs:
        filename = str(augidx)+'.png'
        pair = train_image_labels[augidx-1].split(' ')
        print 'regenerating '+pair[0]+' with label '+pair[1]
        image = skimage.io.imread(Image_Path+filename)
        transformed_img = mirror(image)
        skimage.io.imsave(Image_Path+str(next_image_num)+'.png',transformed_img)
        rep_image_label_file.write(str(next_image_num)+'.png '+pair[1].split('\n')[0]+'\n')
        next_image_num += 1

    # do random crop
    # int(augment_fraction*train_image_num)
    aug_idxs = np.random.choice(train_image_num, int(augment_fraction*train_image_num), replace=False)+1
    for augidx in aug_idxs:
        filename = str(augidx)+'.png'
        pair = train_image_labels[augidx-1].split(' ')
        print 'regenerating '+pair[0]+' with label '+pair[1]
        image = skimage.io.imread(Image_Path+filename)
        transformed_img = random_crop(image)
        skimage.io.imsave(Image_Path+str(next_image_num)+'.png',transformed_img)
        rep_image_label_file.write(str(next_image_num)+'.png '+pair[1].split('\n')[0]+'\n')
        next_image_num += 1

    # do random rotate
    # int(augment_fraction*train_image_num)
    aug_idxs = np.random.choice(train_image_num, int(augment_fraction*train_image_num), replace=False)+1
    for augidx in aug_idxs:
        filename = str(augidx)+'.png'
        pair = train_image_labels[augidx-1].split(' ')
        print 'regenerating '+pair[0]+' with label '+pair[1]
        image = skimage.io.imread(Image_Path+filename)
        transformed_img = rotate(image)
        skimage.io.imsave(Image_Path+str(next_image_num)+'.png',transformed_img)
        rep_image_label_file.write(str(next_image_num)+'.png '+pair[1].split('\n')[0]+'\n')
        next_image_num += 1


# for augidx in aug_idxs:
#     filename = str(augidx)+'.png'
#     image = skimage.io.imread(Image_Path+filename)
#     # do some transform here
#     print image.shape
#
#     skimage.io.imshow(image)
#     skimage.io.show()
#
#     test_img = random_crop(image)
#     skimage.io.imshow(test_img)
#     skimage.io.show()


