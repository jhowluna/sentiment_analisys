from tensorflow.keras.models import model_from_json
import cv2
import numpy as np
import pandas as pd

def analise(frame,img):
    json_file = open('apps/model/models/modelo_02_expressoes.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights('apps/model/models/modelo_02_expressoes.h5')

    expressoes = ["Raiva", "Medo", "Feliz", "Triste", "Surpreso", "Neutro","Nojo"]

    prediction = model.predict(img)[0]

    return prediction
