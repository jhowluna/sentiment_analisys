import time
import cv2
from sentiment import sentiment
import numpy as np
import pandas as pd
from datetime import datetime

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 2

def video(nome):
    current = datetime.now()

    list_cutis= []
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    #bbox = cv2.selectROI(frame, False)
    list_sentiment = []
    while (True):

        ret, frame = cap.read()
        #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('apps/cascade/haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = roi_gray.astype("float") / 255.0
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1,
                          norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)

            expressao = sentiment.analise(frame, cropped_img)
            #list_cabelo.append(hair_color)
            #cv2.putText(frame, f'cabelo: {hair_color}', (2, frame.shape[0]-55), font,fontScale, color, thickness, cv2.LINE_AA)
            #cv2.putText(frame, f'cutis: {expressao}', (2, frame.shape[0]-5), font,fontScale, color, thickness, cv2.LINE_AA)
            list_sentiment.append(expressao)
            # curtis = expressoes[int(np.argmax(prediction))]
        time.sleep(1)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    data = pd.DataFrame(list_sentiment, columns=["Raiva", "Medo", "Feliz", "Triste", "Surpreso", "Neutro","Nojo"])
    data.to_csv(f'media/csv/{nome}{current.strftime("%m-%d-%Y_%H")}.csv',index=False)
    return data