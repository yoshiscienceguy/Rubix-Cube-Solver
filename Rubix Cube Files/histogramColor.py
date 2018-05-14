import cv2
from sklearn.cluster import KMeans
import numpy as np
class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None
    
    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image
        
    def dominantColors(self):
    
        #read image
        img = cv2.imread(self.IMAGE)
        
        #convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
        #reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        
        #save image after operations
        self.IMAGE = img
        
        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(img)
        
        #the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        
        #save labels
        self.LABELS = kmeans.labels_
        
        #returning after converting to integer from float
        return self.COLORS.astype(int)

img = 'cubePics/Cube1.jpg'

clusters = 6
dc = DominantColors(img, clusters) 
colors = dc.dominantColors()
frame = cv2.imread(img)
for color in colors:
    print color

    # define range of blue color in HSV
    uList = [color[0]+20,color[1]+20,color[2]+20]
    lList = [color[0]-20,color[1]-20,color[2]-20]
    lower_blue = np.array(lList, dtype = "uint8")
    upper_blue = np.array(uList, dtype = "uint8")
    #hsv = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.waitKey(0)

cv2.destroyAllWindows()
