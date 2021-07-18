import cv2
import pandas as pd

img=cv2.imread('Multicolor.jpg')

click=False
r=g=b=x_pos=y_pos=0

index=["color","colorName","hex","R","G","B"]
csv=pd.read_csv('colors.csv',names=index,header=None)

def getColorName(R,G,B):
    min=10000
    for i in range(len(csv)):
        d=abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d<=min:
            min=d
            cname=csv.loc[i,"colorName"]
    return cname

def drawFunction(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,x_pos,y_pos,click
        click=True
        x_pos=x
        y_pos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)





cv2.namedWindow('ColorDetection')
cv2.setMouseCallback('ColorDetection',drawFunction)

while True:
    cv2.imshow("ColorDetection",img)
    if click:
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text=getColorName(r,g,b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        click=False
    if cv2.waitKey(20)& 0xFF == 27:
        break
cv2.destroyAllWindows()