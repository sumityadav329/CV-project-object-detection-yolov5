import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ["hello", "Yes", "No", "Thanks", "ILoveYou", "Please" ]

number_of_images = 5

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    if not os.path.exists(img_path):
        os.makedirs(img_path)

    # open camera
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(img_path, label+'.'+'{}.jpg'.format(str(uuid.uuid1()))) 
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    
    cap.release()

cv2.destroyAllWindows()
