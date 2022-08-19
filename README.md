# Mission-to-Mars
"To Infinity and BEYOND!" ~Buzz Lightyear

# Project Overview:

# Results:
## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
```
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
```

## Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
- Added the following to the data dictionary of the scrapping.py
```
"hemispheres": hemisphere_image(browser)
```

- Added the following scraping function below the def mars_facts() function
```
def hemisphere_image(browser):
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
    return hemisphere_image_urls

if __name__ == "__main__":
```

## Deliverable 3: Add Bootstrap 3 Components
- Before:
<img width="281" alt="image" src="https://user-images.githubusercontent.com/106962921/185714436-d407d0dc-9392-43f2-b21c-65becf482deb.png">
<img width="277" alt="image" src="https://user-images.githubusercontent.com/106962921/185714489-0f9f5281-c16d-4544-bd63-4681f222efe6.png">

- After:
<img width="277" alt="image" src="https://user-images.githubusercontent.com/106962921/185715459-8419197b-4d78-4244-bdde-4dc33b183830.png">
<img width="278" alt="image" src="https://user-images.githubusercontent.com/106962921/185715566-f696661f-7477-4612-ba66-37bd7f11513a.png">

# Summary:
This module was challenging as I learned HTML and basic writing and syntax. The web scraping was fairly straightforward although there was alot of research conducted to work through the error messages. There was also difficulty installing MongoDB as the lesson module is outdated. Overall, it was enjoyable creating my web app.

# Resources:
  - Jupyter Notebook version 6.4.8
  - Python version 3.7.13
  - VS code version 1.70.2
  - MongoDB version 6.0
  - Mongosh version 1.5.4
  - HTML
