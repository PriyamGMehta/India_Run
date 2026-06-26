import base64, urllib.request, json
graph = """flowchart TD
    classDef head fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,font-weight:bold,color:#0f172a;
    classDef ui fill:#e0f2fe,stroke:#38bdf8,stroke-width:2px,color:#0f172a,rx:5,ry:5;
    classDef eng fill:#ecfdf5,stroke:#34d399,stroke-width:2px,color:#0f172a,rx:5,ry:5;
    classDef db fill:#f3e8ff,stroke:#c084fc,stroke-width:2px,color:#0f172a,rx:5,ry:5;

    Title["Talent Intelligence Platform Architecture"]:::head

    subgraph Presentation ["1. Presentation Layer (Frontend)"]
        UI["🔍 JD Match  |  🏆 Top Candidates  |  👤 Profile  |  📊 Dashboard"]:::ui
    end

    subgraph AppLayer ["2. Application Layer (Core Pipeline)"]
        direction LR
        Inp(["User Input"]):::eng --> Norm(["Normalization"]):::eng --> NLP["Semantic Vectorization"]:::eng
        NLP --> Cos["Cosine Similarity"]:::eng
        Cos --> Score["Talent Score Aggregation"]:::eng
        Norm --> Sal["Salary Regression"]:::eng
        Sal --> Score
    end

    subgraph DataLayer ["3. ML & Data Layer"]
        direction LR
        DF[("master_df (Local CSVs / Memory)")]:::db
        Models["NLP Transformers & Random Forest"]:::db
    end

    Title ~~~ Presentation
    Presentation <==> AppLayer
    AppLayer <==> DataLayer
    DF -.-> AppLayer
    Models -.-> AppLayer"""

# Using base64 encoding for Mermaid
encoded = base64.b64encode(graph.encode('utf-8')).decode('utf-8')
url = f"https://mermaid.ink/img/{encoded}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urllib.request.urlopen(req).read()

with open('Architecture_Diagram.png', 'wb') as f:
    f.write(data)

print('Saved PNG')
