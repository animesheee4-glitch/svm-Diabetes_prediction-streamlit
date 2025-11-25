import streamlit as st
<<<<<<< HEAD
import cv2
import numpy as np
from PIL import Image

st.title("📸 Fall Detection System (Image-based)")
st.write("Upload an image containing a person, and the app will predict if a fall has occurred.")

uploaded_img = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_img:
    # Display uploaded image
    img = Image.open(uploaded_img)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # Threshold for contour detection
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fall_detected = False

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)

        # Ignore very small objects (noise)
        if area < 1500:
            continue

        # Height-width ratio — used as simple posture estimate
        ratio = h / float(w)

        # If width > height → lying down → possible fall
        if w > h:
            fall_detected = True

        # Draw bounding box
        cv2.rectangle(img_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)

    st.write("### 🧾 Processed Image")
    st.image(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))

    # Final Result
    if fall_detected:
        st.error("⚠️ FALL DETECTED!")
    else:
        st.success("✅ No Fall Detected")
=======
import pickle
st.title("SVM")

model=pickle.load(open("svm.sav",'rb'))
def prediction(new_data):
    outcome=model.predict(new_data)
    return outcome


def main():
    Pregnancies=st.slider("NO of Preganancies", 0,20,0)
    Glucose=st.slider("Glocuse amount",0,199,25)
    BloodPressure=st.slider("BloodPressure amount",0,122,25)
    SkinThickness=st.slider("SkinThickness amount",0,100,25)
    Insulin=st.slider("Insulin amount",0,1000,25)
    BMI=st.slider("BMI amount",0,70,25)
    DiabetesPedigree=st.slider("DiabetesPedigreeFunction amount",0.0,3.0,1.5)
    Age=st.slider("Age ",0,120,25)


    new_data=[[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
        BMI, DiabetesPedigree, Age]]
    if st.button("Predict"):
        Outcome=prediction(new_data)
        st.write(Outcome)
        if Outcome==0:
           st.info("Patient has No diabetes")
        else:
            st.info("NOn diabetic")

if __name__ == "_main_":
    main()
>>>>>>> d68e22f (update)
