import streamlit as st
import os 
from deeplearning import OCR
import PIL.Image as Image
import cv2

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'./static/upload/')
PREDICT_PATH = os.path.join(BASE_PATH,'./static/predict/')
ROI_PATH = os.path.join(BASE_PATH,'./static/roi/')


# def get_image_path(img):
#     # Create a directory and save the uploaded image.
#     file_path = f"data/uploadedImages/{img.name}"
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     with open(file_path, "wb") as img_file:
#         img_file.write(img.getbuffer())
#     return file_path

uploaded_file = st.file_uploader("Upload Car image...", type= ['png', 'jpg'] )

if uploaded_file is not None:
    filename = uploaded_file.name
    #st.write(uploaded_file)

    bytes_data = uploaded_file.getvalue()
    st.write("Input Image:")
    st.image(bytes_data)
        
    # Save File
    path_save = os.path.join(UPLOAD_PATH,filename)
    path_predict = os.path.join(PREDICT_PATH,filename)
    path_roi = os.path.join(ROI_PATH,filename)


    # Saving Uploaded File
    with open(path_save, "wb") as f:
        f.write(uploaded_file.getbuffer())        

    if st.button("Process..."):
        text = OCR(path_save,filename)
        
       
        st.image(path_predict, caption='Predicted Region of License Plate')
        st.image(path_roi, caption='Extracted License Plate Image')

        st.write("Detected License Plate #")
        st.write(text)

#     return render_template('index.html',upload=True,upload_image=filename,text=text)

#  return render_template('index.html',upload=False)
