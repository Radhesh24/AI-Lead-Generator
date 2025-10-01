import csv
from get_lead import search_companies
from config import SEARCH_CRITERIA, MOCK_LEADS
from scraper import scrape_website
from ai_generator import generate_message

def main():
    results = []
    
    print("🔎 Starting Lead Generation Pipeline...\n")

    industry = SEARCH_CRITERIA["industry"]
    location = SEARCH_CRITERIA["location"]
    emp_count = SEARCH_CRITERIA["company_size"]

    # leads = search_companies(industry= industry, location= location, employee_count= emp_count)


    # for lead in leads:
    #     print(f"➡ Processing {lead['company_name']} ({lead['website']})")
        
    #     # Step 1: Scrape website
    #     insights = scrape_website(lead["website"])
        
    #     # Step 2: Generate outreach message
    #     message = generate_message(
    #         lead["company_name"],
    #         lead["employee_count"],
    #         insights,
    #         industry
    #     )
        
    #     lead["insights"] = insights
    #     lead["personalized_message"] = message
    #     results.append(lead)



    for lead in MOCK_LEADS:
        print(f"➡ Processing {lead['company_name']} ({lead['website']})")
        
        # Step 1: Scrape website
        insights = scrape_website(lead["website"])
        
        # Step 2: Generate outreach message
        message = generate_message(
            lead["company_name"],
            lead["employee_count"],
            insights,
            industry
        )
        
        lead["insights"] = insights
        lead["personalized_message"] = message
        results.append(lead)

    
    # Step 3: Save results
    with open("leads.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["company_name", "website", "employee_count", "insights", "personalized_message"])
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    
    print("\n✅ Lead generation completed. Results saved to leads.csv")

if __name__ == "__main__":
    main()
