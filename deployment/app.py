import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'EDA of Dataset', 'Model Prediksi Klasifikasi'])

if page == 'Home Page':
    st.title('Selamat Datang di Model Prediksi Kebangkrutan')
    st.header('Model ini berfungsi untuk membuat prediksi kebangkrutan sebuah perusahaan')
    st.divider()
    st.write('Silahkan masuk ke menu : "Model Prediksi Klasifikasi" untuk memulai program')
    st.divider()
    st.caption('Model dibuat oleh Edy untuk VANGUARD Investment Group')
    # Insert image here
    st.image("vanguard.jpg", width=250)
elif page == 'EDA of Dataset':
    eda.run()
else:
    model.run()
