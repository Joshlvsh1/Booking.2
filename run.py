from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.booking.com/");

with Booking() as bot:
    bot.land_first_page()
    print("Exiting....")

