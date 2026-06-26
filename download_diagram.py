import base64
import zlib
import urllib.request

mermaid_code = """
flowchart TD
    classDef storage fill:#f8fafc,stroke:#cbd5e1,stroke-width:2px,color:#0f172a
    classDef process fill:#eff6ff,stroke:#93c5fd,stroke-width:2px,color:#1e3a8a
    classDef ml fill:#f5f3ff,stroke:#c4b5fd,stroke-width:2px,color:#4c1d95
    classDef ui fill:#ecfdf5,stroke:#6ee7b7,stroke-width:2px,color:#064e3b
    
    subgraph Layer_1 ["Data Storage & Ingestion Layer"]
        JSON[("sample_candidates.json\n(Raw Unstructured Data)")]:::storage
        Parser["candidates_df.py\n(Custom JSON Parser)"]:::storage
        CSV[("Relational CSVs\n(Education, Skills, etc.)")]:::storage
        
        JSON --> Parser
        Parser --> CSV
    end

    subgraph Layer_2 ["Processing & ETL Layer (Pandas/NumPy)"]
        Clean["data_cleaning.py\n(Normalize & Scrub)"]:::process
        Merge["f_merge.py\n(Relational Stitching)"]:::process
        FeatEng["feature_engineering.py\n(Metric Calculation)"]:::process
        MasterDB[("Master DataFrame\n(Optimized Cache)")]:::process
        
        CSV --> Clean
        Clean --> Merge
        Merge --> FeatEng
        FeatEng --> MasterDB
    end

    subgraph Layer_3 ["Machine Learning Layer (AI Engine)"]
        HF["Sentence-Transformers\n(all-MiniLM-L6-v2)"]:::ml
        HiddenTalent["hidden_talent_engine.py\n(Cosine Similarity Math)"]:::ml
        
        HF --> HiddenTalent
    end

    subgraph Layer_4 ["Presentation Layer (Frontend)"]
        Streamlit["app.py\n(Streamlit Dashboard)"]:::ui
        Theme["Dynamic CSS & Flexbox\n(Enterprise SaaS UX)"]:::ui
        
        Streamlit --- Theme
    end

    MasterDB -->|"Provides Clean Profiles"| Streamlit
    Streamlit -->|"Passes JD & Profile Texts"| HiddenTalent
    HiddenTalent -->|"Returns Match Scores"| Streamlit
"""

# Kroki requires the code to be zlib compressed and then base64 encoded
compressed = zlib.compress(mermaid_code.encode('utf-8'), 9)
encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')

url = f"https://kroki.io/mermaid/png/{encoded}"

print(f"Downloading from {url}...")
urllib.request.urlretrieve(url, "Talent_OS_Architecture.png")
print("Saved as Talent_OS_Architecture.png")
