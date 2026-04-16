# Google Rank Checker (Serper API आधारित)

This tool checks Google rankings (Top 100 results) for given keywords and domains using the Serper API.

---

## 🚀 How to Use

1. Install dependencies:
pip install -r requirements.txt

OR manually:
pip install requests python-dotenv

---

2. Create a `.env` file in the project root:

SERPER_API_KEY=your_api_key_here

---

3. Prepare your CSV file

File name:
input.csv

Format:
keyword,domain
Patient Monitoring App for Schools,https://doctodoor.com/
Remote Patient Monitoring Software,cmspricer.com

Notes:
- You can use full URLs OR just domain names
- Script will automatically normalize them

---

4. Run the script:

python locip.py

---

5. Select country when prompted

Example:
1 → USA
2 → Canada
3 → India
4 → Australia
5 → UK

---

6. (Optional) Enable debug mode

- Type "y" to see all 100 results in console
- Helps verify ranking issues

---

7. Output

Results will be saved in:
output.csv

Format:
keyword,domain,country,rank

---

## 🔑 How to Get API Key

1. Go to:
https://serper.dev

2. Sign up / Login

3. Copy your API key

4. Paste it inside `.env` file:
SERPER_API_KEY=your_key_here

---

## ⚠️ Important Notes

- Rankings may differ from your personal Google search
- Google personalizes results based on location, history, and login
- This tool uses a neutral (non-personalized) SERP

---

## 📂 Project Structure

.
├── locip.py
├── input.csv
├── output.csv (generated)
├── .env
├── .gitignore
└── README.md

---

## ✅ Features

- Checks Top 100 Google results
- Supports multiple countries
- Works with domains and full URLs
- Debug mode for verification
- Clean CSV input/output

---

