# SnowGlobe

## A monitoring system for upcoming snow days based on the time and location of events in your calendars. 

### Usage 
This program is ideally meant to run on a dedicated computer and performs the following actions: 
- It logs in to your Google Calendar system and pulls the next 10 events that you have in a specified calendar 
- It then pulls the zip code from each event and opens a Chrome instance that visits a website called the Snow Day Calculator (https://www.snowdaycalculator.com/calculator.php)
- Once open, the program inputs the zip code, number of snow days, and school district type (“Urban Public” by default) and returns the %chance of a snow day on the following page. 
 
#SnowGlobe


