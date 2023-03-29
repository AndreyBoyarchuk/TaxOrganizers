import streamlit as st
import base64

def header(image, text, url):
    with open(image, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode("utf-8")

    st.sidebar.markdown(
        f"""
        <style>
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.5rem;
                background-color: #4a90e2;
            }}
            .header-image {{
                height: 50px;
            }}
            .header-text {{
                font-size: 18px;
                color: white;
                font-weight: bold;
                text-decoration: none;
            }}
        </style>
        <div class="header">
            <img class="header-image" src="data:image/jpeg;base64,{img_data}" alt="Logo">
            <a class="header-text" href="{url}" target="_blank">{text}</a>
        </div>
        """,
        unsafe_allow_html=True
    )
