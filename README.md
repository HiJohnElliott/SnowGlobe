# SnowGlobe

This is a script for monitoring upcoming snow days based on the events that one has in a Google Calendar or set of calendars. The script takes the following steps: 

- Log in to and request the nexy 10 events on a specified Google Calendar 
- Parse the zip code for each event 
- Open and new Chrome window and navigate to https://www.snowdaycalculator.com/calculator.php
- Input each zip code and other specified points of data 
- Parse the %chance of a snow day from the websites response

This script is set to run in a loop for now. 

This script uses the following Python libraries 
- Selenium
- OAuth2client
- GoogleAPIClient 
