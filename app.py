import streamlit as st
from quiz_generation.quiz_gen import create_quiz, post_process

st.title("Quiz Generator From Text")
st.write("This app generates a quiz from the text you provide.")
input_text = st.text_area("Enter the text to generate questions from:", height=200)
if st.button("Generate Quiz"):
    if input_text:
        with st.spinner("Generating quiz..."):
            result = create_quiz(input_text)
        st.success("Quiz generated successfully!")
        number_of_questions = len(result.quiz_out)
        for i in range(number_of_questions):
            quiz=post_process(result, i)
            st.write(quiz[0])
            selected_option=st.radio("Select the correct answer:", options=quiz[1], key=f"question_{i}")
            if selected_option==quiz[1][quiz[2]]:
                st.success("Correct answer!")
            else:
                st.error("worong answer")
    else:
        st.error("Please enter some text to generate a quiz.")