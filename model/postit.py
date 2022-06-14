from predict import load_easter_model, decoder
import cv2
from data_loader import preprocess
import config
import numpy as np

def preprocess(original_img, augment=True):

    # apply a threshold to make it strongly black and white
    (thresh, img) = cv2.threshold(original_img, 127, 255, cv2.THRESH_BINARY)

    ##dilation- kernel dilates region to white
    #width 300, high because we want to extract the whole line, not just word
    #if we want to extract just the word, can reduce to 3,100
    kernel = np.ones((3,300), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations = 1)

    # find contours
    dilated = dilated.astype(np.uint8)
    # cv2.CHAIN_APPROX_SIMPLE only stores the four corner points
    (contours, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # find coordinates of contours so we can draw line
    # also need to sort the contour lines
    sorted_contours_lines = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])  # (x, y, w, h)

    # scaling image [0, 1]
    img = img / 255
    img = img.swapaxes(-2, -1)[..., ::-1]
    target = np.ones((config.INPUT_WIDTH, config.INPUT_HEIGHT))
    new_x = config.INPUT_WIDTH / img.shape[0]
    new_y = config.INPUT_HEIGHT / img.shape[1]
    min_xy = min(new_x, new_y)
    new_x = int(img.shape[0] * min_xy)
    new_y = int(img.shape[1] * min_xy)
    img2 = cv2.resize(img, (new_y, new_x))
    target[:new_x, :new_y] = img2
    return 1 - (target)

charlist = training_data.charList

def predict_postit(img):
    #process image
    img1 = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img = preprocess(img1, augment=False)
    img = np.expand_dims(img, 0)

    #load model
    model = load_easter_model(config.BEST_MODEL_PATH)
    output = model.predict(img)
    prediction = decoder(output, charlist)
    output = (prediction[0].strip(" ").replace("  ", " "))

    return output