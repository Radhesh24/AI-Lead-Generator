from groq import Groq
from config import GROQ_API_KEY, SEARCH_CRITERIA

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_message(company_name, employee_count, insights, industry=SEARCH_CRITERIA["industry"]):
    """Generate a personalized outreach message using Groq API."""
    prompt = f"""
    Write a short, professional B2B outreach message for {company_name}.
    
    Context:
    - Industry: {industry}
    - Employees: {employee_count}
    - Insights from website: {insights}
    
    Position yourself as a hardware computer store offering tailored solutions.
    Keep it under 120 words.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # fast + good for this use case
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating message: {e}"
