from selenium import webdriver

# Replace the URL with the link to the TikTok video you want to download
url = "https://www.tiktok.com/@user/video/1234567890"

# Create a webdriver instance and open the URL
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load and the video to be visible
driver.implicitly_wait(10)

# Find the video element and get its source URL
video_element = driver.find_element_by_css_selector("video")
video_url = video_element.get_attribute("src")

# Use the URL to download the video
import requests

response = requests.get(video_url)

# Save the video to a file
with open("tiktok_video.mp4", "wb") as f:
    f.write(response.content)

# Close the webdriver instance
driver.quit()

from selenium import webdriver

# Replace the URL with the link to the Instagram video you want to download
url = "https://www.instagram.com/p/1234567890/"

# Create a webdriver instance and open the URL
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load and the video to be visible
driver.implicitly_wait(10)

# Find the video element and get its source URL
video_element = driver.find_element_by_css_selector("video")
video_url = video_element.get_attribute("src")

# Use the URL to download the video
import requests

response = requests.get(video_url)

# Save the video to a file
with open("instagram_video.mp4", "wb") as f:
    f.write(response.content)

# Close the webdriver instance
driver.quit()

def TDL() -> None:
    
    pass

def IDL() -> None:
    pass

