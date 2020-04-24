import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#seleione del file
print('selezionare l\'immagine:')
Tk().withdraw()
filename = askopenfilename()

#conversione immagine a matrice
img=cv2.imread(filename)

#dimensioni della matrice
size=np.shape(img)
y=size[0]
x=size[1]
c=size[2]

#coordinate centro
a=int(x/2)
b=int(y/2)

#raggio corconferenza
if a>b :
    r=int(b/2)
else :
    r=int(a/2)

#assi+circonferenza
cv2.line(img,(0,b),(x,b),(255,0,0),1)
cv2.line(img,(a,0),(a,y),(255,0,0),1)
cv2.circle(img,(a,b),r,(255,0,0),2)

#output immagine
cv2.imshow('imagine',img)
cv2.imwrite('img_con_frazner_zone.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
