import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simulazione Albero Decisionale", layout="centered")
st.title("🌳 Simulazione Manuale di un Albero Decisionale")

st.markdown("""
Questa app simula passo passo il funzionamento di un albero decisionale su un piccolo dataset.

👉 **Obiettivo**: scegliere lo split migliore calcolando la *devianza within* e *devianza between*.
""")

# Mini dataset
df = pd.DataFrame({
    'media_voti': [18, 22, 24, 27, 30],
    'ore_studio': [5, 10, 15, 30, 35],
    'churned': [1, 1, 0, 0, 0]
})

st.subheader("📊 Dataset Semplificato")
st.dataframe(df)

# Funzioni devianza
def within_dev(group):
    y = group['churned']
    p = y.mean()
    return np.sum((y - p) ** 2)

def between_dev(part_A, part_B, p_tot):
    return len(part_A) * (part_A['churned'].mean() - p_tot)**2 + \
           len(part_B) * (part_B['churned'].mean() - p_tot)**2

# Selettore feature e soglia
st.subheader("✂️ Prova uno Split")
col1, col2 = st.columns(2)

with col1:
    feature = st.selectbox
