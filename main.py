import os
import cv2
import imutils
import numpy as np
from PIL import Image
from fastapi import FastAPI, Request, HTTPException
from models import Item
from dotenv import load_dotenv
from utils import get_image_from_bucket, get_binary_image, upload_image_to_bucket

load_dotenv()

BUCKET = os.getenv('BUCKET')
app = FastAPI()


@app.post('/coloring-similarity')
def coloring_similarity(request: Request, item: Item):
    # Initialize some counters to get image stats
    reference = 0
    similarity = 0
    residual = 0

    # Get images from bucket as openCV image
    reference_image = get_image_from_bucket(item.expected_image)
    student_image = get_image_from_bucket(item.student_response)

    # Get the right width for both images
    width = reference_image.shape[1]
    if width > student_image.shape[1]:
        width = student_image.shape[1]

    # Get image reference
    (thresh, origin) = get_binary_image(reference_image, width)

    # Get image to validate
    (thresh, dest) = get_binary_image(student_image, width)

    # Get image dimensions
    h = origin.shape[0]
    w = origin.shape[1]

    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # Validate if a pixel is white or black in the reference image
            if origin[y, x] == 0:
                reference += 1

                # Validate if a pixel is colored in both images
                if origin[y, x] == dest[y, x]:
                    similarity += 1

            # Validate if the student image is colored outside the borders
            elif origin[y, x] == 255:
                if dest[y, x] == 0:
                    residual += 1

    # Create a red mask with transparency only with the outside coloring
    mask = origin - dest
    alpha = cv2.merge((mask.copy(), mask.copy(), mask.copy(), mask.copy()))
    alpha[mask == 255] = (0, 0, 255, 255)

    # Get blended image
    source = cv2.cvtColor(student_image, cv2.COLOR_BGR2BGRA)
    source = imutils.resize(source, width=width, inter=cv2.INTER_AREA)
    source = Image.fromarray(cv2.cvtColor(source, cv2.COLOR_BGRA2RGBA))

    alpha = Image.fromarray(cv2.cvtColor(alpha, cv2.COLOR_BGRA2RGBA))

    # Upload images to Bucket
    upload_image_to_bucket(source, item.quark_id, 'original.png')
    upload_image_to_bucket(alpha, item.quark_id, 'alpha.png')

    source.paste(alpha, (0, 0), mask=alpha)
    upload_image_to_bucket(source, item.quark_id, 'blended.png')

    response = {
        "similarity":  ((similarity * 100) / reference),
        "outside":  ((residual * 100) / ((h * w) - reference)),
        "original_image": f'{item.quark_id}/original.png',
        "alpha_image": f'{item.quark_id}/alpha.png',
        "blended_image": f'{item.quark_id}/blended.png'
    }

    return response
