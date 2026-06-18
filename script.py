from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Read Instagram export
with open("pending_follow_requests.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

usernames = []

# Extract usernames
for row in soup.find_all("tr"):
    cells = row.find_all("td")

    if len(cells) == 2:
        label = cells[0].get_text(strip=True)

        if label == "Username":
            usernames.append(cells[1].get_text(strip=True))

print(f"Found {len(usernames)} usernames")

# Open browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.instagram.com/")
input("Log into Instagram manually, then press Enter...")

for username in usernames:
    try:
        profile_url = f"https://www.instagram.com/{username}/"
        print(f"Processing {username}")

        driver.get(profile_url)

        # Wait for page to load
        time.sleep(3)

        # Click Requested
        requested_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Requested')]")
            )
        )
        requested_btn.click()

        time.sleep(1)

        # Click Unfollow in popup
        unfollow_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Unfollow')]")
            )
        )
        unfollow_btn.click()

        print(f"✓ Cancelled request for {username}")

        # Slow down to avoid triggering Instagram limits
        time.sleep(5)

    except Exception as e:
        print(f"✗ Failed for {username}: {e}")

driver.quit()