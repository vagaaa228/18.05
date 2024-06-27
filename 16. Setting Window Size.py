from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10) # in seconds

driver.get("https://www.lambdatest.com/")

element = driver.find_element_by_id("testing_form")

# Setting the window size to 1200 * 800

driver.set_window_size(1200, 800)