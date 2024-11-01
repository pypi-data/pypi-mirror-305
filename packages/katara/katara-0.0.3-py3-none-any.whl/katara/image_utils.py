import glob
import os
import time
from PIL import Image as pillow
from functools import wraps
import cv2
import numpy as np
from skimage import io
from transformers import AutoModelForCausalLM, AutoTokenizer


def read_image(img, img_size):
    img = np.array(img)
    img = cv2.resize(img, (img_size, img_size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0

    return img


def latency(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} latency => {end_time - start_time:.4f}s")
        return result

    return wrapper


def image_loader(img):
    if isinstance(np.ndarray, img):
        return pillow.fromarray(img)

    elif isinstance(str, img):
        return pillow.open(img)

    elif isinstance(pillow, img):
        return img

    elif isinstance(str, img):
        img = io.imread(img)
        img = pillow.fromarray(img)

        return img


def get_all_images(root_dir, extensions=("*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp")):
    image_files = []
    for ext in extensions:
        for directory, _, _ in os.walk(root_dir):
            image_files.extend(glob.glob(os.path.join(directory, ext)))
    print(f"found {len(image_files)} images in {root_dir}")
    return image_files

def load_moondream_models():
    moondream_model = AutoModelForCausalLM.from_pretrained(
        "vikhyatk/moondream2", trust_remote_code=True
    )

    md_tokenizer = AutoTokenizer.from_pretrained(
        "vikhyatk/moondream2", trust_remote_code=True
    )
    
    return moondream_model, md_tokenizer


def caption_image_moondream(
    image: pillow,
) -> str:

    model, tokenizer = load_moondream_models()
    
    enc_image = model.encode_image(
        image
    )  # encode image with vision encoder(moondream uses SigLip)

    img_caption = model.answer_question(
        enc_image, "Describe this image and it's style", tokenizer
    )  # generate caption

    return img_caption
