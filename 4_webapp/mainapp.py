#
# mainapp.py
# Author : Sushil K Sharma
#

import streamlit as st
import base64

st.set_page_config(
    page_title="CSTU Team2 Tensorflow Project",
    page_icon="🤖",
    layout="wide",
)

#-----------------------------------------------
# @st.cache_data
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_image_as_page_bg(jpg_file):
#     bin_str = get_base64_of_bin_file(jpg_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/jpg;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
# set_image_as_page_bg('./images/bg.jpg')
#------------------------------------------------------

st.title("CSTU Team2 : Tensorflow Car Licenseplate Detection!")

st.sidebar.success("Select a site above.")

col1, col2, col3  = st.columns(3)

credits_text1 = """
## MB/CSE 638 Deep Learning with TensorFlow

- Project Git: [Github](https://github.com/krishnatray/cstu_tf_project.git)

---------------------
## Project Team:
- Sushil K Sharma, MSCSE Student [Linkedin](https://linkedin.com/in/krishnatray)
- Vaishali Chauhan, MSCSE Student [Linkedin](https://www.linkedin.com/in/vaishali-chauhan-csr/)
- Gurpreet Kaur, MBA Student [Linkedin](https://www.linkedin.com/)              
---------------------
"""

credits_text2 = """
## Professor:
#### Shih-Yu Chang, PhD (sychangair@gmail.com)

California Science and Technology University
https://www.cstu.edu/

---------------------
"""

with col1:
    st.image('./images/ai.png', caption='AI', output_format="auto")


with col2:
    st.markdown(credits_text1) 


with col3:
    st.markdown(credits_text2) 