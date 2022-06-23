import numpy as np
import os
import re
import cv2


def load_tifdata(dir, classes=2, label=True, width=1024, height=1024):
    """ Load image data from folder \n
    parameters \n
        dir -> folder from which will be loaded images \n
        classes  -> number of classes which we want to load \n
        label -> True if a separate label field should be returned (the result command will also contain labels regardless of this option) \n
        width, height -> width, height of loaded images \n
    return \n
        images -> dir containing image (img), h (height), w (width), name of file, name of metadata (metadata), label for image (Y) \n
    """
    images = []
    labels = []
    Y = -1
    for image_name in os.listdir(dir):
        # Open only images
        if '.tif' in image_name.lower():
            image = cv2.imread(os.path.join(dir, image_name), cv2.IMREAD_GRAYSCALE)
            try:
                # Find a name for metadata
                metadata_name = "".join(image_name.split('.')[0]) + '-TIF.hdr'
                with open(os.path.join(dir, metadata_name), 'r') as file:
                    tag = re.findall(r"tag = (.*)", file.read())

                # Extract label from metadata
                if 'Via' in tag:
                    Y = 0
                elif 'Metal' in tag:
                    Y = 1
                elif 'Other' in tag:
                    Y = 2
            except Exception as e:
                print("Error when reading metadata", e)

            # Create dict
            image = image[0:height, 0:width]
            data = {
                'img': image,
                'h': image.shape[0],
                'w': image.shape[1],
                'name': image_name,
                'metadata': metadata_name,
                'Y': Y
            }

            if Y < classes:
                images.append(data)
                labels.append(Y)

    print(f"Loaded ({len(images)}) images from {dir}")
    if label:
        return images, labels
    return images


def crop_image(image, height, width):
    """ Cut image into small part with height and width"""
    result_images = []
    h = int(np.floor(image.shape[0] / height))
    w = int(np.floor(image.shape[1] / width))
    for x in range(0, h):
        for y in range(0, w):
            result_images.append(
                image[x*height: (x*height) + height, y*width: (y*width) + width])
    return result_images

def classification_var(image, border=100, classification_region=32, verbose=True):
    """
    Classification for thresholding and clustering \n
    parameters \n
        image -> image for classification \n
        border -> border for the difference of variation \n
        classification_region -> size of image to cut \n
    return \n
        classification 1 or 0
    """
    variance = []
    cutted_image = crop_image(
        image, classification_region, classification_region)

    for img in cutted_image:
        # Sum X, Y
        column_sum = np.sum(img, axis=0)
        row_sum = np.sum(img, axis=1)

        # Compute variance for X, Y
        var_column = np.var(column_sum)
        var_row = np.var(row_sum)

        # Difference of variance
        variance.append(var_column - var_row)
    if verbose:
        print(
            f"Max diff var={np.max(np.abs(variance))}, without abs={variance[np.argmax(np.abs(variance))]}, cls-> {1 if np.max(np.abs(variance)) > border else 0}")
    if np.max(np.abs(variance)) > border:
        return 1
    else:
        return 0
