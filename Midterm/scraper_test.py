import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no browser window)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Fetch page
url = 'https://www.espn.com/soccer/table/_/league/'
# url = 'https://www.espn.com/soccer/table/_/league/'
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load the table

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract team names
team_names = [a.get_text() for a in soup.select('span.hide-mobile a')]

# Extract stats
stats = [span.get_text() for span in soup.select('tr.Table__TR td.Table__TD span.stat-cell')]

# Save to JSONL
with open('teams.jsonl', 'w', encoding='utf-8') as f:
    for i in range(0, len(stats), 8):
        team_stats = stats[i:i+8]
        team_data = {
            'team': team_names[i // 8],
            'GP': team_stats[0],
            'W': team_stats[1],
            'D': team_stats[2],
            'L': team_stats[3],
            'F': team_stats[4],
            'A': team_stats[5],
            'GD': team_stats[6],
            'P': team_stats[7]
        }
        json.dump(team_data, f)
        f.write('\n')
