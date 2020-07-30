import os

from utils import create_input_files

IMG_DIR = '/userhome/34/h3509807/MadeWithML/data/Instagram/images'
JSON_PATH = './data/ig_json/full_clean.json'
OUT_DIR = './data/meta_wostyle/data_full_clean'

os.makedirs(OUT_DIR, exist_ok = True)

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset = 'flickr8k',
                       karpathy_json_path = JSON_PATH,
                       image_folder = IMG_DIR,
                       captions_per_image = 1,
                       min_word_freq = 5,
                       output_folder = OUT_DIR,
                       max_len = 50)