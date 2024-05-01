#!/usr/bin/env python
import cv2
import os
import sys, getopt
import numpy as np
from edge_impulse_linux.image import ImageImpulseRunner

runner = None

## Classifying Object
def classify(n):
    m = './module/modelfile.eim'
    with ImageImpulseRunner(m) as runner:
        try:
            model_info = runner.init()
            labels = model_info['model_parameters']['labels']

            img = cv2.imread(n)
            if img is None:
                print('Failed to load image')
                exit(1)

            # imread returns images in BGR format, so we need to convert to RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # get_features_from_image also takes a crop direction arguments in case you don't have square images
            features, cropped = runner.get_features_from_image(img)

            res = runner.classify(features)

            if "classification" in res["result"].keys():
                print('Result (%d ms.) ' % (res['timing']['dsp'] + res['timing']['classification']), end='')
                for label in labels:
                    score = res['result']['classification'][label]
                    print('%s: %.2f\t' % (label, score), end='')
                print('', flush=True)

            elif "bounding_boxes" in res["result"].keys():
                a=0
                b = 0
                for bb in res["result"]["bounding_boxes"]:
                    if (bb['label']) == "Tomato":
                        a = a+1       ## Counting Tomato
                    if (bb['label']) == "Banana":
                        b = b+1       ## Couting Banana 
                    cropped = cv2.rectangle(cropped, (bb['x'], bb['y']), (bb['x'] + bb['width'], bb['y'] + bb['height']), (255, 0, 0), 1)
            # the image will be resized and cropped, save a copy of the picture here
            # so you can see what's being passed into the classifier
            cv2.imwrite('./image/debug.jpg', cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
            c={"Tomato":a,"Banana":b}
            return c
        except:
            return "something wents wrong !!"
        finally:
            if (runner):
                runner.stop()

if __name__ == "__main__":
   main(sys.argv[1:])
