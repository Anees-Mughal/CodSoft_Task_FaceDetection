import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataset'
def getimageid(path):
    image_path =[os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for image_paths in image_path:
        faceimage = Image.open(image_paths).convert('L')
        facenp = np.array(faceimage)
        id = (os.path.split(image_paths)[-1].split(".")[1])
        id = int(id)
        faces.append(facenp)
        ids.append(id)
        cv2.imshow("train", facenp)
        cv2.waitKey(1)
    return ids, faces
IDs ,facess = getimageid(path)
recognizer.train(facess, np.array(IDs))
recognizer.write("Trainerss.yml")
cv2.destroyAllWindows()
print("Training complete........")