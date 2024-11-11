import re
import cv2
import keras_ocr
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import tensorflow as tf

# Enable XLA (Accelerated Linear Algebra)
tf.config.optimizer.set_jit(True)

# Initialize the keras-ocr pipeline with scale set to 1
pipeline = keras_ocr.pipeline.Pipeline(scale=1)

# Image paths and settings
image_paths = [
    "fisheye.jpg",
   
]
desired_width = 1700  # Adjust as needed
roi_left = 0
roi_right = desired_width
roi_top = 0
roi_bottom = 0

three_char_pattern = re.compile(r'[a-zA-Z0-9]{3}')

def preprocess_image(image_path):
    start_time = time.time()
    img = cv2.imread(image_path)
    roi_image = img[roi_top:img.shape[0] - roi_bottom, roi_left:roi_right]
    stretched_image = cv2.resize(roi_image, (desired_width, roi_image.shape[0]))
    stretched_image_rgb = cv2.cvtColor(stretched_image, cv2.COLOR_BGR2RGB)
    end_time = time.time()
    print(f"Preprocessing time: {(end_time - start_time) * 1000:.2f} ms")
    return stretched_image_rgb

def process_images(image_paths):
    with ThreadPoolExecutor() as executor:
        processed_images = list(executor.map(preprocess_image, image_paths))
    return processed_images

def perform_ocr(images):
    start_time = time.time()
    predictions = pipeline.recognize(images)
    end_time = time.time()
    print(f"OCR Processing time: {(end_time - start_time) * 1000:.2f} ms")
    return predictions

def display_results(images, predictions):
    for image, prediction in zip(images, predictions):
        exp = []
        tw = []
        three_char_combinations = [text for text, confidence in prediction if three_char_pattern.match(text)]
        for combo in three_char_combinations:
            if combo[0].isalpha():
                exp.append(combo)

            
            elif combo[0].isdigit():
                tw.append(combo)
        if len(combo)>2:
            exp.append(combo[2])
        keras_ocr.tools.drawAnnotations(image=image, predictions=[(text, confidence) for text, confidence in prediction if text in three_char_combinations])
        print("Three char combinations: ", tw, exp)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

def main():
    images = process_images(image_paths)
    predictions = perform_ocr(images)
    display_results(images, predictions)

main()