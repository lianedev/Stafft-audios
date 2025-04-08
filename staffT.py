from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys
import logging
from playsound import playsound

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('transcription_staff.log'),
        logging.StreamHandler()
    ]
)

# Configuration
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver_path = r"D:\projects\staff-hack\chrome-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Map of field names to values
form_data = {
    "fullname": "John Doe",
    "email": "john.doe@example.com",
    "phone": "1234567890",
    "paypal": "johndoe@example.com",
    "skype": "12345"
}

# Audio names to check for (any 3 of these 4 will trigger the alert)
audio_files_to_check = ["6xxddd", "statepolice", "7oplsc", "aircraft"]  # 4 possible files

def play_alert():
    """Play system alert sound using playsound"""
    try:
        # Replace with your actual sound file path
        playsound('D:\projects\staff-hack\mixkit-uplifting-flute-notification-2317.wav')  # Make sure you have an alert.mp3 file in your directory
    except Exception as e:
        logging.error(f"Couldn't play alert sound: {e}")
        # Fallback to system beep if playsound fails
        try:
            import winsound
            winsound.Beep(1000, 1000)
            winsound.Beep(1500, 1000)
            winsound.Beep(2000, 1000)
        except:
            logging.error("Couldn't play any alert sound")

def check_audio_files():
    """Check if at least 3 of the 4 audio files are present"""
    try:
        # Wait for page to load completely
        time.sleep(2)
        page_source = driver.page_source.lower()
        found_files = [keyword for keyword in audio_files_to_check 
                      if keyword.lower() in page_source]
        
        if len(found_files) >= 3:  # Trigger if 3+ files found
            logging.info(f"✅ Found {len(found_files)}/4 required audio files:")
            for file in found_files:
                logging.info(f" - {file}")
            play_alert()
            return True
        
        logging.info(f"Found {len(found_files)}/3+ required audio files")
        if found_files:
            logging.info("Found files: " + ", ".join(found_files))
        
        missing_files = set(audio_files_to_check) - set(found_files)
        if missing_files:
            logging.info("Missing files: " + ", ".join(missing_files))
            
        return False
    except Exception as e:
        logging.error(f"Error checking audio files: {e}")
        return False

# [Rest of your code remains exactly the same...]