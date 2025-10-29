# Step 1: Import required modules
import requests
import time
import urllib.robotparser
from urllib.parse import urlparse
from datetime import datetime

# Step 2: Define a logger function for consistent output
def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{level}] {timestamp} - {message}")

# Step 3: Check robots.txt to see if scraping is allowed
def is_scraping_allowed(url, user_agent="*"):
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    log(f"Checking robots.txt at {robots_url}")

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)

    try:
        rp.read()
        allowed = rp.can_fetch(user_agent, url)
        return allowed
    except Exception as e:
        log(f"Failed to read robots.txt: {e}", level="ERROR")
        return False

# Step 4: Fetch the page content with error handling and rate limiting
def fetch_page(url, delay=2, timeout=10):
    log(f"Waiting {delay} seconds before request to respect rate limits")
    time.sleep(delay)

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        log("Request timed out.", level="ERROR")
    except requests.exceptions.HTTPError as e:
        log(f"HTTP error: {e}", level="ERROR")
    except requests.exceptions.RequestException as e:
        log(f"Network error: {e}", level="ERROR")
    return None

# Step 5: Save content to a file
def save_content(content, filename="output.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"Content saved to {filename}")
    except Exception as e:
        log(f"Failed to save content: {e}", level="ERROR")

# Step 6: Main function to orchestrate scraping
def scrape_website(url):
    log(f"Starting scrape for {url}")

    # Check robots.txt
    if not is_scraping_allowed(url):
        log("Scraping not permitted by robots.txt.", level="DENIED")
        return

    log("Scraping permitted. Fetching page...", level="ALLOWED")

    # Fetch page content
    content = fetch_page(url)
    if content:
        size = len(content.encode('utf-8'))
        log(f"Successfully fetched {url} ({size} bytes)", level="SUCCESS")
        save_content(content)
    else:
        log("Failed to fetch content.", level="ERROR")

# Step 7: Run the scraper with your target URL
if __name__ == "__main__":
    target_url = "https://example.com"
    scrape_website(target_url)
