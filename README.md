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
  - Reset maxDets if needed

<details><summary><b>CLICK ME</b> - mAP with COCO API</summary>

- mAP with pycocotools (baby-v4) train
  - Reset maxDets `cocoEval.params.maxDets = [1, 100, 1000]`
  - mAP@[IoU=0.50] with Darknet **97.61 %**

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100  ] = 0.704
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=1000 ] = 0.971
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=1000 ] = 0.850
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.580
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.739
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.805
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1  ] = 0.388
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100  ] = 0.751
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=1000 ] = 0.755
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.645
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.788
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.848
```

- mAP with pycocotools (baby-v4) validation
  - mAP@[IoU=0.50] with Darknet **96.64 %**

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

- mAP with pycocotools (car-v4-tiny) train
  - mAP@[IoU=0.50] with Darknet **95.95 %**

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

<details><summary><b>V6baby</b> - mAP with COCO API</summary>

- mAP with pycocotools images291
  - yolov4

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.855
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.984
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.954
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.649
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.845
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.918
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.407
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.885
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.887
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.711
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.881
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.943

 AP@[ IoU=0.50 ] (%)
 ***********************
 Category :  AH  : 97.17
 Category :  BH  : 99.56

 AP@[ IoU=0.50:0.95 ] (%)
 ***********************
 Category :  AH  : 80.14
 Category :  BH  : 90.88
```

- mAP with pycocotools images291
  - yolov5x

```
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95:
                 all        291        951      0.991      0.962      0.986      0.866
           AdultHead        291        678      0.991      0.931      0.977      0.808
        RealBabyHead        291        273      0.991      0.993      0.996      0.923
```

- mAP with pycocotools validation
  - yolov4

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.685
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.962
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.821
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.554
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.707
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.783
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.380
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.707
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.745
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.626
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.765
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.827

 AP@[ IoU=0.50 ] (%)
 ***********************
 Category :  B   : 96.94
 Category :  Y   : 94.88
 Category :  W   : 96.33
 Category :  R   : 93.79
 Category :  AH  : 96.45
 Category :  BH  : 98.92

 AP@[ IoU=0.50:0.95 ] (%)
 ***********************
 Category :  B   : 66.45
 Category :  Y   : 62.23
 Category :  W   : 64.93
 Category :  R   : 62.45
 Category :  AH  : 70.47
 Category :  BH  : 84.64
```

- mAP with pycocotools validation
  - yolov5x

```
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95:
                 all       3401       7804      0.961      0.923      0.963      0.725
                blue       3401        559      0.967      0.938      0.974      0.693
              yellow       3401        813      0.952      0.902      0.945      0.651
               white       3401        786      0.956      0.907      0.957      0.672
                 red       3401        749      0.933      0.878      0.934      0.647
           AdultHead       3401       2349      0.964      0.923      0.969      0.764
        RealBabyHead       3401       2548      0.996      0.991      0.996      0.922
```

</details>

<details><summary><b>V7baby</b> - mAP with COCO API</summary>

- mAP with pycocotools images291
  - yolov4

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.880
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.994
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.983
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.716
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.883
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.923
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.406
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.907
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.908
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.760
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.910
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.949

 AP@[ IoU=0.50 ] (%)
 ***********************
 Category :  AH  : 98.86
 Category :  BH  : 100.00

 AP@[ IoU=0.50:0.95 ] (%)
 ***********************
 Category :  AH  : 83.22
 Category :  BH  : 92.80
```

- mAP with pycocotools images291
  - yolov5x

```
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95:
                 all        291        951      0.998      0.998      0.997       0.92
           AdultHead        291        678      0.999      0.996      0.997      0.888
        RealBabyHead        291        273      0.998          1      0.996      0.952
```

- mAP with pycocotools validation
  - yolov4

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.686
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.963
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.822
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.556
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.709
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.781
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.379
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.706
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.745
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.625
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.766
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.827

 AP@[ IoU=0.50 ] (%)
 ***********************
 Category :  B   : 97.19
 Category :  Y   : 94.91
 Category :  W   : 95.98
 Category :  R   : 94.06
 Category :  AH  : 96.48
 Category :  BH  : 98.92

 AP@[ IoU=0.50:0.95 ] (%)
 ***********************
 Category :  B   : 66.65
 Category :  Y   : 62.23
 Category :  W   : 64.49
 Category :  R   : 62.97
 Category :  AH  : 70.71
 Category :  BH  : 84.40
```

- mAP with pycocotools validation
  - yolov5x

```
               Class     Images     Labels          P          R     mAP@.5 mAP@.5:.95:
                 all       3401       7804      0.961      0.924      0.963      0.726
                blue       3401        559      0.963      0.937      0.971      0.689
              yellow       3401        813      0.943      0.894      0.944      0.653
               white       3401        786      0.957       0.91      0.957      0.672
                 red       3401        749      0.938      0.888      0.942      0.654
           AdultHead       3401       2349      0.967      0.927      0.967      0.766
        RealBabyHead       3401       2548      0.997      0.991      0.996      0.918
```

</details>

<details><summary><b>V7baby</b> - Comparison Darknet v.s. tkDNN-TensorRT (FPS)</summary>

* Inference FPS of Yolov4 with **Darknet** and **tkDNN-TensorRT** on custom trained model
* Platform: **GeForce RTX 2080 Ti:**
* Video Dimensions: 848 x 480

| Network Size | Darknet AVG_FPS | tkDNN-TensorRT FP32 (B=1) | tkDNN-TensorRT FP32 (B=4) | tkDNN-TensorRT FP16 (B=1) | tkDNN-TensorRT FP16 (B=4) |
|:------------:|:---------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
| Yolov4 512   |  78.3           | 98.4                      | 123.3                     | 149.5                     | 197.4                     |

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
