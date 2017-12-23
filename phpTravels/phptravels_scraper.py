import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

url = "http://www.phptravels.net/login"
#Use your username and password
username = "User name"
password = ""
driver = webdriver.Firefox()

if __name__ == "__main__":
   driver.get(url)

   uname = driver.find_element_by_name("username") 
   uname.send_keys(username)

   passw = driver.find_element_by_name("password")
   passw.send_keys(password)
   passw.send_keys(Keys.RETURN)
   
   # Find the submit button using class name and click on it.
   submit_button = driver.find_element_by_class_name("loginbtn").click()

   WebDriverWait(driver, 100).until( lambda driver: driver.find_element_by_id('bookings'))
   divs = driver.find_element_by_id("bookings")
   rows = divs.find_elements_by_class_name("row")
   print ('..................................................................')
   for row in rows:
       name = row.find_element_by_tag_name('a')
       print (name.text)
   print ('..................................................................')

 

      
