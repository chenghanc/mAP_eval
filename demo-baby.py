import pycocotools
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

import pred_yolo2json
import gt_yolo2json

# yolo2coco
# run the command
# ./darknet detector test baby.data baby.cfg baby_final.weights -thresh 0.001 -dont_show -ext_output < test.txt > result.txt
# grep -vE "(Detection|Enter)" result.txt > result2.txt

input_txt = 'data/result2.txt'

output_json = 'darknet_pred_baby.json'
class_file = 'data/baby.names'

pred_yolo2json.write_json(input_txt, output_json, class_file)

# gt

valid_target_txt = "data/test.txt"
name_path = 'data/baby.names'

def load_class_names(path):
    with open(path) as f:
        return [line.rstrip("\n") for line in f.readlines()]

class_names = load_class_names(name_path)

valid_gt_json = 'darknet_valid_gt_baby.json'
gt_yolo2json.generate_annotations_file(valid_target_txt, class_names, valid_gt_json)
