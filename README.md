# yoloV3-
darknet版本的yoloV3实验复现中出现的坑点记录
yoloV3是目标检测算法
参考资料：https://pjreddie.com/darknet/yolo/
         https://blog.csdn.net/c20081052/article/details/80236015
原文链接：http://arxiv.org/abs/1506.02640 
GPU选择：https://www.cnblogs.com/darkknightzh/p/6591923.html#_label0
opencv:安装OpenCV太麻烦了所有在实验的时候安装了opencv-contrib-python
论文实验结果复现：首先需要下载yoloV3.weight。（wget https://pjreddie.com/media/files/yolov3.weights）
                用这个文件和data/文件夹下面的dog.jpg可以复现出论文里面的dog图片结果
                实验很简单：./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
                yolov3.cfg是darknet自带的文件应该不需要修改（具体忘了）。
在VOC数据集上训练：训练数据：
                          下载文件：wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
                                   wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
                                   wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
                          解压文件：tar xf VOCtrainval_11-May-2012.tar
                                   tar xf VOCtrainval_06-Nov-2007.tar
                                   tar xf VOCtest_06-Nov-2007.tar
                          识别出目标要生成标签（没标签网络自然学习不了目标是啥）：
                                   wget https://pjreddie.com/media/files/voc_label.py
                                   python voc_label.py
                          *生成标签之后还要生成一个train.txt文件：cat 2007_train.txt 2007_val.txt 2012_*.txt > train.txt
                   下载卷积网络：wget https://pjreddie.com/media/files/darknet53.conv.74
                   训练：./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74
                         要修改的部分：1、voc.data 主要修改两个文件的路径；测试文件和训练wenjian
                                  !**!2、yolo3-voc.cfg：这个文件最好重新复制两份，重新命名，一份用来训练，一份用来测试。
                                         1).如果你的darknet没有问题的话就不要修改这一部分了，因为一般都是对的：
                                          链接https://github.com/AlexeyAB/darknet有一个
                                          How to train (to detect your custom objects)模块照着该就好，主要是根据class改filter的内容，一般不需要动
                                          如果你的class改变了，那么可以根据公式改filter。
                                         2).上面我们复制了两个文件需要修改，主要修改batch和subdivisions
                                            训练的时候batch=64、subdivision=16
                                            测试的时候batch=1、subdivision=1
                                            这是困扰我很久的地方，当然你也可以不用复制两个文件，在一个文件里修改就可以了。
                                            之前跑测试的时候我们一直用的batch=1、subdivision=1，在训练的时候如果不改就导致大面积的iou=nan、
                                            obj=nan的问题，为什么？识别不出来啊。
                                            当然训练的时候你也可以batch用小一点，那么速度就会快一些。
在用自己的模型识别的时候也有一个坑点(当然到现在我也没明白)：./darknet detector test cfg/voc.data cfg/yolov3-obj-test.cfg backup/yolov3_final.weights data/Desk.jpg
请使用detector test 这个方式。在第一个参考资料里有很多测试的命令，我用过其他的，行不通，导致结果会把显示器测试成cow。（所以它是瞎了么~~）
总结：整个模型在TITAN X上跑了三天多一点，结果还ok
     1.我其实跑的还挺慢的，主要是batchsize给了64，其他的GPU优化也没有做。当然有时候没必要等他训练完了再去测试，在backup文件夹下有不同阶段的
     weight文件，可以提前去测试看一看结果。
     2.生成的weight文件在backup文件夹下面，整个模型迭代了五万多次才好，里面的weight文件都能用，但是准确度不一样。
     3.计算mAP(准确度),用的是别人写的compute_mAP.py文件，这个文件是在python2的环境下跑的，这里这个人也没有给全文件还缺少一个voc_eval.py文件。我上传了
     https://blog.csdn.net/LeeWanzhi/article/details/79690275
     其实写的也不太好,要注意的就是改compute_mAP.py文件的路径问题，其他就是一些小bug可以自己调通的。
     4.mAP结果：其实这个mAP测试的是不同类别的obj的精准度，VOC数据集有20个类别嘛，我测了person，train之类的能达到78-80左右。当然测试的时候是很快的
写在最后：1.写的也不多，主要是记录一下以防以后会用到，看不懂可以自己在查一查，是在不行也可以问我，当然还是自己查比较好。（本来也没指望能给别人讲懂）
         2.我上面出现的问题都是小问题，新手可能比较有用吧。
         3.yolo这个网络，怎么说呢，还是挺快的，但是我这个复现实验其实就是做了一些微小的工作（呱），如果应用到实战中的话最难的应该是整理数据集（打标签）吧
         4.VOC的数据集也不是很美妙，总共就20个种类。我测试的时候拍了自己桌子的照片，有笔记本，显示器，键盘之类的东西。就给我识别出一个显示器。没识别出的
         应该是没有这一类吧。
 
