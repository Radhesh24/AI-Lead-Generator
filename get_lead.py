import requests

def search_companies(industry=None, location=None, employee_count=None):
    """
    Call Apollo Mixed Company Search API and return company name, employee count, and website.

    Args:
        industry (str): Industry filter e.g. "Software"
        location (str): Location filter e.g. "San Francisco, CA"
        employee_count (str): Employee count range e.g. "50-200"

    Returns:
        list of dict: Each dict has "name", "employee_count", "website"
    """
    api_url = "https://api.apollo.io/v1/mixed_companies/search"  # Example endpoint
    headers = {
        "Authorization": "Bearer YOUR_APOLLO_API_KEY",
        "Content-Type": "application/json"
    }

    # Build payload with filters
    payload = {
        "industry": industry,
        "location": location,
        "employee_count": employee_count,
        "page": 1,
        "per_page": 10  # Adjust number of results per page
    }

    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []

    data = response.json()
    
    # Extract company details
    companies = []
    for company in data.get("companies", []):
        companies.append({
            "company_name": company.get("name"),
            "employee_count": company.get("employee_count"),
            "website": company.get("website")
        })
    
    return companies