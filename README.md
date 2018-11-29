# yoloV3-实验复现
### darknet版本的yoloV3实验复现中出现的坑点记录
#### 参考资料：
https://pjreddie.com/darknet/yolo/<br />
https://blog.csdn.net/c20081052/article/details/80236015<br />
#### 原文链接：http://arxiv.org/abs/1506.02640 <br />
#### GPU选择：https://www.cnblogs.com/darkknightzh/p/6591923.html#_label0<br />
opencv:安装OpenCV太麻烦了所有在实验的时候安装了opencv-contrib-python<br />
#### 论文实验结果复现：
&emsp;&emsp;&emsp;&emsp;1.首先需要下载yoloV3.weight。<br />
&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/yolov3.weights```<br />
&emsp;&emsp;&emsp;&emsp;2.用这个文件和data/文件夹下面的dog.jpg可以复现出论文里面的dog图片结果<br />
&emsp;&emsp;&emsp;&emsp;3.实验很简单：./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg<br />
&emsp;&emsp;&emsp;&emsp;yolov3.cfg是darknet自带的文件应该不需要修改（具体忘了）。<br />
#### 在VOC数据集上训练：  
&emsp;&emsp;&emsp;&emsp;下载数据:  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar```  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar```  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar```  
&emsp;&emsp;&emsp;&emsp;解压文件:  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar```  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar```  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar```  
&emsp;&emsp;&emsp;&emsp;识别出目标要生成标签（没标签网络自然学习不了目标是啥）：  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```wget https://pjreddie.com/media/files/voc_label.py```  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;python voc_label.py  
&emsp;&emsp;&emsp;&emsp;*生成标签之后还要生成一个train.txt文件：  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;```cat 2007_train.txt 2007_val.txt 2012_*.txt > train.txt```
