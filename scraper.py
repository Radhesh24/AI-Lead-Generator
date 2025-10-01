import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrape title, meta description, and first h1 tag from a website."""
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")

        title = soup.title.string.strip() if soup.title else ""
        meta_desc = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta and meta.get("content"):
            meta_desc = meta["content"].strip()

        h1 = soup.find("h1").get_text(strip=True) if soup.find("h1") else ""

        insights = [t for t in [title, meta_desc, h1] if t]
        return insights[:10]  # return insights
    except Exception as e:
        return [f"Could not scrape ({e})"]
