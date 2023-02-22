 
import cv2
from PIL import Image
import tempfile
from graphviz import Digraph
import streamlit as st 


st.title('TRAFFIC VEHICLES AND OBJECT DETECTION DASHBOARD')
st.markdown('**Python Libraries:** tensorflow, keras,pygame,streamlit''')
st.write(' **Our Objectives:** ')
st.write('''
         * Object detection using Yolo and CNN models
         * Object Classification using CNN
         * Vehicle count based on the classifications from CNN model
         * Minimising Traffic using Vehicle count to prioritise lanes with
         higher vehicle rates
         ''')
st.markdown('---')

st.write('**Our Approach:**')
st.write('''
         Project Flow 
        
         ''')


image1=Image.open('C:\\Users\\saadh\\Downloads\\Object Detect.jpg',)
st.image(image1)
st.write()
st.sidebar.title('Settings')


confidence= st.sidebar.slider('Confidence',0.0,1.0,0.5)
st.sidebar.markdown('---')

#save_img=st.sidebar.checkbox('save video')
#enable_gpu=st.sidebar.checkbox('Enable GPU')
custom_class=st.sidebar.checkbox('Use Custom Class')
assigned_class_id=[]

if custom_class:
    assigned_class = st.sidebar.multiselect('Select the Custom Classes',['cars','bikes','truck'], default='cars')
    #for each in assigned_class:
        #assigned_class_id.append(list.index(each))
st.sidebar.markdown('---')        
video_file_buffer=st.file_uploader('**Upload a video**',type=['mp4','mov','avi','asf','m4v'])


if video_file_buffer is not None:
    st.video(video_file_buffer)
    st.success('Video uploaded successfully')
st.markdown('---')
    
#stframe=st.empty()

st.sidebar.markdown('---')

st.write('Trained Model Output')
st.video('C:\\Users\\saadh\\Desktop\\bosch\\sample.mp4')

st.write(' **Traffic Light Control Simulation:**')

st.video('C:\\Users\\saadh\\Desktop\\bosch\\simulation.mp4')


st.write(''' **References** 
         
         ''')
st.write('''
         * https://www.tensorflow.org/
         * https://ultralytics.com/yolov8
         * https://streamlit.io/
         * https://www.researchgate.net/publication/330890240
         ''')
