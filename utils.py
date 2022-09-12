import io
import os
import cv2
import imutils
import numpy as np
from google.cloud import storage
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

storage_client = storage.Client()
BUCKET = os.getenv('BUCKET')


def get_image_from_bucket(image):
    bucket = storage_client.bucket(BUCKET)
    response_image = bucket.get_blob(image)
    response_image = np.asarray(
        bytearray(response_image.download_as_string()), dtype="uint8")
    response_image = cv2.imdecode(response_image, cv2.IMREAD_UNCHANGED)

    return response_image


def get_binary_image(image, width=800):
    origin = imutils.resize(image, width=width, inter=cv2.INTER_AREA)
    origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(origin, 235, 255, cv2.THRESH_BINARY)


def upload_image_to_bucket(image, quark_id, filename):
    bucket = storage_client.bucket(BUCKET)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    blob = bucket.blob(f'{quark_id}/{filename}')
    blob.upload_from_string(img_byte_arr, content_type="image/png")
    return
