import sys
import cv2
import numpy as np
from insightface.app import FaceAnalysis

camera_id = 0
delay = 1
window_name = 'frame'

app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

cap = cv2.VideoCapture(camera_id)

if not cap.isOpened():
    sys.exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    ret, frame = cap.read()
    if ret:
        faces = app.get(np.asarray(frame))
        #print('')
        #print(faces)  # gender・age プロパティが存在する・その他は特徴点の座標値と思われる
        rimg = app.draw_on(frame, faces)
        
        cv2.imshow(window_name, rimg)
    
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow(window_name)
