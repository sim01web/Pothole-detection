import numpy as np 
import tensorflow as tf
from keras.preprocessing import image
import streamlit as st

st.set_page_config(page_title="Pothole detection")
st.header("Pothole detection")

#st.write(html_temp, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit=st.button("Predict")
def image_prediction(uploaded_file):
    model= tf.keras.models.load_model(r"C:\Users\simra\Downloads\cnn.h5") 
    test_image = image.load_img(uploaded_file, target_size = (64, 64))
    # plt.imshow(cv2.imread("D:/Python/Pothole detection/potholes/123.jpg"))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)

    if result[0][0] == 1:
        prediction = 'pothole'
    else:
        prediction = 'normal'


    print(prediction)
    return prediction

if submit:
    pred=image_prediction(uploaded_file)
    st.image(uploaded_file)
    st.subheader("Prediction:")
    st.write(pred)
    st.markdown("Made by ")
    st.markdown("**Satyajeet** | **Simran** ")