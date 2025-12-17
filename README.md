# Top Jobs Scrapper
A Python-based web scraping project that automatically collects **top job listings** from **Merojob.com**, stores them in CSV files, and keeps the data **updated, deduplicated, and sorted by deadline**. The scraper is designed to run **locally or automatically every hour using GitHub Actions**.

---

## 🚀 Features
* Scrapes **Individual Job** listings from Merojob
* Extracts:
  * Job Title (Post)
  * Company Name
  * Experience Required
  * Job Level
  * Salary
  * Application Deadline
* Saves data into structured CSV files
* Prevents **duplicate entries** (based on Post, Company, Deadline)
* Automatically sorts jobs **by deadline**
* Stores deadlines in **date format** for accurate sorting
* Fully automated using **GitHub Actions (runs every hour)**

---

## 📁 Project Structure

```
Top-Jobs-Scrapper/
│
├── scraper.py              # Main scraping script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .github/
│   └── workflows/
│       └── scrapper.yml      # GitHub Actions workflow
└── data/
    ├── top_jobs.csv        # Main job listings
    └── by_deadline.csv     # Jobs sorted by deadline
```

---

## 🛠️ Tech Stack

* **Python 3**
* **Selenium** (Chrome WebDriver)
* **CSV module** for data storage
* **GitHub Actions** for automation

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dpm24800/top-jobs-scraper.git

cd top-jobs-scrapper
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Scraper

```bash
python scraper.py
```

CSV files will be created/updated inside the **data/** folder.

---

## 🤖 Automation with GitHub Actions

This project is configured to run **automatically every hour** using GitHub Actions.

### Workflow Highlights
* Uses **Ubuntu latest** runner
* Installs Google Chrome & ChromeDriver
* Runs the scraper in headless mode
* Commits updated CSV files back to the repository

### Cron Schedule

```yaml
schedule:
  - cron: '0 * * * *'   # Runs every hour
```

> ⚠️ Make sure your script uses **headless Chrome** for GitHub Actions.

---

## 📊 CSV Output Format

### `top_jobs.csv`

```
Post,Company,Experience,Level,Salary,Deadline
Senior Accountant,ABC Pvt Ltd,More than 2 years,Senior Level,Not Disclosed,2025-12-27
```

### `by_deadline.csv`

* Same structure as `top_jobs.csv`
* Sorted in **ascending order of deadline**
* No duplicate records

---

## 🔐 Anti-Duplication Logic

A job is considered duplicate if all three match:

* **Post**
* **Company**
* **Deadline**

This ensures clean and reliable data even with frequent scraping.

---

## ⚠️ Disclaimer

* This project is for **educational and personal use only**
* Respect the website’s **robots.txt** and terms of service
* Do not overload the website with excessive requests

---

<!-- ## 📌 Future Improvements

* Save data to a database (PostgreSQL / SQLite)
* Add email or Telegram notifications for new jobs
* Build a simple dashboard (Streamlit / Django)
* Add logging and error alerts -->

---

## 👤 Author

**Dipak Pulami Magar**  
Python | Web Scraping | Automation

---

⭐ If you find this project useful, consider giving it a star!
