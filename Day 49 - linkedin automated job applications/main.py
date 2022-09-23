from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

service = Service(r"C:chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3260863804&f_AL=true&f_WT=2&keywords=junior%20python%20developer&location=Remoto&refresh=true")

driver.implicitly_wait(5)
login = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis, .btn-secondary-emphasis:visited, .btn-secondary-emphasis:focus")
login.click()
log_email = driver.find_element(By.ID, "username")
log_email.send_keys("email")
log_pass = driver.find_element(By.ID, "password")
log_pass.send_keys("password", Keys.ENTER)


all_offers = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list__list-item--active")

for job in all_offers:
    print("called")
    job.click()
    time.sleep(5)


all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    try:
        print("called")
        listing.click()
        time.sleep(2)
        guardar = driver.find_element(By.CLASS_NAME, "jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary")
        guardar.click()
    except NoSuchElementException:
        print("Not Found")
    else:
        guardar.click()


# This version doesnt apply, just save the job offers.

# time.sleep(5)

# all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#
#     # Try to locate the apply button, if can't locate then skip the job.
#     try:
#         apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)
#
#         # If phone field is empty, then fill your phone number.
#         phone = driver.find_element_by_class_name("fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         submit_button = driver.find_element_by_css_selector("footer button")
#
#         # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             close_button.click()
#             time.sleep(2)
#             discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         # Once application completed, close the pop-up window.
#         time.sleep(2)
#         close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#         close_button.click()
#
#     # If already applied to job or job is no longer accepting applications, then skip.
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()