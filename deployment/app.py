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
    st.markdown('Model dibuat oleh <a href="https://www.linkedin.com/in/edysetiawan/" target="_blank" style="font-size: 20px;">Edy Setiawan</a>', unsafe_allow_html=True)
    # Insert image here
    st.image("https://github.com/eeeeeedy/bankruptcy_prediction/blob/main/deployment/vanguard.jpg?raw=true", width=250)
elif page == 'EDA of Dataset':
    eda.run()
else:
    model.run()
