import cv2
import matplotlib.pyplot as plt

image = cv2.imread("/Users/atharva.gautam.29/Desktop/After class projects 1/project 65/Dice.jpg")
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_ = image_rgb.shape
arrow_start_1 = (width,645)
arrow_end_1 = (width//2 + 400,645)
cv2.arrowedLine(image_rgb,arrow_start_1,arrow_end_1,(255,0,255),3,tipLength=0.05)

arrow_start_2 = (0,645)
arrow_end_2 = (width//2 - 400,645)
cv2.arrowedLine(image_rgb,arrow_start_2,arrow_end_2,(255,0,255),3,tipLength=0.05)
text = f"Image is {width} px wide"
text_x_length = width//2 - 350
text_y_length = 645 
cv2.putText(image_rgb,text,(text_x_length,text_y_length),cv2.FONT_HERSHEY_SIMPLEX,2,(255, 120, 255),2,cv2.LINE_AA)

plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.axis("off")
plt.title("Dice")
plt.show()