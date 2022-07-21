from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.disneyplus.com/en-gb/home")
