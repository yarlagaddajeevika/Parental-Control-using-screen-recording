from selenium import webdriver
import time

# Replace with your own values
takeout_url = "https://takeout.google.com/settings/takeout"
api_key = "AIzaSyA5KqXSCOtwFfTuoJ3r3_nlIxirnxBLyl4"

# Set up the Selenium webdriver
options = webdriver.FirefoxOptions()
options.headless = True  # Run Firefox in headless mode
driver = webdriver.Firefox(options=options)

# Log in to Google
driver.get("https://accounts.google.com")
time.sleep(2)
driver.find_element("id","identifierId").send_keys("trial0parental@gmail.com")
driver.find_element("id","identifierNext").click()
time.sleep(2)
driver.find_element("type","password").send_keys("chinni1$")
# driver.find_element("id","passwordNext").click()
time.sleep(2)

# # Navigate to the Google Takeout page
# driver.get(takeout_url)
# time.sleep(2)

# # Find and click the "Deselect All" button
# deselect_button = driver.find_element_by_css_selector("div.gb_Df > div > button")
# deselect_button.click()
# time.sleep(1)

# # Find and select the "YouTube and YouTube Music" checkbox
# youtube_checkbox = driver.find_element_by_css_selector("div[id^='exportService']:nth-of-type(4) input[type='checkbox']")
# youtube_checkbox.click()
# time.sleep(1)

# # Find and click the "All YouTube data included" dropdown
# youtube_dropdown = driver.find_element_by_css_selector("div[id^='exportService']:nth-of-type(4) div[jsname='yfjG6c']")
# youtube_dropdown.click()
# time.sleep(1)

# # Find and select the checkboxes for the YouTube data you want to download
# youtube_video_checkbox = driver.find_element_by_css_selector("div[id^='exportService']:nth-of-type(4) li:nth-of-type(1) input[type='checkbox']")
# youtube_video_checkbox.click()
# time.sleep(1)

# youtube_search_checkbox = driver.find_element_by_css_selector("div[id^='exportService']:nth-of-type(4) li:nth-of-type(2) input[type='checkbox']")
# youtube_search_checkbox.click()
# time.sleep(1)

# # Find and click the "OK" button to confirm the YouTube data selection
# youtube_ok_button = driver.find_element_by_css_selector("div[id^='exportService']:nth-of-type(4) button[jsname='GY6Xd']")
# youtube_ok_button.click()
# time.sleep(1)

# # Find and click the "Next" button to proceed to the export options page
# next_button = driver.find_element_by_css_selector("div[jscontroller='CwoxHf'] button[jsname='WxTTNd']")
# next_button.click()
# time.sleep(1)

# # Find and select the export options you want
# file_type_dropdown = driver.find_element_by_css_selector("div[jsname='I5eA77'] select")
# file_type_dropdown.send_keys("zip")
# time.sleep(1)

# delivery_method_dropdown = driver.find_element_by_css_selector("div[jsname='I5eA77'] div:nth-of-type(2) select")
# delivery_method_dropdown.send_keys("link")
# time.sleep(1)

# # Find and click the "Create export" button to start the export process
# create_export_button = driver.find_element_by_css_selector("div[jscontroller='CwoxHf'] button[jsname='WxTTNd']")
# create_export_button.click()
# time.sleep(1)

# # Find and copy the download URL for the export
# download_url = None
# for element in driver.find_elements_by_css_selector("div[jscontroller='bFyxl'] a"):
#     if "Download" in element.text:
#         download_url = element.get
