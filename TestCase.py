import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from homePageElements import HomePageElements

driver = webdriver.Chrome()
driver.get("https://pf.com.pk/")
driver.maximize_window()
time.sleep(4)

# Expertise button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.expertise)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "expertise" in driver.current_url, "Go to expertise at PF page failed."
    print("Expertise button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# About us button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.about_us)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "about-us" in driver.current_url, "Go to about us at PF page failed."
    print("About Us Button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# Life at PF button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.life_at_pf)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "life-at-pf" in driver.current_url, "Go to Life at PF page failed."
    print("Life at PF button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# Graduate Gateway button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.trainee_program)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "trainee-program" in driver.current_url, "Go to Graduate Gateway Program page failed."
    print("Graduate Gateway Program button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# Career Button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.career)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "career" in driver.current_url, "Go to career page failed."
    print("Career button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# Apply Now Button
def test_click_button():
    button = driver.find_element(By.XPATH, HomePageElements.apply_now)
    assert button.is_displayed(), "Button is visible on the page."
    button.click()
    assert "apply-now" in driver.current_url, "Go to apply now page failed."
    print("Apply Now button clicked successfully and correct page loaded")
test_click_button()
time.sleep(2)
driver.back()

# Career Dropdown Option 1 (Open Positions)
def career_dropdown_click_button():
    actions = ActionChains(driver)
    Career_button = driver.find_element(By.XPATH, HomePageElements.career)
    actions.move_to_element(Career_button).perform()
    Career_dropdown1 = driver.find_element(By.ID, HomePageElements.career_drop1)
    Career_dropdown1.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Careers option 1 Open positions clicked successfully and correct page opened")
    else:
        print("Careers option 1 Open positions did not work")
career_dropdown_click_button()
time.sleep(2)
driver.back()

# Career Dropdown Option 2 (Send Resume)
def career_dropdown_click_button():
    actions = ActionChains(driver)
    Career_button = driver.find_element(By.XPATH, HomePageElements.career)
    actions.move_to_element(Career_button).perform()
    Career_dropdown2 = driver.find_element(By.ID, HomePageElements.career_drop2)
    Career_dropdown2.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/apply-now/#popup1"
    if driver.current_url == expected_url:
        print("Careers option 2 Send Resume clicked successfully and correct page opened")
    else:
        print("Careers option 2 Send Resume did not work")
career_dropdown_click_button()
time.sleep(2)
driver.back()

# Resources Dropdown Option 1 (Blogs)
def resources_dropdown_click_button():
    actions = ActionChains(driver)
    Resource_button = driver.find_element(By.XPATH, HomePageElements.resource)
    actions.move_to_element(Resource_button).perform()
    Resource_dropdown1 = driver.find_element(By.XPATH, HomePageElements.resource_drop1)
    Resource_dropdown1.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/blogs/"
    if driver.current_url == expected_url:
        print("Resources option 1 Blogs clicked successfully and correct page opened")
    else:
        print("Resources option 1 Blogs did not work")
resources_dropdown_click_button()
time.sleep(2)
driver.back()

# Resources Dropdown Option 2 (News)
def resources_dropdown_click_button():
    actions = ActionChains(driver)
    Resource_button = driver.find_element(By.XPATH, HomePageElements.resource)
    actions.move_to_element(Resource_button).perform()
    Resource_dropdown2 = driver.find_element(By.XPATH, HomePageElements.resource_drop2)
    Resource_dropdown2.click()
    driver.implicitly_wait(5)
    expected_url = "https://pf.com.pk/news/"
    if driver.current_url == expected_url:
        print("Resources option 2 News clicked successfully and correct page opened")
    else:
        print("Resources option 2 News did not work")
resources_dropdown_click_button()
time.sleep(2)
driver.back()

# PF Logo Clickable and redirect to homepage
def test_logo_click():
    button = driver.find_element(By.XPATH, HomePageElements.pf_logo)
    assert button.is_displayed(), "Logo is visible on the page."
    button.click()
    assert "pf" in driver.current_url, "Redirect to homepage failed."
    print("PF Logo clicked successfully and redirect to homepage")
test_logo_click()

# Footer test cases start here

# Life at PF Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_life_at_pf)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    assert "life-at-pf" in driver.current_url, "Go to Life at PF page failed."
    print("Life at PF footer link clicked successfully and correct page loaded")
test_click_link()
time.sleep(2)
driver.back()

# Our Teammates Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_our_teammate)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    assert "about-us" in driver.current_url, "Go to our teammate page failed."
    print("Our Teammate footer link clicked successfully and correct page loaded")
test_click_link()
time.sleep(2)
driver.back()

# In House Privacy Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_in_house_privacy)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/privacypolicy/"
    if driver.current_url == expected_url:
        print("In House Privacy Policy footer link clicked successfully and correct page loaded")
    else:
        print("Go to Privacy Policy page failed")
test_click_link()
time.sleep(2)
driver.back()

# ISO Certifications Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_iso_certificates)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/iso_certified/"
    if driver.current_url == expected_url:
        print("ISO Certifications footer link clicked successfully and correct page loaded")
    else:
        print("Go to ISO Certifications page failed")
test_click_link()
time.sleep(2)
driver.back()

# Career Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_career)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/career/"
    if driver.current_url == expected_url:
        print("Career footer link clicked successfully and correct page loaded")
    else:
        print("Go to Career page failed")
test_click_link()
time.sleep(2)
driver.back()

# Job Positions Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_job_position)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Job Positions footer link clicked successfully and correct page loaded")
    else:
        print("Go to Job Positions page failed")
test_click_link()
time.sleep(2)
driver.back()

# Send Resume Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_send_resume)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/#popup1"
    if driver.current_url == expected_url:
        print("Send Resume footer link clicked successfully and correct page loaded")
    else:
        print("Go to Send Resume page failed")
test_click_link()
time.sleep(2)
driver.back()

# Track Your Application Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_track_application)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Track your Application footer link clicked successfully and correct page loaded")
    else:
        print("Go to Track your Application page failed")
test_click_link()
time.sleep(2)
driver.back()

# Ransomware Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_ransomware)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/ransomware-year-beware-you-may-be-the-next-target/"
    if driver.current_url == expected_url:
        print("Ransomware footer link clicked successfully and correct page loaded")
    else:
        print("Go to Ransomware page failed")
test_click_link()
time.sleep(2)
driver.back()

# FinTech Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_fintech)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/social-impact-of-fintech-solution-in-pakistan/"
    if driver.current_url == expected_url:
        print("FinTech footer link clicked successfully and correct page loaded")
    else:
        print("Go to FinTech page failed")
test_click_link()
time.sleep(2)
driver.back()

# Life-Changing Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_life_changing)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/is-it-a-life-changing-industry/"
    if driver.current_url == expected_url:
        print("Life-Changing footer link clicked successfully and correct page loaded")
    else:
        print("Go to Life-Changing page failed")
test_click_link()
time.sleep(2)
driver.back()

# AI Career Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_ai_career)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/blogs/ai-career-paths-and-future-market-trends-in-ai/"
    if driver.current_url == expected_url:
        print("AI Career footer link clicked successfully and correct page loaded")
    else:
        print("Go to AI Career page failed")
test_click_link()
time.sleep(2)
driver.back()

# Apply Now Footer Link
def test_click_link():
    link = driver.find_element(By.XPATH, HomePageElements.footer_apply_now)
    assert link.is_displayed(), "Link is visible on the page."
    link.click()
    expected_url = "https://pf.com.pk/apply-now/"
    if driver.current_url == expected_url:
        print("Apply Now footer link clicked successfully and correct page loaded")
    else:
        print("Go to Apply Now page failed")
test_click_link()
time.sleep(2)
driver.back()

# PF Footer Logo Clickable and redirect to homepage
def test_logo_click():
    button = driver.find_element(By.XPATH, HomePageElements.pf_footer_logo)
    assert button.is_displayed(), "Logo is visible on the page."
    button.click()
    assert "pf" in driver.current_url, "Redirect to homepage failed."
    print("PF footer Logo clicked successfully and redirect to homepage")
test_logo_click()
