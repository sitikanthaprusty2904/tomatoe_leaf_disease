from fastapi import FastAPI, UploadFile, File
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import io
import uvicorn
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = FastAPI(
    title="Tomato Leaf Disease Prediction API",
    description="Upload a tomato leaf image to get prediction",
    version="1.0"
)

model = load_model("model.keras", compile=False)

CLASS_NAMES = [
    "Bacterial Spot",
    "Early Blight",
    "Late Blight",
    "Leaf Mold",
    "Septoria Leaf Spot",
    "Spider Mites",
    "Target Spot",
    "Yellow Leaf Curl Virus",
    "Mosaic Virus",
    "Healthy"
]

# didi
def preprocess(image: Image.Image):
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.get("/")
def home():
    return {"message": "Tomato Leaf Disease Prediction API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    input_img = preprocess(image)

    preds = model.predict(input_img)

    class_index = np.argmax(preds[0])
    confidence = float(np.max(preds[0]))

    return {
        "filename": file.filename,
        "prediction": CLASS_NAMES[class_index],
        "confidence": round(confidence, 4)
    }
    

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)