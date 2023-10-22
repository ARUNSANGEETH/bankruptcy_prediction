import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from random import randint

def run():
    st.header("Welcome to EDA of the Dataset")
    st.markdown('Made by <a href="https://www.linkedin.com/in/edysetiawan/" target="_blank">Edy Setiawan</a>', unsafe_allow_html=True)

    st.header('Exploratory Data Analysis')

    try:
        # Load the data
        df = pd.read_csv('https://raw.githubusercontent.com/eeeeeedy/bankruptcy_prediction/main/Company_Bankruptcy_Prediction_dataset.csv')
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return
    # Remove leading and trailing whitespaces from column names
    df.columns = [col.strip() for col in df.columns]

    # Display a few rows from the dataset
    st.table(df.head(5))

    colors = ["Greys", "Reds", "Greens", "Blues", "Oranges", "Purples", "BuGn", "BuPu", "GnBu", "OrRd", "PuBu", "PuRd", "RdPu", "YlGn", "PuBuGn", "YlGnBu"]

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    # Distribution of Bankrupt class
    st.subheader('1. Distribusi Kelas Target (Bankrupt)')

    with st.expander("Lihat Plot"):
        fig1, ax1 = plt.subplots(figsize=(2,2))
        df['Bankrupt?'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, labels=['Tidak Bangkrut', 'Bangkrut'], ax=ax1, textprops={'fontsize': 5})
        ax1.set_title('Distribusi Kelas Target (Bankrupt)', fontsize=5)
        ax1.set_ylabel('')
        st.pyplot(fig1)
        st.write(df['Bankrupt?'].value_counts())

    # Distribution of 'Liability-Assets Flag'
    st.subheader('2. Distribusi dari "Liability-Assets Flag"')

    with st.expander("Lihat Plot"):
        fig2, ax2 = plt.subplots()
        df['Liability-Assets Flag'].value_counts().plot(kind='bar', ax=ax2)
        ax2.set_title('Distribusi Liability-Assets Flag')
        st.pyplot(fig2)
        st.write(df['Liability-Assets Flag'].value_counts())

        fig2b = sns.countplot(x='Liability-Assets Flag', hue='Bankrupt?', data=df, palette=colors[randint(0, len(colors)-1)])
        st.pyplot(fig2b.figure)

    # Distribution of 'Net Income Flag'
    st.subheader('3. Distribusi dari "Net Income Flag"')

    with st.expander("Lihat Plot"):
        fig3 = sns.countplot(x='Net Income Flag', hue='Bankrupt?', data=df, palette=colors[randint(0, len(colors)-1)])
        st.pyplot(fig3.figure)

    # Average Profit Margin Based on Bankruptcy
    st.subheader('4. Rata-Rata Margin Laba Berdasarkan Bankruptcy')

    with st.expander("Lihat Plot"):
        grouped_data_laba = df.groupby('Bankrupt?')[['Operating Gross Margin', 'Realized Sales Gross Margin']].mean()
        fig4 = grouped_data_laba.plot(kind='bar', figsize=(8, 4))
        plt.title('Rata-Rata Margin Laba Berdasarkan Bankruptcy')
        plt.ylabel('Rata-rata Margin Laba')
        st.pyplot(fig4.figure)
        st.write(grouped_data_laba)

    # Correlation between Liability and Equity
    st.subheader('5. Korelasi antara Liabilitas dan Ekuitas')

    with st.expander("Lihat Plot"):
        fig5 = plt.figure(figsize=(5, 3))
        sns.scatterplot(data=df, x='Liability to Equity', y='Equity to Liability')
        st.pyplot(fig5)

    # Positive and Negative correlation with 'Bankrupt'
    st.subheader('6. Analisis Top 5 atribut teratas yang berkorelasi positif dan negatif dengan "Bankrupt"')

    with st.expander("Lihat Plot"):
        def corrbargraph(x_value, y_value):
            fig = plt.figure(figsize=(15, 8))
            for i in range(5):
                plt.subplot(2, 3, i + 1)  
                sns.barplot(x=x_value, y=y_value[i], data=df, palette=colors[randint(0, len(colors)-1)])
            plt.tight_layout(pad=0.5)
            st.pyplot(fig)

        top_pos_corr = df[numeric_columns].corrwith(df["Bankrupt?"]).sort_values(ascending=False)[:5].index.tolist()
        top_neg_corr = df[numeric_columns].corrwith(df["Bankrupt?"]).sort_values()[:5].index.tolist()

        corrbargraph('Bankrupt?', top_pos_corr)
        corrbargraph('Bankrupt?', top_neg_corr)

    # Heatmap of correlations
    st.subheader('Heatmap of Correlations')

    with st.expander("Lihat Plot"):
        relation = top_pos_corr + top_neg_corr
        fig7 = plt.figure(figsize=(8, 7))
        sns.heatmap(df[relation].corr(), annot=True)
        st.pyplot(fig7)
        st.write(df[relation].corr())
