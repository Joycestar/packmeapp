import streamlit as st
from PIL import Image
img = Image.open("joy.png")

st.image(img, width=205)

st.title("welcome to pack-me moving company")
st.subheader("Giving you a stress free relocation")
st.text("At pack-me moving company,\n we are committed to giving\n you the best relocation in \n the city of Abuja.")
st.text("we also render other services \n like cleaning, packing, moving, electricals, \n rearranging and general house care.")
st.text("Are you willing to expirence stress free services from us?")
if st.checkbox("YES"):
 st.text("you have made the right decision")
if st.checkbox("NO"):
 st.text("Feel free to contact us some other time")
status = st.radio("from: ",('Asokoro', 'Apo','kubwa','Guzape','karu','lugbe','maitama',))
if (status=='Asokoro'):
 st.success('Asokoro')

if (status=='Apo'):
    st.success('Apo')

if (status=='kubwa'):
     st.success('kubwa')

if (status=='Guzape'):
    st.success('Guzape')

if (status=='karu'):
    st.success('karu')

if (status=='lugbe'):
    st.success('lugbe')

if (status=='maitama'):
    st.success('maitama')
 
st.text_input("where are you moving to")

st.text_input("What is your name")

st.text_input("phone number")

st.text_input("when would you like to move")

st.text_input("Any special request?")

level = st.slider("How satisfied are you on a scale of 5?", 1, 5)
st.text('selected: {}'.format(level))
