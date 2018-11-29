# yoloV3-实验复现
### darknet版本的yoloV3实验复现中出现的坑点记录
#### 参考资料：
https://pjreddie.com/darknet/yolo/<br />
https://blog.csdn.net/c20081052/article/details/80236015<br />
#### 原文链接：http://arxiv.org/abs/1506.02640 <br />
#### GPU选择：https://www.cnblogs.com/darkknightzh/p/6591923.html#_label0<br />
opencv:安装OpenCV太麻烦了所有在实验的时候安装了opencv-contrib-python<br />
#### 论文实验结果复现：
   1.首先需要下载yoloV3.weight。<br />
   ```wget https://pjreddie.com/media/files/yolov3.weights```<br />
   2.用这个文件和data/文件夹下面的dog.jpg可以复现出论文里面的dog图片结果<br />
   3.实验很简单：./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg<br />
     yolov3.cfg是darknet自带的文件应该不需要修改（具体忘了）。<br />
#### 在VOC数据集上训练：  
&ensp;&ensp;&ensp;&ensp;训练数据:  
&ensp;&ensp;&ensp;&ensp;下载文件：
