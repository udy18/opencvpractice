import cv2
from matplotlib import pyplot as plt
#opencv is bgr and mp is rgb
img=cv2.imread(r"\obj.jpg")
img=cv2.resize(img,(512,512))
img=cv2.imread(r"cg.jpeg",0)
frame=cv2.imread(r"product.jpg")
frame=cv2.resize(frame,(512,512))
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
'''threshold:segmentation technique used for speerating object from background'''
_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
#value inv means black is white and white is black
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
'''
_,th3=cv2.threshold(img,127,255,cv2.THRESH_MASK)'''

#pixel less than threshold value is 0 so black
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#thresh trunc is that after set value all values above it or below it can be made 
# to be the closest value of threshold
_,th5=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)

titles=['og','bin','bininv','tozero','trunc']
images=[img,th1,th2,th4,th5]
for i in range(5):
    #rows,col,index of img
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
