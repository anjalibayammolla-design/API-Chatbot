import streamlit as st
st.title("AI CHATBOT")
st.write("welcome to ai chatbot")
prompt=st.text_input("Enter your prompt")
if st.button("Generate"):
    if prompt:
        st.success("You entered a question")
        st.write(prompt)
    else:
        st.warning("Please enter a question")

