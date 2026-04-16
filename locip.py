import csv
import requests
import time
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPER_API_KEY")

if not API_KEY:
    raise ValueError("❌ SERPER_API_KEY not found in .env file")

# 🔍 Normalize domain (handles full URLs, www, etc.)
def extract_domain(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url  # handle plain domains

        domain = urlparse(url).netloc.lower()
        domain = domain.replace("www.", "")
        return domain
    except:
        return ""


# 🔍 Rank checker
def get_rank(keyword, domain, country, debug=False):
    url = "https://google.serper.dev/search"

    payload = {
        "q": keyword,
        "gl": country,
        "hl": "en",
        "num": 100
    }

    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    results = data.get("organic", [])

    # ✅ Proper normalization
    target_domain = extract_domain(domain)

    for i, result in enumerate(results, start=1):
        link = result.get("link", "")
        result_domain = extract_domain(link)

        if debug:
            print(f"{i}. {result_domain} → {link}")

        # ✅ Smart matching
        if target_domain == result_domain or target_domain in result_domain:
            return i

    return None


# 🌍 Country selector
def select_country():
    print("\n🌍 Select Country:")
    print("1. USA")
    print("2. Canada")
    print("3. India")
    print("4. Australia")
    print("5. UK")

    choice = input("Enter choice (1-5): ")

    country_map = {
        "1": "us",
        "2": "ca",
        "3": "in",
        "4": "au",
        "5": "uk"
    }

    return country_map.get(choice, "us")


# 📂 Files
input_file = "input.csv"
output_file = "output.csv"


# 🚀 Main
def main():
    country = select_country()

    debug_mode = input("\nEnable debug mode? (y/n): ").lower() == "y"

    with open(input_file, newline='', encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    with open(output_file, "w", newline='', encoding="utf-8") as outfile:
        fieldnames = ["keyword", "domain", "country", "rank"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            keyword = row["keyword"]
            domain = row["domain"]

            print(f"\n🔎 Checking: {keyword}")

            try:
                rank = get_rank(keyword, domain, country, debug=debug_mode)
            except Exception as e:
                print(f"⚠️ Error: {e}")
                rank = None

            writer.writerow({
                "keyword": keyword,
                "domain": domain,
                "country": country,
                "rank": rank if rank else "Not Found"
            })

            print(f"✅ Rank: {rank if rank else 'Not Found'}")

            time.sleep(1)  # safe API delay

    print("\n🎉 Done! Results saved to output.csv")


if __name__ == "__main__":
    main()