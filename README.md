# Lead Generation Pipeline

An automated B2B lead generation system that identifies potential clients, scrapes their website insights, and generates personalized outreach messages using AI.

## Overview

This project automates the lead generation process by:
1. Searching for companies based on industry, location, and size criteria
2. Scraping website content to gather company insights
3. Generating personalized B2B outreach messages using AI (Groq LLM)
4. Exporting results to CSV format

## Features

- **Company Search**: Integration with Apollo.io API for targeted company discovery
- **Web Scraping**: Automated extraction of website metadata (title, description, headings)
- **AI-Powered Messaging**: Personalized outreach message generation using Groq's LLaMA 3.1 model
- **CSV Export**: Structured output with company details, insights, and personalized messages

## Project Structure

```
Wednesday_Assignment/
├── leadgen.py          # Main pipeline orchestrator
├── get_lead.py         # Apollo API integration for company search
├── scraper.py          # Website scraping functionality
├── ai_generator.py     # AI message generation using Groq
├── config.py           # Configuration and mock data
└── leads.csv           # Output file with generated leads
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Wednesday_Assignment
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install requests beautifulsoup4 groq
```

## Configuration

Update `config.py` with your API keys and search criteria:

```python
# API Keys
GROQ_API_KEY = "your_groq_api_key"
APOLLO_API_KEY = "your_apollo_api_key"

# Search Criteria
SEARCH_CRITERIA = {
    "industry": "software",
    "company_size": "50-200",
    "location": "India"
}
```

## Usage

Run the lead generation pipeline:

```bash
python leadgen.py
```

The script will:
1. Search for companies matching your criteria
2. Process each lead by scraping their website
3. Generate personalized outreach messages
4. Save results to `leads.csv`

## Important Notes

### Apollo API Limitation
**Note**: The Apollo.io API restricts usage of the `mixed_companies/search` endpoint for free tier accounts. Due to this limitation, the project currently uses **MOCK_LEADS** (defined in `config.py`) to demonstrate functionality.

To use real Apollo API data:
1. Upgrade to a paid Apollo.io plan
2. Update your API key in `config.py`
3. Uncomment the Apollo API code in `leadgen.py` (lines 16-35)
4. Comment out the mock leads section (lines 39-55)

### Mock Leads
The current implementation uses 5 sample Indian software companies:
- Vibeosys Software Pvt Ltd
- Wide Softech Pvt Ltd
- Equations Work It Services Pvt. Ltd
- Prometteur Solutions Pvt Ltd
- Teqrox Solutions LLP

## Output Format

The generated `leads.csv` contains:
- `company_name`: Company name
- `website`: Company website URL
- `employee_count`: Number of employees
- `insights`: Scraped website metadata (title, description, headings)
- `personalized_message`: AI-generated outreach message

## Technologies Used

- **Python 3.x**: Core programming language
- **Apollo.io API**: Company search and discovery
- **Groq API**: AI-powered message generation (LLaMA 3.1-8B model)
- **BeautifulSoup4**: Web scraping
- **Requests**: HTTP requests

## Development

This project was developed with assistance from **ChatGPT** for code structure, API integration guidance, and best practices implementation.

## Future Enhancements

- Add command-line arguments for dynamic search criteria
- Implement email sending automation
- Add support for multiple LLM providers
- Include lead scoring/prioritization
- Add database storage for lead management
- Implement rate limiting and retry logic

