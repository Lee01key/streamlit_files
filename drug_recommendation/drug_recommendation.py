import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity
import streamlit as st

df = pd.read_csv('../data/cleaned/cleaned_df.csv')

df.dropna(inplace = True)

sat_df = df[['drug', 'satisfaction', 'reviewer']]

pivot = pd.pivot_table(sat_df, index='drug', columns='reviewer', values='satisfaction')

sparse_pivot = sparse.csr_matrix(pivot.fillna(0))

dists = pairwise_distances(sparse_pivot, metric='cosine')

similarities = cosine_similarity(sparse_pivot)

recommender_df = pd.DataFrame(dists, 
                              columns=pivot.index, 
                              index=pivot.index)

#get drug name
def name_of_drug(drug):
    return drug

#get drug satisfiaction
def satisfaction_drug(drug):
    satisfaction = pivot.loc[drug, :].mean()
    return satisfaction

def number_of_drug_review(drug):
    number_of_drug_review = pivot.T[drug].count()
    return number_of_drug_review

def recommended_drug(drug):
    recommended = pd.DataFrame(recommender_df[drug].sort_values()[1:6]).reset_index()
    drug_name_recommended = recommended['drug']
    return drug_name_recommended

drug_inq = st.text_input(f'Hi, what drugs are you currently taking?:', 'Afrezza inhalation')

st.image('./drug_image/'+drug_inq+'.jpeg')

st.write(f'💊 You are currently taking {name_of_drug(drug_inq)}.')
st.write(f'📝 In our system, {number_of_drug_review(drug_inq)} users also treid this medication and left reviews.')
st.write(f'❤️ Average satisfaction of users taking this drug was {round(satisfaction_drug(drug_inq),2)}/5.')
st.write(' ✅ Considering alternative drugs due to side effects? People with same gender, age, treatment period also considered medication below.')
st.write(recommended_drug(drug_inq))

