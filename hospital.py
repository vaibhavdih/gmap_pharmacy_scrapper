from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException





#content = driver.find_element_by_class_name('div.section-result')


def get_data(driver,city):
	try:
		check = driver.find_element_by_css_selector('div.section-no-result-title')
		print("no result title found")
		return False,driver
	except NoSuchElementException:
		content =driver.find_elements_by_css_selector('div.section-result')
		for j in range(len(content)):
			try:
				content=driver.find_elements_by_css_selector('div.section-result')
				try:
					current_url_ = driver.current_url
					content[j].send_keys(Keys.ENTER)
				except IndexError:
					continue

				while driver.current_url == current_url_:
					time.sleep(1)
				time.sleep(3)

				try:
					name_=driver.find_element_by_css_selector('h1.section-hero-header-title-title.GLOBAL__gm2-headline-5')
					try:
						name=name_.get_attribute("innerHTML")
					except NoSuchAttributeException:
						name="N.A."


				except NoSuchElementException:
					name="N.A."


				try:
					rating_ = driver.find_element_by_css_selector('span.section-star-display')
					try:
						rating = rating_.get_attribute("innerHTML")
					except NoSuchAttributeException:
						rating="N.A."


				except NoSuchElementException:
					rating="N.A."
				

				try:
					c = driver.find_elements_by_css_selector('div.section-info-line')
					location_img='https://www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png'
					contact_img ='https://www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png'

					for a in c:
						try:
							b=a.find_element_by_tag_name('img')
							try:
								if b.get_attribute('src') == location_img:
									address = a.find_element_by_css_selector('span.widget-pane-link').get_attribute('innerHTML')
							except NoSuchAttributeException:
								address="N.A."

						except NoSuchElementException:
							address="N.A."

						try:
							d=a.find_element_by_tag_name('img')
							try:
								if d.get_attribute('src') == contact_img:
									contact = a.find_element_by_css_selector('span.widget-pane-link').get_attribute('innerHTML')
							except NoSuchAttributeException:
								contact="N.A."

						except NoSuchElementException:
							contact="N.A."


			
					

				except NoSuchElementException:
					address="N.A."
					contact="N.A."

				file = open(str(city)+".txt",'a')
				file.write(str(name)+" @;@ "+str(rating)+" @;@ "+str(address)+" @;@ "+str(contact)+"\n")
				file.close()

				print(j)
				print(name)
				print(rating)
				print(address)
				print(contact)
				print("===============================")

			except NoSuchElementException:
				print("no details")

			try:
				driver.find_element_by_css_selector('button.section-back-to-list-button.blue-link.noprint').send_keys(Keys.ENTER)
			except NoSuchElementException:
				print("cant proceed to next page")

			current_url_ = driver.current_url
			while driver.current_url == current_url_:
				time.sleep(1)
			time.sleep(2)

		try:
			next_page=driver.find_element_by_css_selector('div.gm2-caption')
			next_page_buttons=next_page.find_elements_by_tag_name('button')
			
			next_page_buttons[-1].click()
			current_url_ = driver.current_url
			while driver.current_url == current_url_:
				time.sleep(1)
			time.sleep(2)
			return True,driver
					
										
			
		except NoSuchElementException:
			print("can not move to next page")


	

def check_run(driver,city):
	while True:
		m,driver=get_data(driver,city)
		if not m:
			print("program ended")
			driver.close()
			break
	




		

	
def start_run(city):
	url="https://www.google.com/maps/search/medical+stores+in+"+str(city)+"/"
	driver = webdriver.Chrome('/home/vaibhav/Downloads/chromedriver_linux64/chromedriver')
	driver.get(url)
	check_run(driver,city)


	
start_run("koderma")











	
	
	
	
	
	
	
	
	
	

	

	

	

	
	
	
	
	



