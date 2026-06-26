import base64, urllib.request, json, time

diagrams = {
    "Semantic_Matching_Diagram.png": """flowchart TD
    classDef input fill:#fef08a,stroke:#ca8a04,stroke-width:2px,color:#000;
    classDef model fill:#bfdbfe,stroke:#2563eb,stroke-width:2px,color:#000;
    classDef calc fill:#bbf7d0,stroke:#16a34a,stroke-width:2px,color:#000;

    JD[Job Description Text]:::input --> Tokenizer[NLP Tokenization & Cleaning]:::model
    Cand[Candidate Profile Text]:::input --> Tokenizer
    
    Tokenizer --> Transformer[Sentence Transformer Model]:::model
    
    Transformer --> Vec1[JD Vector Embedding<br/>384 Dimensions]:::calc
    Transformer --> Vec2[Candidate Vector Embedding<br/>384 Dimensions]:::calc
    
    Vec1 --> Cosine[Cosine Similarity Algorithm]:::calc
    Vec2 --> Cosine
    
    Cosine --> Score[Semantic Match Percentage %]:::input
""",

    "Talent_Score_Calculation.png": """flowchart TD
    classDef metric fill:#fecaca,stroke:#dc2626,stroke-width:2px,color:#000;
    classDef agg fill:#bfdbfe,stroke:#2563eb,stroke-width:2px,color:#000;
    classDef out fill:#bbf7d0,stroke:#16a34a,stroke-width:2px,color:#000;

    S1[Semantic Match Score<br/>Weight: 50%]:::metric --> Aggregator{Weighted<br/>Talent Scoring<br/>Algorithm}:::agg
    S2[Learning Velocity<br/>Weight: 20%]:::metric --> Aggregator
    S3[Technical Assessments<br/>Weight: 20%]:::metric --> Aggregator
    S4[Experience Level<br/>Weight: 10%]:::metric --> Aggregator
    
    Aggregator --> Output[Final Talent Score<br/>0 - 100]:::out
"""
}

for filename, graph in diagrams.items():
    print(f"Fetching {filename}...")
    encoded = base64.b64encode(graph.encode('utf-8')).decode('utf-8')
    url = f"https://mermaid.ink/img/{encoded}?type=png&bgColor=!white"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = urllib.request.urlopen(req).read()
        with open(filename, 'wb') as f:
            f.write(data)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Failed to generate {filename}: {e}")
    time.sleep(1) # Be nice to the API
