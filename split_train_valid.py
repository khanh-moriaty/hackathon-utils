import shutil, os, random

TRAIN_DIR = '/dataset/final_classification_ver3/train'
VALID_DIR = '/dataset/final_classification_ver3/validation'

CLASSES = [str(x) for x in range(8)]
EXT = ['.jpg', '.jpeg', '.png', '.bmp']

for name in CLASSES:
    INP_DIR = os.path.join(TRAIN_DIR, name)
    OUT_DIR = os.path.join(VALID_DIR, name)
    dir = os.listdir(INP_DIR)
    dir = [fi for fi in dir if os.path.splitext(fi)[-1].lower() in EXT]
    test = random.sample(dir, int(len(dir) * 0.3))

    for fi in test:
        print(os.path.join(OUT_DIR, fi))
        fn, _ = os.path.splitext(fi)
        shutil.move(os.path.join(INP_DIR, fi), os.path.join(OUT_DIR, fi))
