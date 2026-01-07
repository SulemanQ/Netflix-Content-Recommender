import os
import sys

# --- AUTO-INSTALL DEPENDENCIES ---
# This ensures the script works even if you haven't run pip yet
try:
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
except ImportError:
    print("Missing dependencies. Installing now...")
    os.system(f"{sys.executable} -m pip install pandas scikit-learn")
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel

# --- CONFIGURATION ---
DATA_PATH = r"C:\Users\Sulem\OneDrive\Desktop\Fahad\Projects\The Netflix Matchmaker\netflix_titles.csv"

def load_and_clean_data():
    """Load the Netflix dataset and clean missing values"""
    if not os.path.exists(DATA_PATH):
        print(f"Error: File not found at {DATA_PATH}")
        return None
    
    df = pd.read_csv(DATA_PATH)
    # Removing titles without descriptions as they can't be analyzed
    df = df.dropna(subset=['description']).reset_index(drop=True)
    return df

def build_recommendation_engine(df):
    """Initialize the NLP engine using TF-IDF and Cosine Similarity"""
    print("Initializing NLP Engine...")
    
    # Transform text descriptions into mathematical vectors
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    
    # Calculate similarity scores between all titles
    similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    return similarity_matrix

def main():
    df = load_and_clean_data()
    if df is None: return

    sim_matrix = build_recommendation_engine(df)
    
    # Create lookup table for titles
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()

    print("\n" + "="*30)
    print("  NETFLIX MATCHMAKER ACTIVE")
    print("="*30)
    
    while True:
        query = input("\nEnter a Movie or TV Show: ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            break
            
        if query not in indices:
            # Simple search if title isn't exact
            matches = [t for t in indices.index if query.lower() in str(t).lower()]
            if matches:
                print(f"Showing results for: '{matches[0]}'")
                query = matches[0]
            else:
                print("Title not found. Try 'Blood & Water' or 'Zombieland'.")
                continue

        # Get top 5 recommendations
        idx = indices[query]
        scores = list(enumerate(sim_matrix[idx]))
        top_matches = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
        
        print(f"\nRecommended for fans of '{query}':")
        for i, (m_idx, score) in enumerate(top_matches, 1):
            print(f"{i}. {df['title'].iloc[m_idx]}")

if __name__ == "__main__":
    main()