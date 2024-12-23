from selenium import webdriver      # for automating browser interaction
from selenium.webdriver.common.by import By     # for locating elements in DOM
from selenium.webdriver.common.keys import Keys     # for simulating keyboard inputs
from selenium.webdriver.chrome.service import Service     # to manage ChromeDriver services
from webdriver_manager.chrome import ChromeDriverManager     # to automatically download & manage ChromeDriver
import time       # for adding delays between actions
import os       # for interacting with operating system
import logging       # for logging messages and errors
import schedule        # for scheduling tasks to run at specific time

# Setup Logging
logging.basicConfig(filename="whatsapp_automation.log",
                    level=logging.INFO,     # confirmation that things are working as expected
                    format="%(asctime)s-%(levelname)s-%(message)s")

# Function: Initializa WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://web.whatsapp.com/")
    logging.info("WhatsApp web opened.")
    return driver

# Function: Wait for QR Coge Login
def wait_for_login(driver):
    print("Please scan the QR Code to login...")
    time.sleep(15)
    logging.info("Login checked.")

# Function: Perform an action safely with logging
def safe_action(action, description):
    try:
        action()
    except Exception as e:
        logging.error(f"Error during {description}: {e}")

# Function: Search and Open Chat
def search_chat(driver, contact_name):
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.clear()      # clear pre-existing text
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    logging.info(f"Chat opened for: {contact_name}")

# Function: Send a message
def send_message(driver, contact_name, message):
    search_chat(driver, contact_name)
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    logging.info(f"Message sent to {contact_name}: {message}")

# Function: Bulk Messaging
def bulk_message(driver, contacts, message):
    for contact in contacts:
        send_message(driver, contact, message)
        time.sleep(30)

# Function: Auto-reply based on Keywords
def auto_reply(driver, trigger_keyword, reply_message):
    try:
        chats = driver.find_elements(By.XPATH, "//div[contains(@class,'message-in')]")
        last_message = chats[-1].find_element(By.CSS_SELECTOR, "span.selectable-text").text

        if trigger_keyword.lower() in last_message.lower():
            logging.info(f"Trigger keyword detected: {trigger_keyword}")
            send_message(driver, "Auto-Reply", reply_message)
    
    except Exception as e:
        logging.error(f"Error in Auto-reply: {e}")

# Function: Send Media
def send_media(driver, contact_name, file_path):
    search_chat(driver, contact_name)
    attach_button = driver.find_element(By.XPATH, "//span[@data-icon='clip']")
    attach_button.click()
    time.sleep(1)

    file_input = driver.find_element(By.XPATH, "//input[@typr='file']")
    file_input.send_keys(os.path.abspath(file_path))
    time.sleep(2)

    send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
    send_button.click()
    logging.info(f"Media sent to {contact_name}: {file_path}")

# Function: Scheduled Messaging
def schedule_message(driver, contact_name, message, send_time):
    def task():
        send_message(driver, contact_name, message)
        logging.info(f"Scheduled message sent to {contact_name}: {message}")
    
    schedule.every().day.at(send_time).do(task)

# Main Program Loop
def main():
    try:
        os.system("cls")

        # Initialize WebDriver and log in
        driver = setup_driver()
        wait_for_login(driver)
        print("WhatsApp Automation Iniitialized")

        # Menu-Based Interaction
        while True:
            print("\n-"*30)
            print("\n1. Send a single message")
            print("2. Send bulk messages")
            print("3. Auto-reply setup")
            print("4. Send media (image/video/document)")
            print("5. Schedule a message")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                contact = input("Enter contact name: ").strip()
                message = input("Enter your message: ").strip()
                safe_action(lambda: send_message(driver, contact, message), "sending single message")

            elif choice == "2":
                contacts = input("Enter contact names separated by commas: ").strip().split(",")
                message = input("Enter your message: ").strip()
                safe_action(lambda: bulk_message(driver, [c.strip() for c in contacts], message), "bulk messaging")

            elif choice == "3":
                keyword = input("Enter trigger keyword: ").strip()
                reply = input("Enter auto-reply message: ").strip()
                safe_action(lambda: auto_reply(driver, keyword, reply), "setting up auto-reply")

            elif choice == "4":
                contact = input("Enter contact name: ").strip()
                file_path = input("Enter the file path (image/video/document): ").strip()

                # error handling for file path and existance
                if not os.path.isfile(file_path):
                    logging.error(f"File not found: {file_path}")
                    print("Error: File does not exist. Please check file path and try again..")
                
                else:
                    try:
                        # chech if file has valid extension (image, video, document)
                        valid_extentions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4", ".avi", ".pdf", ".docx", ".txt"]
                        
                        if not any(file_path.endswith(ext) for ext in valid_extentions):
                            logging.error(f"Invalid file type: {file_path}")
                            print("Error: Invalid file type. Please provide valid image, video or document and try again..")
                        
                        else:
                            safe_action(lambda: send_media(driver, contact, file_path), "sending media")
                    except Exception as e:
                        logging.error(f"Error while sending media to {contact}: {e}")
                        print(f"An error occured whikle sending the media: {e}")

            elif choice == "5":
                contact = input("Enter contact name: ").strip()
                message = input("Enter your message: ").strip()
                send_time = input("Enter the scheduled time (HH:MM in 24-hour format): ").strip()

                # Error handling for correct time format
                time_pattern = r"^(2[0-3]|[01]?[0-9]):([0-5][0-9])$"  # Regex pattern for HH:MM in 24-hour format
                
                if not re.match(time_pattern, send_time):
                    logging.error(f"Invalid time format entered: {send_time}")
                    print("Error: Invalid time format. Please enter the time in HH:MM format (24-hour).")
                
                else:
                    try:
                        # Check if the entered time is in the future
                        now = datetime.now()
                        scheduled_time = datetime.strptime(send_time, "%H:%M")
                
                        if scheduled_time <= now:
                            logging.error(f"Scheduled time is in the past: {send_time}")
                            print("Error: Scheduled time cannot be in the past. Please choose a future time.")
                
                        else:
                            safe_action(lambda: schedule_message(driver, contact, message, send_time), "scheduling message")
                            print("Message scheduled successfully.")
                
                    except Exception as e:
                        logging.error(f"Error while scheduling message: {e}")
                        print(f"An error occurred while scheduling the message: {e}")

            elif choice == "6":
                print("Exiting te program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again..")
    
    except Exception as e:
        logging.error(f"Error in main process: {e}")
    
    finally:
        # close driver
        try:
            driver.quit()
            logging.info("Driver closed successfully.")
        except NameError:
            logging.warning("Driver was not initialized, so it cannot be closed.")

# Run the Program 
if __name__ == "__main__":
    main()
