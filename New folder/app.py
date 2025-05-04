import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# --------- Page Configuration ---------
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide", page_icon="🔍")

# --------- Custom Styling ---------
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stTextInput>div>div>input {
        background-color: #1e1e1e;
        color: white;
        border-radius: 0.5rem;
        padding: 0.6rem;
    }
    </style>
""", unsafe_allow_html=True)

# --------- Sidebar ---------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1177/1177568.png", width=80)
    st.markdown("## 💡 How to Use")
    st.markdown("""
        1. Enter a **job role** or **assessment requirement**  
        2. View the **top matching assessments**  
        3. Click the link to explore more!  
    """)
    st.markdown("---")
    st.markdown("Created by **SHL Intern 🚀**")

# --------- App Title ---------
st.markdown("<h1 style='text-align: center;'>🔍 SHL Assessment Recommendation Engine</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Find the right assessment for the right role!</h4>", unsafe_allow_html=True)

# --------- Load the Dataset ---------
file_path = "assessment_data.pkl"

if not os.path.exists(file_path):
    st.error(f"❌ File not found: {file_path}")
    st.stop()

df = pd.read_pickle(file_path)

if 'embedding' not in df.columns:
    st.error("❌ Data format issue: 'embedding' column not found.")
    st.stop()

# --------- Load Sentence Transformer Model ---------
model = SentenceTransformer("all-MiniLM-L6-v2")

# --------- User Input ---------
user_query = st.text_input("💬 Enter a job role or assessment requirement:")

if user_query:
    with st.spinner("🔎 Searching for best matches..."):
        try:
            # Generate embedding for input
            query_embedding = model.encode([user_query])
            assessment_embeddings = np.vstack(df['embedding'].values)
            similarities = cosine_similarity(query_embedding, assessment_embeddings)[0]

            # Get top 5 matches
            top_indices = similarities.argsort()[::-1][:5]
            top_results = df.iloc[top_indices][['name', 'url', 'test_type', 'duration_minutes']].copy()
            top_results['similarity'] = similarities[top_indices]

            # --------- Show Results ---------
            st.subheader("🎯 Top Recommended Assessments")
            for i, row in top_results.iterrows():
                st.markdown(f"**{row['name']}**  \n"
                            f"🧪 Type: *{row['test_type']}*  | ⏱️ Duration: *{row['duration_minutes']} mins*")
                st.markdown(f"[👉 View Assessment]({row['url']})")
                st.progress(int(row['similarity'] * 100))
                st.write("---")

            # --------- Optional: Show Chart ---------
            st.subheader("📊 Similarity Score Chart")
            chart_data = top_results[['name', 'similarity']].set_index('name')
            st.bar_chart(chart_data)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
