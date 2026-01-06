import streamlit as st
import requests
from PIL import Image
import io
# didi
st.title("🍅 Tomato Leaf Disease Prediction")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    bytes_data = uploaded_file.read()

    image = Image.open(io.BytesIO(bytes_data))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):

        files = {"file": (uploaded_file.name, bytes_data, uploaded_file.type)}

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files=files
        )

        if response.status_code == 200:
            result = response.json()
            st.success("Prediction Complete")
            st.markdown(f"""
            ### 🏷 Disease Predicted  
            **{result['prediction']}**

            ### 📁 File Name  
            {result['filename']}

            ### 🔥 Confidence  
            **{result['confidence']*100:.2f}%**
            """)
        else:
            st.error("Server error — check backend logs")