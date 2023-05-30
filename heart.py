import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('heart.sav','rb'))

st.title('Prediksi Terkena Penyakit hati')
col1, col2 = st.columns(2)

with col1:  
   age = st.number_input('usia')
   sex = st.number_input('jenis kelamin')
   cp = st.number_input('nyeri dada')
   trtbps = st.number_input('tekanan darah')
   chol = st.number_input('kolesteros')
   slp = st.number_input('sirosis hati')
   caa = st.number_input('percepatan angiopati amiloid serebral')
   
   
with col2:
   fbs= st.number_input('gula darah')
   restecg = st.number_input('istirahat')
   thalachh = st.number_input('detak jantung maksimum')
   exng = st.number_input('latihan di induksi angina')
   oldpeak = st.number_input('depresi')
   thall = st.number_input('keracunan')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[age, sex, cp, trtbps, chol, slp, caa, fbs, restecg, thalachh, exng, oldpeak, thall]])

    if(predik[0] == 1):
        predik = 'Kemungkinan Pasien yang terkena Penyakit hati'
    else:
        predik = 'Kemungkinan Pasien yang tidak terkena Penyakit hati'
st.success(predik)