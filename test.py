import streamlit as st
from PIL import Image

st.title("Hello World !")
st.write("Hello World !")
st.header("Hello World !")
st.subheader("Hello World !")
st.text("Hello World !")

st.text_input("Enter Text here !")
st.text_area("Enter Text here !")

st.success("Succesfully completed")
st.warning("Succesfully completed with warning !!")
st.info("Succesfully completed with info !")
st.error("Error occured")
st.exception("Exception occured !!!")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

st.image(Image.open("cat.jpeg"), width=200)

show = st.radio("Select ", ("Bilaal", "Guddi"))
if(show == "Bilaal"):
    st.success("Bilaal it is :)")
else:
    st.success("Guddi it is :)")

show1 = st.multiselect("Select ! ",
                     ['kofta Biryani', 'Tehri', 'Turkish Shawarma' ,'Chicken Afgan','Chicken 65'])
st.write('Your Selection is :')   
for i in range(len(show1)):
    st.write(show1[i])


a = st.text_input("Enter Name: ")
if(st.button('Enter')):
    r = a.title()
    st.success(r)

