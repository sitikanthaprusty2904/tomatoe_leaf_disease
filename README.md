# 🌱 Tomato Leaf Disease Classification (Deep Learning)

## 🔍 Project Summary
### Image classification system to detect tomato leaf diseases
### Focus on model performance, limitations, and real-world challenges
### Built as a learning + accuracy chasing

## 🎯 Problem Statement
### Manual disease detection is slow and error-prone
### Goal: classify tomato leaf diseases from images using deep learning

## 📊 Dataset
### Source: kaggle
### Classes: Multiple tomato diseases + healthy - (10 classes)

# 🧠 Approach

## Data Preparation
### Image resizing & normalization
### Data augmentation (flip, rotate, zoom)
### Train / validation split

# 🛠️ Tech Stack
## Python
### Matplotlib, tensirflow, keras , opendatasets
## Streamlit (frontend)
## FastAPI (API backend)
## Docker (containerization)


## Model
### CNN-based image classifier
### Applied transfer learning using an ImageNET-pretrained CNN 
### Fine-tuning the final convulational block (Block-5) 
### Designin a custom ANN-based classification head from scratch

## Training
### Loss: Categorical Cross-Entropy
### Optimizer: RMSprop with learning_rate=2e-5
### Metrics: Accuracy


# 📈 Results
## High accuracy achieved 93.79%
## High validation accuracy achieved 91.60%
### Transfer learning improved
### Faster convergence
### Better generalization



