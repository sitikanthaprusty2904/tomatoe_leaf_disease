# import streamlit as st
# import requests
# from PIL import Image
# import io
# # didi
# st.title("🍅 Tomato Leaf Disease Prediction")

# uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

# if uploaded_file is not None:

#     bytes_data = uploaded_file.read()

#     image = Image.open(io.BytesIO(bytes_data))
#     st.image(image, caption="Uploaded Image", use_container_width=True)

#     if st.button("Predict"):

#         files = {"file": (uploaded_file.name, bytes_data, uploaded_file.type)}

#         response = requests.post(
#             "http://127.0.0.1:8000/predict",
#             files=files
#         )

#         if response.status_code == 200:
#             result = response.json()
#             st.success("Prediction Complete")
#             st.markdown(f"""
#             ### 🏷 Disease Predicted  
#             **{result['prediction']}**

#             ### 📁 File Name  
#             {result['filename']}

#             ### 🔥 Confidence  
#             **{result['confidence']*100:.2f}%**
#             """)
#         else:
#             st.error("Server error — check backend logs")

import streamlit as st
import requests
from PIL import Image
import io
import time
url="https://leafscan-10.onrender.com/predict"
# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="LeafScan AI",
    page_icon="🌿",
    layout="wide", # Uses the full width of the screen
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for a "Classy" look in both Light and Dark modes
st.markdown("""
    <style>
    /* Smooth transitions */
    .stApp {
        transition: background-color 0.5s ease;
    }
    /* Stylish Gradient Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8080 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(255, 75, 75, 0.3);
    }
    /* Rounded image corners with shadow */
    img {
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Setup
with st.sidebar:
    st.header("⚙️ Settings & Theme")
    st.info("💡 **Pro Tip:** Toggle between **Dark Mode** and **Light Mode** by clicking the **⋮** menu in the top right corner -> Settings -> Theme.")
    st.divider()
    st.markdown("### About LeafScan AI")
    st.write("Powered by a Deep Learning CNN pipeline to detect diseases in tomato leaves instantly.")

# 4. Main Header
st.title("🌿 Tomato Leaf Disease AI")
st.markdown("**Upload a clear specimen image below to run the diagnostic model.**")

# 5. File Uploader
uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png"])

# 6. Two-Column Layout (The secret to a pro-looking app)
if uploaded_file is not None:
    # Create two columns with a bit of a gap
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📷 Specimen")
        bytes_data = uploaded_file.read()
        image = Image.open(io.BytesIO(bytes_data))
        st.image(image, use_container_width=True)

    with col2:
        st.markdown("### 🔬 Diagnostics")
        st.write("Image loaded. Ready for AI analysis.")

        if st.button("Run AI Prediction", use_container_width=True):
            # Sleek loading animation
            with st.spinner('Analyzing cell structures...'):
                time.sleep(0.5) # Optional: slight delay makes the animation visible

                files = {"file": (uploaded_file.name, bytes_data, uploaded_file.type)}
                
                try:
                    response = requests.post(url, files=files)

                    if response.status_code == 200:
                        result = response.json()
                        confidence = result['confidence'] * 100

                        # Cool popup notification
                        st.toast("Analysis Complete!", icon="✅")

                        # Display results using professional metrics
                        if result['prediction'].lower() == "healthy":
                            st.success("Status: Healthy")
                        else:
                            st.warning("Status: Disease Detected")

                        st.metric(label="Predicted Condition", value=result['prediction'])
                        
                        # Visual progress bar for confidence
                        st.write(f"**Confidence Level:** {confidence:.2f}%")
                        st.progress(float(result['confidence']))

                    else:
                        st.error("Server error — check backend logs")
                        
                except requests.exceptions.ConnectionError:
                    st.error("🚨 Backend is offline. Please make sure FastAPI is running on port 8000.")