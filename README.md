# Selenium Audio Checker Script 

## Overview
This Python script automates the process of checking for specific audio file references on a webpage using Selenium WebDriver.  
It is designed to alert the user if at least 3 out of 4 predefined audio file keywords are found in the page source.  

Key Features:
- Automates browser navigation and page inspection using Selenium.
- Checks for specific audio file names in the page source.
- Triggers an alert (sound notification) if the required audio files are detected.
- Logs all actions, found files, and missing files for traceability.

---

## Requirements
- Python 3.x
- Selenium (`pip install selenium`)
- Playsound (`pip install playsound`)
- Chrome browser and compatible ChromeDriver
- Windows OS (for `winsound` fallback)

---

## Configuration

### ChromeDriver
Set the path to your ChromeDriver executable:
```python

driver_path = r"D:\projects\chrome-win64\chromedriver.exe"

Enjoy
