from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

while True:
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open a webpage
    driver.get("http://phanurat-chakkranukoonkit.duckdns.org/")

    # Print the title of the webpage
    print(driver.title)
    print("Get To my Web")

    # Close the WebDriver
    driver.quit()
    print("=========================================")
    time.sleep(5)
    print("=========================================")
    
