# YOLOv5_from_labelbox_format


This repo is used whenever you want to convert label-box format to coco for object detection.
Here I used YOLOv5 since it easy for implementation.

After converting to coco I splitted the data to train,test, val while filtering duplicated images.

<img width="607" alt="image" src="https://user-images.githubusercontent.com/51881832/180162705-32c07a7b-6996-4f14-bd48-fe91cf42ae58.png">

One important step is adding 0-10% background images to increase the performance of the model.

Before training the model you should clone the yolov5 model:

!git clone https://github.com/ultralytics/yolov5.git

%cd yolov5

!pip install -r requirements.txt

Training the model is very straight forward using yolov5, here I used hyp.scratch-low which contains augmentations and freezed all layers for better fine tuning.

!python train.py --img 416 --epochs 300 --data /content/yolov5/my_dataset1.yaml --weights 'yolov5x.pt'  --batch-size 16 --name my_model --nosave --cache --cfg /content/yolov5/models/yolov5x.yaml --hyp /content/yolov5/data/hyps/hyp.scratch-low.yaml --patience 5 --freeze 0

<img width="883" alt="image" src="https://user-images.githubusercontent.com/51881832/180163707-a68a0c2b-4e53-4559-a7a3-5b2110b682e1.png">

Next validation of the model is required:

!python val.py --weights /content/yolov5/runs/train/my_model/weights/last.pt --data /content/yolov5/my_dataset1.yaml --img 416 --conf 0.5

<img width="1069" alt="image" src="https://user-images.githubusercontent.com/51881832/180164018-0427e144-5c78-437f-b902-b6546f12dfb5.png">



![image](https://user-images.githubusercontent.com/51881832/180164302-34640b82-1cfa-4dce-a5a4-e00d54165275.png)

The results are pretty good using the fact that the model was trained on 120~ images. 

![image](https://user-images.githubusercontent.com/51881832/180164634-19b89e06-2e12-4db5-b025-50f6344448da.png)



!python detect.py --weights /content/yolov5/runs/train/exp3/weights/last.pt  --source /content/drive/MyDrive/windows_boarded_1/test/images --img 640 --save-txt --save-conf 


import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', '//content/yolov5/runs/train/no_tr_more_data_high_aug_26/weights/best.pt',force_reload=True)
