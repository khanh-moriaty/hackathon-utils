import os
import shutil
from PIL import Image

INP_SUB_FILE = 'team007_b8tf_datacrop_5epoch.txt'
INP_SUB_PATH = '/storage/timm/'

OUT_SUB_FILE = 'team007_b8tf_datacrop_5epoch_threshold0.txt'
OUT_SUB_PATH = '/storage/submissions/'
fn, _ = os.path.splitext(OUT_SUB_FILE)

TEST_SET_DIR = '/dataset/test_set_A_full'
test_dir = os.path.dirname(TEST_SET_DIR+'/')

CROP_DIR = test_dir + '_cropped'
NONE_DIR = test_dir + '_none'
SQUARE_DIR = test_dir + '_square'

with open(os.path.join(INP_SUB_PATH, INP_SUB_FILE), 'r') as f:
    lines = f.read().splitlines()

lines = [line.strip().split() for line in lines]
lines.sort(key=lambda x: x[0])

THRESHOLD = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
}
def post_proc(lines):
    result = []
    for line in lines:
        if len(line) == 2:
            result.append(line[:2])
            continue
        fi = line[0]
        top1 = line[1]
        score1 = line[2]
        top2 = line[3]
        score2 = line[4]
        img_path = os.path.join(CROP_DIR, fi)
        if not os.path.exists(img_path):
            continue
        print(img_path)
        img = Image.open(img_path)
        width, height = img.size
        if width == height:
            continue
        if top1 == '0' and round(width/height, 4) == 1.7778:
            result.append([fi, top2, score2, top1, score1])
        elif float(score1) <= 0.5 and top2 == '0':
            result.append([fi, top2, score2, top1, score1])
        elif float(score1) <= THRESHOLD[top1]:
            result.append([fi, top2, score2, top1, score1])
        else:
            result.append([fi, top1, score1, top2, score2])
            
    return result
        
def populate_none(result):
    dir = os.listdir(NONE_DIR)
    for fi in dir:
        result.append([fi, '0', '1.0000', '0', '1.0000'])
        
def populate_square(result):
    dir = os.listdir(SQUARE_DIR)
    for fi in dir:
        result.append([fi, '0', '1.0000', '0', '1.0000'])

result = post_proc(lines)
populate_none(result)
populate_square(result)

print(result)
print(len(result))

with open(os.path.join(OUT_SUB_PATH, OUT_SUB_FILE), 'w') as f:
    for line in result:
        f.write('\t'.join(line[:2]) + '\n')

with open(os.path.join(OUT_SUB_PATH, "{}_viz.txt".format(fn)), 'w') as f:
    for line in result:
        f.write('\t'.join(line) + '\n')