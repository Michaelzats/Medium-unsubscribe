from selenium import webdriver
from time import sleep

# Create a new instance of the Chrome driver
browser = webdriver.Chrome()

# Navigate to Medium login page
browser.get(
    "https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F")

# Locate the email input element and enter your email
email_input = browser.find_element_by_name("email")
email_input.send_keys("EMAIL")

# Locate the password input element and enter your password
password_input = browser.find_element_by_name("password")
password_input.send_keys("PASSWORD")

# Click the Sign in button
submit_button = browser.find_element_by_css_selector(".button--primary")
submit_button.click()

# Wait for the user to log in and navigate to the following URL
sleep(5)
browser.get("https://medium.com/me/following")

# Click on the Following button
following_button = browser.find_element_by_css_selector(
    ".show-more.Button.Button--chromeless.u-baseColor--buttonNormal")
following_button.click()

# Locate the "Following" div container and get all "Unfollow" buttons
following_div = browser.find_element_by_css_selector(".js-followingStream")
unfollow_buttons = following_div.find_elements_by_css_selector(
    ".button--smaller.Button.Button--chromeless.u-baseColor--buttonNormal")

# Unfollow each account by clicking the "Unfollow" button
for unfollow_button in unfollow_buttons:
    unfollow_button.click()
    sleep(1)

# Close the browser
browser.quit()
