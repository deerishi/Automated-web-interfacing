from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("http://www.google.com/maps")
inputelement=driver.find_element_by_name("q")
inputelement.send_keys("vasant kunj")
inputelement.submit()
button=driver.find_elements_by_class_name("searchbutton")
inputelement.send_keys(Keys.RETURN)
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 1000).until(EC.title_contains("vasant"))
    #while True:
    # You should see "cheese! - Google Search"
   	#print driver.title
	
except KeyboardInterrupt:
    driver.quit()

