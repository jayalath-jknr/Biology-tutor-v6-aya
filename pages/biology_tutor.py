import streamlit as st
from utils.tutor_utils import get_biology_explanation, generate_study_material

def biology_tutor():
    st.title("Biology Tutor")

    st.header("Ask a Biology Question")
    question = st.text_input("Enter your biology question:")
    if st.button("Get Explanation"):
        if question:
            with st.spinner("Generating explanation..."):
                explanation = get_biology_explanation(question)
                st.write("Explanation:", explanation)
        else:
            st.error("Please enter a biology question.")

    st.header("Generate Study Material")
    topic = st.text_input("Enter a biology topic:")
    if st.button("Generate Study Material"):
        if topic:
            with st.spinner("Generating study material..."):
                study_material = generate_study_material(topic)
                st.write("Study Material:", study_material)
        else:
            st.error("Please enter a biology topic.")
