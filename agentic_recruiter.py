import random
import os

def generate_outreach_email(candidate_name, score, experience, salary, job_desc, tone="Professional", focus="Balanced"):
    """
    Generates a highly personalized, context-aware cold outreach email.
    If OPENAI_API_KEY is found, it could use the OpenAI API.
    Otherwise, it uses a deterministic NLP engine to mock the LLM output perfectly.
    """
    
    # Optional: If you ever want to connect this to real OpenAI, 
    # you would un-comment the lines below and install the openai package.
    # 
    # if os.getenv("OPENAI_API_KEY"):
    #     import openai
    #     openai.api_key = os.getenv("OPENAI_API_KEY")
    #     prompt = f"Write a {tone} cold recruiting email to {candidate_name} focusing on {focus}..."
    #     response = openai.ChatCompletion.create(...)
    #     return response.choices[0].message.content

    jd_lower = str(job_desc).lower()
    
    key_tech = []
    if "python" in jd_lower: key_tech.append("Python")
    if "machine learning" in jd_lower or "ml" in jd_lower: key_tech.append("Machine Learning")
    if "data" in jd_lower: key_tech.append("Data Engineering")
    if "react" in jd_lower: key_tech.append("React")
    if "cloud" in jd_lower or "aws" in jd_lower: key_tech.append("Cloud Architecture")
        
    tech_stack_str = "our core platform"
    if key_tech:
        tech_stack_str = f"our upcoming initiatives involving {', '.join(key_tech)}"

    name_first = candidate_name.split()[0] if candidate_name != 'Unknown' else 'there'

    # --- TONE LOGIC ---
    if tone == "Professional":
        subject = "Exploring a potential fit for a Senior Engineering role"
        greeting = f"Hi {name_first},"
        opener = "I hope this email finds you well. Your background recently stood out to our engineering leadership team."
        closing = "Are you open to a brief, exploratory introductory call later this week?\n\nBest regards,\nTalent Acquisition Team"
    elif tone == "Casual":
        subject = f"Quick question about your background, {name_first} 👋"
        greeting = f"Hey {name_first},"
        opener = "I'll keep this short. I came across your profile and was genuinely impressed by your trajectory."
        closing = "Would you be down for a quick 10-minute virtual coffee this week?\n\nCheers,\nTalent Team"
    elif tone == "Direct / Aggressive":
        subject = f"{name_first} - Senior Engineering Opportunity"
        greeting = f"Hi {name_first},"
        opener = "We are actively recruiting top-tier engineering talent and your profile is an exact match for what we need."
        closing = "Let me know when you have 15 minutes to speak tomorrow or Thursday.\n\nBest,\nTalent Acquisition"
    else:
        subject = "Reaching out regarding a Senior Engineering Role"
        greeting = f"Hi {name_first},"
        opener = "Your background instantly stood out to our engineering team."
        closing = "Are you open to a quick introductory call later this week?\n\nBest regards,\nTalent Acquisition Team"

    # --- FOCUS LOGIC ---
    if focus == "Salary / Compensation":
        focus_block = f"Based on our market calibration models, we know exactly what it takes to pull top talent. We are prepared to offer highly competitive compensation aligned with your expectations (in the ₹{salary}L range), alongside significant equity."
    elif focus == "Tech Stack / Challenges":
        focus_block = f"We are currently tackling some of the hardest problems in the industry and would love to get your specific thoughts on {tech_stack_str}. We need engineers who want to build, not just maintain."
    elif focus == "Company Culture":
        focus_block = f"Beyond the technical challenges, we pride ourselves on a culture of extreme autonomy and fast shipping. You would be joining a team of incredibly smart, driven engineers who love what they do."
    else:
        focus_block = f"We are currently scaling our platform and would love to get your thoughts on {tech_stack_str}. Furthermore, we are prepared to offer compensation aligned with your expectations (in the ₹{salary}L range)."

    # Construct the final email
    email_body = f"""Subject: {subject}

{greeting}

{opener}

Our Talent Intelligence Engine actually flagged your profile as a highly unique {score}% semantic match for an open role we are actively hiring for. Given your {experience} years of experience, we believe you could come in and immediately drive technical strategy.

{focus_block}

I know you are likely happily employed, but I'd love to chat—no pressure to interview.

{closing}
"""

    return email_body
