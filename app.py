import streamlit as st
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

if __name__ == "__main__":
    main()