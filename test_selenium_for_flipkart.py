from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("http://www.flipkart.com/")
search_box=driver.find_element_by_id("fk-top-search-box")
search_box.send_keys("tommy hilfiger watches")
search_box.submit()
try:
	element1 = WebDriverWait(ff, 5).until(EC.presence_of_element_located((By.ID, "sort-dropdown")))
	print 'element is ', element1
except:
	pass
	element=driver.find_element_by_id("sort-dorpdown")
	element.send_keys("P")
	element.send_keys("P")
	element.send_keys("P")
	element.send_keys(Keys.RETURN)
