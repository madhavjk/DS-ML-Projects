import streamlit as st
import pandas as pd
import numpy as np
import cv2
from PIL import Image, ImageOps
from matplotlib import pyplot as plt




st.title("Image Classification Model")

'''uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))'''


def import_and_predict(image_data, model):
        
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("Aeroplane")
    elif np.argmax(prediction) == 1:
        st.write("It is a rock!")

    elif np.argmax(prediction) == 2:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 3:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 4:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 5:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 6:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 7:
        st.write("It is a rock!")
    elif np.argmax(prediction) == 8:
        st.write("It is a rock!") 
    elif np.argmax(prediction) == 9:
        st.write("It is a rock!")                               
    else:
        st.write("It is a scissor!")
    
    st.text("Probability (0: aeroplane, 1: Rock, 2: Scissor,3:  , 4:  , 5:  , 6:  ,7:   , 8:   , 9:   , 10:  ")
    st.write(prediction)