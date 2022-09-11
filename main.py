from fastapi import FastAPI, Request, HTTPException
from models import Item
import cv2
import imutils
from PIL import Image

app = FastAPI()
BUCKET = "ai-coloring-similarity"


@app.post('/coloring-similarity')
def coloring_similarity(request: Request, item: Item):

    return
    # # Get image reference
    # origin = cv2.imread(args.origin)
    # origin = imutils.resize(origin, width=800, inter=cv2.INTER_AREA)
    # origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
    # (thresh, origin) = cv2.threshold(origin, 235, 255, cv2.THRESH_BINARY)

    # # Get image to validate
    # dest = cv2.imread(args.destination)
    # dest = imutils.resize(dest, width=800, inter=cv2.INTER_AREA)
    # dest = cv2.cvtColor(dest, cv2.COLOR_BGR2GRAY)
    # (thresh, dest) = cv2.threshold(dest, 235, 255, cv2.THRESH_BINARY)

    # source = cv2.imread(args.destination)
    # source = cv2.cvtColor(source, cv2.COLOR_BGR2BGRA)
    # source = imutils.resize(source, width=800, inter=cv2.INTER_AREA)

    # h = origin.shape[0]
    # w = origin.shape[1]
    # counter = 0
    # similarity = 0
    # residual = 0
    # # loop over the image, pixel by pixel
    # for y in range(0, h):
    #     for x in range(0, w):
    #         # Validate if a pixel is white or black
    #         if origin[y, x] == 0:
    #             counter += 1

    #             if origin[y, x] == dest[y, x]:
    #                 similarity += 1

    #         elif origin[y, x] == 255:
    #             if dest[y, x] == 0:
    #                 residual += 1

    # print("Counter: ", counter)
    # print("Similarity: ", similarity)
    # print("Similarity %: ", (similarity * 100) / counter)
    # print("Residual: ", residual)
    # print("Residual %: ", ((residual * 100) / ((h * w) - counter)))
    # print("Total: ", h * w)

    # mask = origin - dest

    # alpha = cv2.merge((mask.copy(), mask.copy(), mask.copy(), mask.copy()))
    # alpha[mask == 255] = (0, 0, 255, 255)

    # cv2.imwrite("alpha.png", alpha)

    # # Concatenate
    # # result = cv2.addWeighted(alpha, 1, source, 0.5, 0)
    # # result = np.dstack([source, alpha])
    # im1 = Image.fromarray(cv2.cvtColor(source, cv2.COLOR_BGRA2RGBA))
    # im2 = Image.fromarray(cv2.cvtColor(alpha, cv2.COLOR_BGRA2RGBA))

    # # result = Image.blend(im1, im2, 0.5)
    # im1.paste(im2, (0, 0), mask=im2)
    # im1.save("result.png", "PNG")

    # im1.show()

    # # cv2.imshow("Origin", source)
    # # cv2.imshow("Alpha", alpha)
    # # cv2.imshow("Result", np.asarray(im1))
    # # cv2.waitKey(0)
