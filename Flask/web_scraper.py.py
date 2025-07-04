from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_driver_path = 'D:/Flask/chromedriver.exe' 
options = Options()
options.headless = False  # Need to set it False to access the contents after accepting the cookies
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage
driver.get('https://journals.sagepub.com/toc/JMX/current')

time.sleep(5) # Just to make sure the webpage is loaded completely

try:
    # Wait for the page to load and the retrieve the articles
    wait = WebDriverWait(driver, 10)  # Wait for a 10 seconds
    articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.issue-item')))

    # Extract details for each article
    for article in articles:
        # Extract title
        title_element = article.find_element(By.CSS_SELECTOR, 'h5.issue-item__heading')
        title = title_element.text if title_element else "Title not found"
        
        # Extract authors
        try:
            # there are two selectors for author's elements : div.issue-item__authors ul.rlist--inline li span and div.issue-item__authors
            # For multiple authors
            authors_elements = article.find_elements(By.CSS_SELECTOR, 'div.issue-item__authors ul.rlist--inline li span') 
            if authors_elements:
                authors = [author.text for author in authors_elements]
            else:
                # for single author
                authors_elements = article.find_elements(By.CSS_SELECTOR, 'div.issue-item__authors')
                authors = [author.text for author in authors_elements if author.text] if authors_elements else ["Authors not found"]
        except:
            authors = ["Authors not found"]

        # Extract published date
        try:
            published_date_element = article.find_element(By.CSS_SELECTOR, 'div.issue-item__header span:nth-child(3)')
            published_date = published_date_element.text.replace('First published ', '') if published_date_element else "Published date not found"
        except:
            published_date = "Published date not found"

        # Extract DOI
        try:
            doi_element = article.find_element(By.CSS_SELECTOR, 'a[href^="/doi/abs/"]')
            doi = doi_element.get_attribute('href').split('/')[-1] if doi_element else "DOI not found"
        except:
            doi = "DOI not found"

        # Extract abstract
        try:
            abstract_button = article.find_element(By.CSS_SELECTOR, 'div.issue-item__abstract button')
            abstract_button.click()
            time.sleep(2)  # Just to make sure the abstract is loaded after clicking it
            abstract_content = article.find_element(By.CSS_SELECTOR, 'div.issue-item__abstract__content').text
            abstract = abstract_content if abstract_content else "Abstract not found"
        except:
            abstract = "Abstract not found"

        # Print the extracted information for each article
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Published Date: {published_date}")
        print(f"DOI: {doi}")
        print(f"Abstract: {abstract}\n")

finally:
    # Close the chrome webdriver
    driver.quit()