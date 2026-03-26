# BeautyScout-
Personalized product recommender that fetches real reviews from Nykaa, Purplle, and Amazon, and shows the most representative review with a purchasability score
# 🌸 BeautyScout

**Personalized product recommender that fetches real reviews from Nykaa, Purplle, and Amazon, and shows the most representative review with a purchasability score.**

## 🚀 What It Does
- Asks you about your skin type, concerns, and budget
- Finds 2–3 products that best match your profile
- Fetches real reviews from Nykaa, Purplle, and Amazon (in real time)
- Analyzes sentiment to find the **most representative review** (not just the most positive)
- Gives you a **purchasability score (1–10)** to help you decide

## 📊 How It Works
1. **User input** – category, skin type, concerns, budget
2. **Product matching** – uses cosine similarity to match your needs with product attributes
3. **Review scraping** – collects reviews from Nykaa, Purplle, and Amazon (using BeautifulSoup)
4. **Sentiment analysis** – uses TextBlob to assign polarity scores
5. **Output** – shows top recommendations with:
   - Product details (name, brand, price, rating)
   - Overall purchasability score
   - Summary of pros and cons from real users
   - The “optimum” review (closest to average sentiment)
   - Direct purchase links

## 🛠️ Tech Stack
- Python
- BeautifulSoup (web scraping)
- TextBlob (sentiment analysis)
- Scikit-learn (cosine similarity matching)
- Pandas / NumPy (data handling)
- Matplotlib / Seaborn (visualization, optional)

## 🧪 How to Run
1. **Open in Google Colab** – [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shivangisinha828-beep/BeautyScout/blob/main/BEAUTYSCOUT.ipynb)
   (Replace the link with your actual notebook URL after you push changes.)
2. Run all cells.
3. Answer the questions about your skin type, concerns, and budget.
4. Wait a few seconds while the system fetches real reviews.
5. See your personalized recommendations with actual user reviews!

## 📌 Example Output
*(Add a screenshot here after you run the notebook)*

## 📁 Files
- `BEAUTYSCOUT.ipynb` – main notebook with all code
- `requirements.txt` – Python dependencies (coming soon)

## ⚠️ Notes
- Web scraping is for educational purposes only. Respect website terms of service.
- The scrapers may break if the target websites change their HTML structure. You can adjust the selectors as needed.

## 🔮 Future Improvements
- Add support for Tira, Myntra, Flipkart
- Extract ingredient lists and compare against user allergies
- Build a Chrome extension for one-click analysis
- Train a custom sentiment model for better accuracy

## 👩‍💻 Author
**Shivangi Sinha** – [GitHub](https://github.com/shivangisinha828-beep)

## 📄 License
MIT
