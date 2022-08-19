# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
new_soup = soup(html, 'html.parser')
slide_elem = new_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()


# ##  D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# a. Using a for loop, iterate through the tags or CSS element
for i in range(4):
    # Create an empty dictionary, hemispheres = {}, inside the for loop
    hemispheres = {}
    # i. click on each hemisphere link
    browser.find_by_css('a.product-item h3')[i].click()
    # Loop through the full-resolution image URL, click the link, find the Sample image anchor tag
    full_res_elem = browser.links.find_by_text('Sample').first
    # ii. navigate to the full-resolution image page
    img_url = full_res_elem['href']
    title = browser.find_by_css('h2.title').text
    # iii. retrieve the full-resolution image URL string and title for the hemisphere,
    # Save the full-resolution image URL string as the value for the img_url,
    hemispheres["img_url"] = img_url
    # Save the hemisphere image title as the value for the title
    hemispheres["title"] = title
    # add the dictionary with the image URL string and the hemisphere image title to the list
    hemisphere_image_urls.append(hemispheres)
    # iv. use browser.back() to navigate back to the beginning to get the next hemisphere image
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

browser.quit()

