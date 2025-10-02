# Alza.hu Laptop Scraper 💻

## Project Description

This project is a web scraper built with Python to automatically collect data about laptops from the Hungarian e-commerce site, Alza.hu. It uses the Selenium library to control a web browser, allowing it to handle dynamically loaded content (JavaScript).

The script extracts the name and price of each laptop on the main notebook page, cleans the extracted data using regular expressions, and saves the final, structured information into a `laptops.csv` file.

---

## Technologies and Skills Demonstrated

- **Web Scraping:** Using **Selenium** for browser automation to scrape a modern, JavaScript-heavy website.
- **Bot Detection Evasion:** Implementing strategies (e.g., robust headers, handling cookie banners) to bypass basic anti-scraping measures.
- **Dynamic Waits:** Using Selenium's `WebDriverWait` for efficient and reliable page loading, instead of fixed sleeps.
- **Data Cleaning:** Parsing messy, unstructured text to extract clean, numerical data using **Regular Expressions (Regex)**.
- **Data Storage:** Saving the scraped data into a structured CSV file using Python's built-in `csv` module.

---

## Tools and Libraries Used

* Python
* Selenium
* webdriver-manager
* Requests
* BeautifulSoup4

---

## How to Run This Project

1.  Clone this repository to your local machine.
2.  Make sure you have Google Chrome installed.
3.  Install the required libraries from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the Python script:
    ```bash
    python main.py
    ```
5.  After the script finishes, a `laptops.csv` file will be created in the project directory.