import streamlit as st
import pickle


model = pickle.load(open("model.pkl", "rb"))

st.title("NewsPrediction App")


feature1 = st.text_input("Enter The news")



if st.button("Predict"):
    pred = model.predict([feature1])
    if pred == 0:
        st.info("Fake news")
    else:
        st.info("Real news") 
