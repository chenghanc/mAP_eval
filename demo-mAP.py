from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import matplotlib.pyplot as plt

annType = 'bbox'

anno_file = 'darknet_valid_gt_baby.json'
results_json = 'darknet_pred_baby.json'

cocoGt=COCO(anno_file)
cocoDt=cocoGt.loadRes(results_json)

imgIds=sorted(cocoDt.getImgIds())
len(imgIds)

# running evaluation
cocoEval = COCOeval(cocoGt,cocoDt,annType)
#cocoEval.params.catIds = [5]                # COCO API evaluation for subset of classes
cocoEval.params.imgIds = imgIds
#cocoEval.params.areaRng = [[0 ** 2, 1e5 ** 2], [0 ** 2,155 ** 2], [155** 2,185 ** 2], [185** 2, 1e5 ** 2]] # reset object area for AffectNet
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

#print(cocoEval.stats)

# pr curve
#  iouThrs    - [.5:.05:.95] T=10 IoU thresholds for evaluation
#  recThrs    - [0:.01:1] R=101 recall thresholds for evaluation
#  catIds     - [all] K cat ids to use for evaluation
#  areaRng    - [...] A=4 object area ranges for evaluation
#  maxDets    - [1 10 100] M=3 thresholds on max detections per image

#  counts     - [T,R,K,A,M] parameter dimensions
#  precision  - [TxRxKxAxM] precision for every evaluation setting
#  recall     - [TxKxAxM] max recall for every evaluation setting

cocoEval.eval['counts']
cocoEval.eval['params']
cocoEval.eval['date']
cocoEval.params.iouThrs

all_precision = cocoEval.eval['precision'][0, :, :, 0, 2] # data for IoU@0.50
#all_precision = cocoEval.eval['precision'][5, :, :, 0, 2] # data for IoU@0.75
len(all_precision)
#all_precision
all_recall = cocoEval.params.recThrs
len(all_recall)
#all_recall
cocoEval.eval['scores'][0, :, 0, 0, 2]

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
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
plt.savefig('prcurve.jpg',dpi=250)
plt.show()
