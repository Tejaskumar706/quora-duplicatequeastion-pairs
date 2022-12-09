import streamlit as st
import helper
import pickle
file1= open('C:/Users/hp/Downloads/duplicate_question_nlp/quora-question-pairs-main/model.pkl','rb')
model = pickle.load(file1)

st.header('Duplicate Question Pairs')
q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplpicate')


