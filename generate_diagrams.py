import base64, urllib.request, json, time

diagrams = {
    "Data_Pipeline_Diagram.png": """flowchart LR
    classDef raw fill:#fecaca,stroke:#dc2626,stroke-width:2px,color:#000;
    classDef clean fill:#fef08a,stroke:#ca8a04,stroke-width:2px,color:#000;
    classDef feat fill:#bbf7d0,stroke:#16a34a,stroke-width:2px,color:#000;
    classDef ml fill:#bfdbfe,stroke:#2563eb,stroke-width:2px,color:#000;

    Raw[(Raw CSV Data)]:::raw --> |load_data.py| Clean[Data Cleaning & Imputation]:::clean
    Clean --> |feature_engineering.py| Feat[Feature Engineering]:::feat
    
    Feat --> NumFeat[Numerical Features<br/>Experience, Skills]:::feat
    Feat --> TextFeat[Unstructured Text<br/>Summaries, Headlines]:::feat

    NumFeat --> |Random Forest| SalPredict[Salary Prediction]:::ml
    TextFeat --> |Sentence Transformers| Vector[Semantic Embeddings]:::ml
    
    Vector --> |Cosine Similarity| JDMatch[JD Match Score]:::ml
    SalPredict --> TalentScore
    JDMatch --> TalentScore[Composite Talent Score]:::ml
""",

    "Data_Schema_Diagram.png": """erDiagram
    CANDIDATES ||--o{ SKILLS : "possesses"
    CANDIDATES ||--o{ CAREER_HISTORY : "has"
    CANDIDATES ||--o{ EDUCATION : "completed"
    CANDIDATES ||--o{ CERTIFICATIONS : "achieved"
    CANDIDATES ||--o{ ASSESSMENTS : "takes"
    
    CANDIDATES {
        string candidate_id PK
        string name
        string headline
        float years_of_experience
    }
    SKILLS {
        string candidate_id FK
        string skill_name
        string proficiency
    }
    CAREER_HISTORY {
        string candidate_id FK
        string company_name
        string role
    }
    ASSESSMENTS {
        string candidate_id FK
        string assessment_name
        float score
    }
""",

    "User_Workflow_Diagram.png": """sequenceDiagram
    autonumber
    participant R as Recruiter
    participant UI as Presentation UI
    participant ML as AI Engine
    participant DB as master_df

    R->>UI: Pastes Job Description (JD)
    UI->>ML: Triggers Analysis (Send JD)
    ML->>ML: Generate JD Vector Embedding
    ML->>DB: Fetch Candidate Vectors
    DB-->>ML: Return 50+ Candidate Profiles
    ML->>ML: Compute Cosine Similarity
    ML->>ML: Aggregate Talent Score & Salary
    ML-->>UI: Return Ranked Candidate List
    UI-->>R: Displays Results (Glassmorphism List)
    R->>UI: Clicks "Score > 80" Filter
    UI-->>R: Updates instantly via Cache
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
