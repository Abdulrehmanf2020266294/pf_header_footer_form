from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), Options=chrome_options))
actions = ActionChains(driver)
driver.get("https://pf.com.pk/job/business-development-associate/")
driver.implicitly_wait(5)

#press apply now
applynow_button = driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/div[2]/div[1]/a")
applynow_button.click()
expected_url = "https://pf.com.pk/job/business-development-associate/#position"
if driver.current_url==expected_url:
    print("form opened")
else:
    print("form not opened")
driver.implicitly_wait(5)

#fill the form
gender_male = driver.find_element(By.XPATH, "//*[@id='gender']/span[1]/label/input")
gender_female = driver.find_element(By.XPATH, "//*[@id='gender']/span[2]/label/input")
gender_male.click()

dob_input = driver.find_element(By.ID, "dob")
driver.execute_script("arguments[0].removeAttribute('onkeydown')", dob_input)
driver.execute_script("arguments[0].value = '1995-01-01'", dob_input)

fullname_field = driver.find_element(By.XPATH, "//*[@id='name']")
fullname_field.send_keys("abc def")

email_field = driver.find_element(By.XPATH, "//*[@id='email']")
email_field.send_keys("abcdef123@gmail.com")

cnic_field = driver.find_element(By.XPATH, "//*[@id='cnic']")
cnic_field.send_keys("35202688888881")

contactnum_field = driver.find_element(By.XPATH, "//*[@id='phone']")
contactnum_field.send_keys("03116969696")

address_field = driver.find_element(By.XPATH, "//*[@id='address']")
address_field.send_keys("176-G2 Wapda Town, Lahore")

city_field = driver.find_element(By.XPATH, "//*[@id='city']")
city_field.send_keys("Lahore")

qualification_dropdown = driver.find_element(By.XPATH, "//*[@id='qualification']/option[4]")
qualification_dropdown.click()

year_select = driver.find_element(By.XPATH, "//*[@id='yr-of-comp']/option[17]")
year_select.click()

university_field = driver.find_element(By.XPATH, "//*[@id='university']")
university_field.send_keys("University of abcdefgh")

cgpa_field = driver.find_element(By.XPATH, "//*[@id='cgpa_cd']")
cgpa_field.send_keys("2.89")

currentlyworking_yes = driver.find_element(By.XPATH, "//*[@id='cur-working']/span[1]/label/input")
currentlyworking_no = driver.find_element(By.XPATH, "//*[@id='cur-working']/span[2]/label/input")
currentlyworking_no.click()

expectedsalary_fied = driver.find_element(By.XPATH, "//*[@id='salry-expt']")
expectedsalary_fied.send_keys("80000")

hear_field = driver.find_element(By.XPATH, "//*[@id='hear-abt-us']")
hear_field.send_keys("linkedin")

doj_input = driver.find_element(By.ID, "doj")
driver.execute_script("arguments[0].removeAttribute('onkeydown')", doj_input)
driver.execute_script("arguments[0].value = '2024-11-11'", doj_input)

experience_dropdown = driver.find_element(By.XPATH, "//*[@id='experiance']/option[1]")
cv_upload = driver.find_element(By.XPATH, "//*[@id='resume']")

cv_upload.send_keys(r'C:\Users\Acer\Downloads\testcv.pdf')

submit_button = driver.find_element(By.XPATH, "//*[@id='submit-btn']")
submit_button.click()

time.sleep(10)