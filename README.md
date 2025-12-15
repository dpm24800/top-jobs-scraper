# **Merojob Top Jobs Scraper**

Automated Python scraper that extracts **Top Jobs** listings from **Merojob.com** and exports them into CSV file.
This tool helps developers, data analysts, and job seekers collect fresh job listings programmatically.

---

## ⭐ **Features**
* Scrapes **Top Jobs** from Merojob.com
* Uses **Python + Requests / Selenium (your choice)**
* Exports data to:
  * ✔ CSV
  * ✔ JSON
  * ✔ Google Sheets
* Handles pagination (if available)
* Automatically cleans and structures job data
* Built for automation (Cron, GitHub Actions, etc.)

---

## 📁 **Output Fields**
Each job record typically includes:

* Job Title
* Company Name
* Location
* Salary (if available)
* Experience Required
* Education Level
* Deadline
* Job Link (direct)
* Job ID
* Category / Type

*(Add/remove fields depending on your implementation.)*

---

## 🛠️ **Tech Stack**

* Python 3.8+
* `requests` or `selenium` (based on your code)
* `pandas` (for CSV/JSON exports)
* `gspread` + Google Credentials (for Google Sheets export)

---

# 🚀 **Getting Started**

## **1. Clone the Repository**

```bash
git clone https://github.com/your-username/merojob-top-jobs-scraper.git
cd merojob-top-jobs-scraper
```

---

## **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

Your `requirements.txt` might include:

```
requests
pandas
gspread
oauth2client
selenium
python-dotenv
```

---

# ⚙️ **Configuration**

## **Google Sheets Setup (Optional)**

If you want Google Sheets export:

1. Create a Google Cloud Project
2. Enable **Google Sheets API**
3. Download `credentials.json`
4. Save it in the project root
5. Add your Sheets ID in `.env`

Example `.env`:

```
GOOGLE_SHEET_ID=your_google_sheet_id_here
```

---

# ▶️ **Usage**

## **Run the scraper**

```bash
python scraper.py
```

## Example output:

```
Scraping Top Jobs...
Found 42 jobs.
Exporting to CSV...
Exporting to JSON...
Updating Google Sheet...
Done.
```

---

# 📦 **Data Export**

### **CSV Output**

File saved as:

```
output/jobs.csv
```

### **JSON Output**

File saved as:

```
output/jobs.json
```

### **Google Sheets**

Data is appended or overwritten based on your configuration.

---

# 📂 **Project Structure**

```
merojob-top-jobs-scraper/
│
├── scraper.py              # Main scraping script
├── export_csv.py           # CSV export helper
├── export_json.py          # JSON export helper
├── export_gsheet.py        # Google Sheets helper
│
├── utils/
│   ├── parser.py           # Parse and clean job data
│   ├── fetcher.py          # API/HTML fetching logic
│
├── credentials.json        # (ignored in .gitignore)
├── .env                    # API keys & config
├── requirements.txt
└── README.md
```

---

# 🧪 **Example Code Snippet**

*(Replace with your actual scraper logic)*

```python
from utils.fetcher import fetch_jobs
from utils.parser import clean_data
from export_csv import export_csv
from export_json import export_json
from export_gsheet import export_gsheet

jobs = fetch_jobs()
cleaned_jobs = clean_data(jobs)

export_csv(cleaned_jobs, "output/jobs.csv")
export_json(cleaned_jobs, "output/jobs.json")
export_gsheet(cleaned_jobs)

print("Scraping Completed!")
```

---

# 🔄 **Automation (Optional)**

### **Run daily using GitHub Actions**

Create `.github/workflows/scraper.yml`:

```yaml
name: Daily Scraper
on:
  schedule:
    - cron: "0 */6 * * *"   # every 6 hours
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run scraper
        run: python scraper.py
```

---

# 📜 **License**

MIT License – feel free to use, modify, and distribute.

---

# 🤝 **Contributing**
Pull requests are welcome!
If you'd like to add features (like notifications or database storage), feel free to open an issue.

---

# 🙌 **Author**

**Dipak (Dpm IT)**
GitHub: *your link here*
