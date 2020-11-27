import os

from flow_utils.post_proc import post_proc
from flow_utils.pre_proc import pre_proc
from flow_utils.predict import predict

INP_DIR = '/dataset/test_flow/test_set_A_full/'

def full_flow(INP_DIR):

    NONE_DIR, SQUARE_DIR, CROP_DIR = pre_proc(INP_DIR)

    SUB_PATH = predict(CROP_DIR, BATCH_SIZE=8, MODEL_PATH='/storage/timm/output/train/20201126-010303-tf_efficientnet_b8-672/checkpoint-4.pth.tar')

    SUB_DIR_PATH = os.path.dirname(SUB_PATH)
    SUB_FILE_PATH = os.path.basename(SUB_PATH)

    OUT_SUB_PATH, OUT_SUB_PATH_VIZ = post_proc(SUB_DIR_PATH, SUB_FILE_PATH, '/dataset/test_flow/', 'sub_test_flow.txt', INP_DIR)

    return OUT_SUB_PATH, OUT_SUB_PATH_VIZ

if __name__ == '__main__':
    print(full_flow(INP_DIR))
