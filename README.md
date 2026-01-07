# 🎬 Netflix Recommendation Engine (Content-Based)

## 📌 Project Overview
I developed this recommendation system to mimic Netflix's core "Suggestions" algorithm. By processing movie and TV show descriptions, the system calculates the mathematical similarity between titles to suggest relevant content to users.

This project demonstrates my ability to handle unstructured text data and implement Machine Learning concepts like Vectorization and Similarity Metrics.

## 🛠️ Technical Workflow
1. **Data Ingestion:** Processed a catalog of 8,800+ Netflix titles.
2. **Text Processing:** Used **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert plot summaries into numerical vectors. This allows the system to prioritize unique keywords while ignoring common English stop words.
3. **Similarity Calculation:** Implemented **Cosine Similarity** to measure the distance between vectors. The closer two vectors are in high-dimensional space, the more similar the content.
4. **Fuzzy Search:** Built a search handler to manage partial user inputs or typos.



## 🚀 Key Skills
- **Language:** Python
- **Libraries:** Pandas, Scikit-Learn
- **NLP Techniques:** Vectorization, Stop-word removal
- **Mathematics:** Linear Algebra (Cosine Similarity)

## 📊 Sample Output
The engine provides highly relevant recommendations. For example:

**User Input:** `Zombieland`
1. True to the Game
2. The Last Kids on Earth
3. Rust Creek
4. Submission
5. The Bridge Curse

## ⚙️ How to Run
1. Ensure you have the dataset `netflix_titles.csv` in the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
