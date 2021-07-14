# mAP_eval (Custom dataset)

## How to use the scripts

- Verifying mAP for the custom dataset with results generated from [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)

```
$ ./darknet detector test baby.data baby.cfg baby.weights -thresh 0.001 -dont_show -ext_output < test.txt > result.txt
```

- Removing lines from the text file containing specific words

```
$ grep -vE "(Detection|Enter)" result.txt > result2.txt
```

- Modify `separator_key='...'` in `pred_yolo2json.py`
- Run the code `demo-baby.py` and Yolo Darknet Detection/GT files will be converted to pycocotools json format
  - It might be a good idea to rename the file names, e.g. `train1.jpg, train2.jpg, ... train5011.jpg`
- Run the code `demo-mAP.py`  and mAP will be shown on screen

<details><summary><b>CLICK ME</b> - mAP with COCO API</summary>

- mAP with pycocotools (baby-v4) train
  - mAP@[IoU=0.50] with Darknet 97.61 %

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.704
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.963
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.848
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.576
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.738
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.805
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.388
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.709
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.751
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.639
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.787
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.848
```

- mAP with pycocotools (baby-v4) validation
  - mAP@[IoU=0.50] with Darknet 96.64 %

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.685
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.962
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.821
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.554
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.708
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.783
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.380
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.707
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.745
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.626
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.765
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.827
```

- mAP with pycocotools (baby-v4-csp-swish) validation
  - mAP@[IoU=0.50] with Darknet 96.30 %

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.686
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.957
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.820
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.561
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.713
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.771
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.376
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.704
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.743
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.653
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.765
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.819
```

- mAP with pycocotools (car-v4-tiny) train
  - mAP@[IoU=0.50] with Darknet 95.95 %

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.753
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.956
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.913
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.636
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.810
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.850
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.702
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.796
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.796
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.696
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.848
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.875
```

- mAP with pycocotools (car-v4-tiny) validation
  - mAP@[IoU=0.50] with Darknet **99.81 %**

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.625
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.997
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.705
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.464
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.628
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.717
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.645
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.692
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.692
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.578
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.695
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.717
```

- mAP with pycocotools (emotion-v4-tiny) validation
  - mAP@[IoU=0.50] with Darknet **68.22 %**

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.484
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.683
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.635
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.568
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.464
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.479
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.761
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.761
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.761
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.746
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.709
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.770
```

</details>

- We can modify `cocoapi/PythonAPI/pycocotools/cocoeval.py` to calculate AP for each class (https://stackoverflow.com/questions/56247323/coco-api-evaluation-for-subset-of-classes). Add following code between lines 458-464

    ```python
    num_classes = 6
    avg_ap = 0.0
    if ap == 1:
        for i in range(0, num_classes):
            print('category : {0} : {1}'.format(i,np.mean(s[:,:,i,:])))
            avg_ap +=np.mean(s[:,:,i,:])
        print('(all categories) mAP : {}'.format(avg_ap / num_classes))
    ```

## Issues related to COCO API

<details><summary><b>CLICK ME</b> - Issues related to COCO API</summary>

- https://github.com/AlexeyAB/darknet/issues/2140
- https://github.com/AlexeyAB/darknet/issues/3094
- https://github.com/AlexeyAB/darknet/issues/7808
- https://github.com/AlexeyAB/darknet/issues/2145
- https://github.com/AlexeyAB/darknet/issues/5643

</details>

---

# mAP_eval (In progress)

Goals:
1. Convert Yolo Darknet Ground Truth Files to pycocotools json (Done)
2. Convert Yolo Darknet Detection Files to pycocotools json (Done)
3. Convert Yolo Darknet Ground Truth/Detection Files to */groundtruths /detections* folder usable by [rafaelpadilla/Object-Detection-Metrics](https://github.com/rafaelpadilla/Object-Detection-Metrics)
4. Customizable Ground Truth/Detection format for custom datasets

Current state:
Verifying mAP for the 5k validation dataset with results generated from [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) .  
`./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights -thresh 0.005 -dont_show -ext_output < /5k.txt > result.txt`  

Refer to demo.ipynb for details

![map_0 5iou_darknet](https://user-images.githubusercontent.com/22487836/50642471-3afa9800-0fa6-11e9-89da-bb8fb294b863.png)



# References

1. [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
2. [rafaelpadilla/Object-Detection-Metrics](https://github.com/rafaelpadilla/Object-Detection-Metrics)
3. [Cartucho/mAP](https://github.com/Cartucho/mAP)
4. [cocodataset/cocoapi](https://github.com/cocodataset/cocoapi)
