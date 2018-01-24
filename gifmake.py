import numpy as np
import cv2
import imageio

x_list = [x for x in range(1, 255) if x % 20 == 0]
img_list = []
path = 'F:\\my_python_toys\\'
'''
img_aa = cv2.imread(r'G:\a.bmp')
#aa_pray = cv2.cvtColor(img_aa, cv2.COLOR_BGR2HLS)
#aa_pray = cv2.cvtColor(img_aa, cv2.COLOR_BGR2GRAY)
aa_pray = img_aa
for x in x_list:
    ret, aa_thres = cv2.threshold(aa_pray, x, 255, cv2.THRESH_BINARY)
    #cv2.imshow('aa', aa_thres)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite('G:\\' + repr(x) + '_pray.bmp', aa_thres)
'''
x = 0
for x in x_list:
    try:
        img_list.append(imageio.imread('G:\\' + repr(x) + '_pray.bmp'))
    except: 
        continue

#img_list.append(imageio.imread('G:\\aa_pray.bmp'))
#img_list.append(imageio.imread('G:\\aa.bmp'))
img_list.append(imageio.imread('G:\\a.bmp'))
x_list.sort(reverse = True)

for x in x_list:
    try:
        img_list.append(imageio.imread('G:\\' + repr(x) + '_pray.bmp'))
    except:
        continue

#img_list.append(imageio.imread('G:\\aa.bmp'))
#img_list.append(imageio.imread('G:\\aa_pray.bmp'))

#img_list.append(imageio.imread('G:\\a.bmp'))
#img_list.append(imageio.imread('G:\\aa.bmp'))

imageio.mimsave('G:\\jiqi.gif', img_list, 'GIF', duration = 0.2)