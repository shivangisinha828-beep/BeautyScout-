import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
import random

# ---------- This MUST be the first Streamlit command ----------
st.set_page_config(page_title="BeautyScout", layout="wide")

# ---------- Load your product data (replace with your real data) ----------
@st.cache_data
def load_products():
    data = {
        'product_name': ['CeraVe Hydrating Cleanser', 'Neutrogena Hydro Boost Gel'],
        'brand': ['CeraVe', 'Neutrogena'],
        'category': ['cleanser', 'moisturizer'],
        'skin_type': ['dry', 'combination'],
        'concerns': ['hydration', 'hydration'],
        'price': [1450, 550],
        'rating': [4.6, 4.4],
        'url_nykaa': ['https://www.nykaa.com/...', 'https://www.nykaa.com/...'],
        'url_amazon': ['https://amazon.in/...', 'https://amazon.in/...']
    }
    return pd.DataFrame(data)

df = load_products()

# ---------- Build recommendation vectors ----------
@st.cache_resource
def build_vectors():
    product_texts = df.apply(lambda row: f"{row['brand']} {row['category']} {row['skin_type']} {row['concerns']}", axis=1)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(product_texts)
    return vectorizer, vectors

vectorizer, product_vectors = build_vectors()

def recommend_products(user_prefs, top_n=3):
    filtered = df[
        (df['category'] == user_prefs['category']) &
        (df['price'] >= user_prefs['min_budget']) &
        (df['price'] <= user_prefs['max_budget'])
    ].copy()
    if filtered.empty:
        return pd.DataFrame()
    user_text = f"{user_prefs['category']} {user_prefs['skin_type']} {' '.join(user_prefs['concerns'])}"
    user_vec = vectorizer.transform([user_text])
    idxs = filtered.index.tolist()
    filtered_vectors = product_vectors[idxs]
    similarities = cosine_similarity(user_vec, filtered_vectors).flatten()
    filtered['similarity'] = similarities
    filtered['score'] = (similarities * 0.6 + (filtered['rating'] / 5) * 0.4) * 10
    recommended = filtered.nlargest(top_n, 'score')
    return recommended[['product_name', 'brand', 'price', 'rating', 'score', 'url_nykaa', 'url_amazon']]

# ---------- Streamlit UI ----------
st.title("🌸 BeautyScout")
st.markdown("Find your perfect product with real reviews from Nykaa, Purplle, and Amazon.")

st.sidebar.header("Your Preferences")
category = st.sidebar.selectbox("Category", ["cleanser", "moisturizer", "serum", "sunscreen", "haircare"])
skin_type = st.sidebar.selectbox("Skin Type", ["dry", "oily", "combination", "all"])
concerns = st.sidebar.multiselect("Concerns", ["acne", "hydration", "brightening", "aging", "dryness", "sensitive", "oil_control"])
min_budget = st.sidebar.number_input("Min Budget (₹)", min_value=0, value=0, step=100)
max_budget = st.sidebar.number_input("Max Budget (₹)", min_value=0, value=5000, step=100)

if st.sidebar.button("Find My Match"):
    with st.spinner("Finding the best products for you..."):
        user_prefs = {
            'category': category,
            'skin_type': skin_type,
            'concerns': concerns,
            'min_budget': min_budget,
            'max_budget': max_budget
        }
        recs = recommend_products(user_prefs)
        if recs.empty:
            st.warning("No products match your criteria. Try adjusting your budget or concerns.")
        else:
            for _, prod in recs.iterrows():
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.subheader(f"{prod['product_name']} by {prod['brand']}")
                        st.write(f"**Price:** ₹{prod['price']}")
                        st.write(f"**Rating:** {prod['rating']}/5")
                        st.write(f"**Match Score:** {prod['score']:.1f}/10")
                    with col2:
                        st.write("**Buy at:**")
                        if pd.notna(prod.get('url_nykaa')):
                            st.write(f"[Nykaa]({prod['url_nykaa']})")
                        if pd.notna(prod.get('url_amazon')):
                            st.write(f"[Amazon]({prod['url_amazon']})")
                with st.expander("See real reviews from the web"):
                    st.write("Reviews will be fetched from Nykaa, Purplle, Amazon...")
                st.divider()