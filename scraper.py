from selenium import webdriver
# Provides the WebDriver interface to control a browser (e.g., Chrome, Firefox)

from selenium.webdriver.common.by import By  
# Used to locate web elements using methods like ID, XPATH, CLASS_NAME, etc.

from selenium.webdriver.support.ui import WebDriverWait  
# Allows waiting for a specific condition to occur before continuing execution

from selenium.webdriver.support import expected_conditions as EC  
# Contains predefined conditions (like element visible, clickable) used with WebDriverWait

import csv
import time
import os
from datetime import datetime

# -------------------------
# PATH SETUP (IMPORTANT)
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

TOP_JOBS_CSV = os.path.join(DATA_DIR, "top_jobs.csv")
BY_DEADLINE_CSV = os.path.join(DATA_DIR, "by_deadline.csv")

FIELDNAMES = ["Post", "Company", "Experience", "Level", "Salary", "Deadline"]

# -------------------------
# SELENIUM SETUP
# -------------------------
# driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") # Runs Chrome in headless mode. The browser works without opening a visible window.
chrome_options.add_argument("--no-sandbox") # Disables Chrome’s security sandbox. Helps avoid permission-related crashes.
chrome_options.add_argument("--disable-dev-shm-usage") # Prevents Chrome from using /dev/shm (shared memory). Instead, it uses disk storage.

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://merojob.com/")
wait = WebDriverWait(driver, 10)

# Click "Individual Jobs" tab
try:
    btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Individual Jobs')]")
        )
    )
    btn.click()
except Exception as e:
    print("Error clicking Individual Jobs:", e)
    driver.quit()
    exit()

# Wait for job cards
time.sleep(40)

jobs = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".rounded-lg.border.bg-card.text-card-foreground.shadow-sm.hover\\:shadow-xl")
    )
)

# -------------------------
# LOAD EXISTING top_jobs.csv
# -------------------------
existing_jobs = []      # List to store all existing job records from the CSV
existing_keys = set()   # Set to store unique job identifiers for fast duplicate checking

if os.path.exists(TOP_JOBS_CSV):
    with open(TOP_JOBS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # Read CSV file as dictionaries using header row as keys
        for row in reader:           # Iterate through each job record in the CSV
            key = (row["Post"], row["Company"], row["Deadline"]) # Create a unique identifier for a job entry
            existing_keys.add(key)      # Store the unique job key to avoid duplicates
            existing_jobs.append(row)   # Save the full job record for later use

# -------------------------
# SCRAPE NEW JOBS
# -------------------------
new_jobs = []

for job in jobs:
    lines = job.text.split("\n")

    if len(lines) < 6:
        continue

    post, company, experience, level, salary = lines[:5]
    deadline_raw = lines[5].replace("Apply Before: ", "").strip()

    try:
        deadline = datetime.strptime(deadline_raw, "%b %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        deadline = deadline_raw

    key = (post, company, deadline)
    if key in existing_keys:
        continue

    new_jobs.append({
        "Post": post.strip(),
        "Company": company.strip(),
        "Experience": experience.strip(),
        "Level": level.strip(),
        "Salary": salary.strip(),
        "Deadline": deadline
    })

    existing_keys.add(key)

driver.quit()

# -------------------------
# WRITE top_jobs.csv
# -------------------------
all_jobs = new_jobs + existing_jobs

with open(TOP_JOBS_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(all_jobs)

print(f"top_jobs.csv updated ({len(new_jobs)} new jobs)")

# -------------------------
# UPDATE by_deadline.csv
# -------------------------
deadline_jobs = []
deadline_keys = set()

if os.path.exists(BY_DEADLINE_CSV):
    with open(BY_DEADLINE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["Post"], row["Company"], row["Deadline"])
            deadline_keys.add(key)
            deadline_jobs.append(row)

for job in all_jobs:
    key = (job["Post"], job["Company"], job["Deadline"])
    if key not in deadline_keys:
        deadline_jobs.append(job)
        deadline_keys.add(key)

def parse_deadline(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return datetime.max

deadline_jobs.sort(key=lambda x: parse_deadline(x["Deadline"]))

with open(BY_DEADLINE_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(deadline_jobs)

print(f"by_deadline.csv updated ({len(deadline_jobs)} jobs)")