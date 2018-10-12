from selenium import webdriver
from Google_Calendar_Caller import calCall
import re


def snowDayCalculator(zip, numberOfSnowdDays, nameOfEvent):
	driver = webdriver.Chrome('/Applications/chromedriver')

	# Open the webpage
	driver.get('https://www.snowdaycalculator.com/calculator.php')

	# input the zipcode in the zipcode box
	inputZipCode = driver.find_element_by_xpath('//*[@id="calculator"]/div/article/span/form/center/table[2]/tbody/tr/td[1]/span/center/input').send_keys(zip)

	# input the number of snow days so far in the year
	inputNumberOfSnowDays = driver.find_element_by_xpath('//*[@id="calculator"]/div/article/span/form/center/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys(numberOfSnowdDays)

	# Select type of school district
	typeOfDistrict = driver.find_element_by_xpath('//*[@id="calculator"]/div/article/span/form/center/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/select').send_keys('Urban Public')

	# Hit the Calculate Button
	commitButton = driver.find_element_by_xpath('//*[@id="calculator"]/div/article/span/form/center/input').click()

	# Get the % chance of snow day
	getPercentChance = driver.find_element_by_xpath('//*[@id="predSPAN"]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/font')

	print('There is a' + getPercentChance.text + ' of a snow day for ' + nameOfEvent)
	driver.quit()


def parseZip(locationString): 
	stringLook = re.search(r'.*(\d{5}(\-\d{4})?)', locationString, flags=0)
	zipString = stringLook.group(1)
	return zipString


def snowGlobe():
	for event in calCall():
		eventDate = event['start'].get('dateTime', event['start'].get('date'))
		eventSummary =  event['summary']
		eventLocation = event['location']
		eventZip = parseZip(eventLocation)
		snowDayCalculator(eventZip, 0, eventSummary)

