from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\sayyed.ali\\PycharmProjects\\pythonProject2\\pythonSelenium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://exchange2.tmfhorizon.com/en")

print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.refresh()
driver.back()
driver.close()
