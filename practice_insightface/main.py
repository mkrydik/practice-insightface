import numpy as np
import cv2
from insightface.app import FaceAnalysis

def main() -> None:
    image_file = './input.jpg'
    img = cv2.imread(image_file)
    
    app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    
    faces = app.get(np.asarray(img))
    print('Faces : ' + str(len(faces)))
    
    rimg = app.draw_on(img, faces)
    cv2.imwrite('./output.jpg', rimg)

if __name__ == "__main__":
    main()
