# Google Rank Checker (Serper API)

This tool checks Google search rankings (Top 100 results) for keywords and domains using the Serper API.

---

## 🚀 How to Use

1. Install dependencies:
pip install requests python-dotenv

---

2. Create a `.env` file in the project root:

SERPER_API_KEY=your_api_key_here

---

3. Prepare your CSV file

File name:
input.csv

---

### 📊 CSV Format

Your CSV must follow this exact structure:


---

### 📝 Rules

- First row must be headers: `keyword,domain`
- Do not change column names
- You can provide:
  - domain only → `example.com`
  - full URL → `https://example.com`
- One keyword per row

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

- Type `y` to print all results in console
- Useful for troubleshooting

---

7. Output

Results will be saved in:
output.csv

Format:


---

## 🔑 How to Get API Key

1. Go to: https://serper.dev  
2. Sign up or log in  
3. Copy your API key  
4. Paste it into `.env` file  

---

## ⚠️ Important Notes

- Results are based on non-personalized Google search
- Rankings may differ from your local search
- Country selection affects results

---

## 📂 Project Structure

---

## ✅ Features

- Top 100 Google results tracking
- Country-based search
- Supports domain and full URL input
- Debug mode for visibility
- CSV input/output system

---