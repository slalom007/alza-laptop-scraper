from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re  # NEW: Import the regular expression library
import csv  # NEW: Import the library for writing CSV files

URL = "https://www.alza.hu/notebookok/18842920.htm"

# A list to store our structured data
laptops_data = []

print("Setting up the browser driver...")
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    print(f"Opening the page: {URL}")
    driver.get(URL)

    try:
        time.sleep(2)
        accept_cookies_button = driver.find_element(By.CSS_SELECTOR, ".js-cookies-agree")
        accept_cookies_button.click()
        print("Cookie consent banner accepted.")
    except Exception as e:
        print("Cookie consent banner not found or could not be clicked. Continuing...")

    print("Waiting for product boxes to load...")
    wait = WebDriverWait(driver, 10)
    # Let's scrape all product boxes, not just the first 5
    product_boxes = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.box")))

    print(f"\n--- Scraping data for {len(product_boxes)} laptops ---")

    for box in product_boxes:
        name = None
        price = None

        try:
            name_element = box.find_element(By.CSS_SELECTOR, "a.name")
            name = name_element.text
        except:
            continue  # If a box has no name, it's not a product, skip it

        try:
            price_element = box.find_element(By.CSS_SELECTOR, "div.price")
            raw_price_text = price_element.text

            # NEW: Use regex to find the price pattern (numbers followed by 'Ft')
            match = re.search(r'(\d[\d\s]*\d)\s*Ft', raw_price_text)
            if match:
                # Clean the found price: remove spaces and convert to integer
                price = int(match.group(1).replace(" ", ""))

        except:
            pass

        # If we successfully found a name and a price, add it to our list
        if name and price:
            print(f"Found: {name} - {price} Ft")
            laptops_data.append({'name': name, 'price': price})

    # --- NEW: Save the collected data to a CSV file ---
    if laptops_data:
        print("\nSaving data to laptops.csv...")
        # Define the CSV file name and the header
        csv_file = "laptops.csv"
        csv_columns = ['name', 'price']

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data_row in laptops_data:
                writer.writerow(data_row)
        print(f"Successfully saved {len(laptops_data)} items to {csv_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'driver' in locals():
        print("Closing the browser.")
        driver.quit()