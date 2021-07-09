from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

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
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

#print(cocoEval.stats)
