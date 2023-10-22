import streamlit as st
import pandas as pd
import pickle
import numpy as np

def run():
    st.header("Model Prediksi Kebangkrutan")

    # Load the saved models and transformers
    with open('deployment/best_rf_pipeline.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Get user input
    columns = [
        'Current Liability to Current Assets',
        'Liability-Assets Flag',
        'Total expense/Assets',
        'Cash/Current Liability',
        'Fixed Assets Turnover Frequency',
        'Fixed Assets to Assets',
        'Net Value Growth Rate',
        'Revenue per person',
        'Total assets to GNP price',
        'Quick Asset Turnover Rate',
        'Tax rate (A)',
        'Cash/Total Assets'
    ]

    min_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    max_values = [1, 1, 1, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 10000000000, 1, 1]
    
    input_data = {}

    for column, min_val, max_val in zip(columns, min_values, max_values):
        # Check if the column is 'Liability-Assets Flag' to provide option selector
        if column == 'Liability-Assets Flag':
            value = st.selectbox(label=f'Please select {column} (options: {min_val} or {max_val})', options=[0, 1])
        else:
            value = st.number_input(label=f'Please enter {column} (min: {float(min_val)}, max: {float(max_val)})', 
                                    min_value=float(min_val), 
                                    max_value=float(max_val), 
                                    value=0.0,  # set default value as float
                                    format="%.2f", 
                                    key=column)
        input_data[column] = [value]

    data_inf = pd.DataFrame(input_data)

    # Display the input DataFrame
    st.table(data_inf)
    
    # On 'predict' button click
    if st.button(label='Predict'):
        # Perform prediction
        y_pred_inf = loaded_model.predict(data_inf)

        # Display the prediction
        st.write("Prediction: ", y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Perusahaan tidak ada kemungkinan akan BANKRUPT')
        else:
            st.write('Perusahaan kemungkinan akan BANKRUPT')
