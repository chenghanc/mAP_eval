from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import argparse
import numpy as np
import matplotlib.pyplot as plt

def coco_eval(args):
    cocoGt = COCO(args.gt_json)
    cocoDt = cocoGt.loadRes(args.pred_json)
    cocoEval = COCOeval(cocoGt, cocoDt, args.eval_type)
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()

    # pr-curve

    all_precision = cocoEval.eval['precision'][0, :, :, 0, 2]
    all_recall = cocoEval.params.recThrs

    names=['B', 'Y', 'W', 'R', 'AH', 'BH']

    x = np.arange(0, 1.01, 0.01)
    if 0 < len(names) < 98:
        for i, y in enumerate(all_precision.T):
            plt.plot(x, y, linewidth=1, label=f'{names[i]} {all_precision[:,i].mean():.3f}')  # plot(recall, precision)
    else:
        plt.plot(x, all_precision, linewidth=1, color='grey')                                 # plot(recall, precision)

    plt.plot(x, all_precision.mean(1), linewidth=3, color='blue', label='all classes %.3f mAP@0.50' % all_precision.mean())
    plt.title('PR Curve: mAP@0.50 =  %.3f' % all_precision.mean())
    plt.ylabel("Precision")
    plt.xlabel("Recall")
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper right")
    plt.savefig('prcurve.jpg',dpi=250)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate segm/bbox/keypoints in COCO format.')
    parser.add_argument('gt_json', type=str, help="COCO format segmentation/detection/keypoints ground truth json file")
    parser.add_argument('pred_json', type=str, help="COCO format segmentation/detection/keypoints prediction json file")
    parser.add_argument('eval_type', type=str, choices=['segm', 'bbox', 'keypoints'], help="Evaluation type")
    args = parser.parse_args()
    coco_eval(args)
