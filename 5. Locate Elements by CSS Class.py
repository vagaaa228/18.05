from selenium import webdriver

driver = webdriver.Chrome()
driver.get(“https://www.lambdatest.com")
first_form_input = driver.find_element_by_class_name(“ form-control “)
