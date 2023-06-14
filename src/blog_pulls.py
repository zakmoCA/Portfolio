# from bs4 import BeautifulSoup
# import requests

# # Fetch the HTML of the page
# url = "https://medium.com/@mo.zak2047/book-notes-the-war-of-art-by-steven-pressfield-11a7d27fe059"
# response = requests.get(url)
# html = response.content

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Select the main content of the blog post
# # Replace 'article' with the correct tag or CSS selector for your website
# # Inspecting the Medium page, the 'div' with the class 'n p' seems to contain the main article content
# article = soup.find('div', {'class': 'n p'})

# # Remove class, id, and style attributes
# for tag in article():
#     if 'class' in tag.attrs:
#         del tag['class']
#     if 'id' in tag.attrs:
#         del tag['id']
#     if 'style' in tag.attrs:
#         del tag['style']

# # Print the 'clean' HTML
# print(article.prettify())
