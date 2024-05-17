import streamlit as st
from streamlit_option_menu import option_menu
from pages import home, subtitle_generator, biology_tutor

st.set_page_config(page_title="AI-based Biology Tutor Application", layout="wide")

def main():
    with st.sidebar:
        selected = option_menu(
            "Main Menu",
            ["Home", "Subtitle Generator", "Biology Tutor"],
            icons=["house", "video", "book"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Home":
        home.home()
    elif selected == "Subtitle Generator":
        subtitle_generator.subtitle_generator()
    elif selected == "Biology Tutor":
        biology_tutor.biology_tutor()

if __name__ == "__main__":
    main()
