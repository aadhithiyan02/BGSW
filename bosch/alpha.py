import streamlit as st 
c1,c2,c3=st.columns([2,5,1])
c1.markdown('# This is column 1')

a=st.file_uploader("upload a photo")
# get input from camera
# b=st.camera_input("take a photo")
#accept_multiple_file to upload more than one file
imgs=st.file_uploader('upload an image',type=['jpg','png','mp4'],accept_multiple_files=True)

if imgs is not None:
    for img in imgs:
        st.image(img)
        st.success('image uploaded successfully')
        
vide1=st.file_uploader('upload  a video',type=['mp4'])
if vide1 is not None:
    st.video(vide1)
    
    
    
progress_=st.progress(0)
for perc in range(100):
    

