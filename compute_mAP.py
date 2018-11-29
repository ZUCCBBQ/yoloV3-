from voc_eval import voc_eval

rec,prec,ap = voc_eval('/home/cbq/Desktop/yolo3/darknet/results/{}.txt', '/home/cbq/Desktop/yolo3/VOC/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/cbq/Desktop/yolo3/VOC/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'person', '.')

print('rec',rec)
print('prec',prec)
print('ap',ap)
