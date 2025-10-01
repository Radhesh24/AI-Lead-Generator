# ============ CONFIG FILE ============

# Groq API Key
GROQ_API_KEY = "GROQ_API_KEY"
APOLLO_API_KEY = "APOLLO_API_KEY"

# Search criteria (can be modified or later replaced by argparse)
SEARCH_CRITERIA = {
    "industry": "software",
    "company_size": "50-200",
    "location": "India"
}

# Mock Apollo/Lead Gen API response (replace with real API later)
MOCK_LEADS = [
    {"company_name": "Vibeosys Software Pvt Ltd", "website": "https://www.vibeosys.com", "employee_count": 30},  
    {"company_name": "Wide Softech Pvt Ltd", "website": "https://widesoftech.com/", "employee_count": 25},  
    {"company_name": "Equations Work It Services Pvt. Ltd", "website": "https://www.eqw.ai", "employee_count": 40},  
    {"company_name": "Prometteur Solutions Pvt Ltd", "website": "https://prometteursolutions.com/", "employee_count": 35},  
    {"company_name": "Teqrox Solutions LLP", "website": "https://www.teqrox.com", "employee_count": 22}
]

