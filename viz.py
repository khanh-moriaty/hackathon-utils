import os, shutil
import cv2
from PIL import Image

INP_DIR = '/dataset/test_set_A_full/'
OUT_DIR = '/dataset/viz/'
SUBMISSION_NAME = 'team007_b8tf_datacrop_BEST_postproc_final_viz.txt'
MAX_SIZE = 200

SUBMISSION_PATH = '/storage/submissions/'
submission_path = os.path.join(SUBMISSION_PATH, SUBMISSION_NAME)
lines = open(submission_path, 'r').read().splitlines()
lines.sort()

SPECIAL_SIZE = [
    (1000, 677),
    (1024, 683),
    (960, 720),
    (1080, 720),
    (1000, 750),
    (1912, 1080),
    (512, 288),
    (426, 240),
    (500, 300),
    (459, 306),
    (500, 313),
    (640, 360),
    (660, 371),
    (600, 400),
    (660, 410),
    (640, 427),
    (660, 440),
    (665, 449),
    (500, 450),
    (800, 450),
    (656, 480),
    (653, 490),
    (660, 495),
]

submission_name, _ = os.path.splitext(SUBMISSION_NAME)
OUT_DIR = os.path.join(OUT_DIR, submission_name)
CLASSES = [str(x) for x in range(8)]
for name in CLASSES:
    out_path = os.path.join(OUT_DIR, name)
    os.makedirs(out_path, exist_ok=True)
    shutil.rmtree(out_path)
    os.makedirs(out_path, exist_ok=True)

all_img = os.listdir(INP_DIR)
pred_img = []

# fo = open(os.path.join(SUBMISSION_PATH, submission_name + '_viz.txt'), 'w')

viz_count = 0

for line in lines[:]:
    line = line.split()
    print(line)
    out_name = line[0]
    name = line[1]
    
    pred_img.append(out_name)
    inp_path = os.path.join(INP_DIR, out_name)
        
    # img = Image.open(inp_path)
    # width, height = img.size
    # if width == height: 
    #     name = '0'
    #     print('1:1', inp_path)
    # if abs(width/height - 16/9) < 0.0001 and name == '0': 
    #     name = '2'
    #     print('16:9', inp_path)
    
    
    img = cv2.imread(inp_path)
    if img is None: continue
    height, width = img.shape[:2]
    if width == height: continue
        
    special = 'SPECIAL' if (width, height) in SPECIAL_SIZE else 'XXXXXXX'
        
    if len(line) > 4:
        score = float(line[2])
        fn, ext = os.path.splitext(out_name)
        out_path = os.path.join(OUT_DIR, name, "{}_{:.4f}_{}_{:.4f}_{}{}".format(special, score, line[3], float(line[4]), fn, ext))
    elif len(line) > 2:
        score = float(line[2])
        fn, ext = os.path.splitext(out_name)
        out_path = os.path.join(OUT_DIR, name, "{}_{:.4f}_{}{}".format(special, score, fn, ext))
    else:
        out_path = os.path.join(OUT_DIR, name, out_name)
    
    # fo.write("{}\t{}\n".format(out_name, name))
    img = cv2.resize(img, (width * MAX_SIZE // height, MAX_SIZE))
    cv2.imwrite(out_path, img)
    
    # shutil.copyfile(inp_path, out_path)

pred_img = list(set(all_img) - set(pred_img))
pred_img.sort()
print('no class:', len(pred_img))
for fi in pred_img:
    inp_path = os.path.join(INP_DIR, fi)
    out_path = os.path.join(OUT_DIR, '0', fi)
        
    # fo.write("{}\t{}\n".format(fi, 0))
    
    img = cv2.imread(inp_path)
    height, width = img.shape[:2]
    img = cv2.resize(img, (width * MAX_SIZE // height, MAX_SIZE))
    cv2.imwrite(out_path, img)
    
    # shutil.copyfile(inp_path, out_path)

# fo.close()
