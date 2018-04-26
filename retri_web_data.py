# # # import flat file from web + save the file locally
# Import package
from urllib.request import urlretrieve
import pandas as pd
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Save file locally
urlretrieve(url, 'winequality-red.csv')
# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


# # # directly read the file from web without saving it locally + plot histogram
# Import packages
import matplotlib.pyplot as plt
import pandas as pd
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep=";")
# Print the head of the DataFrame
print(df.head())
# Plot histogram of the first feature in the DataFrame df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# # # read in a spreadsheet (read in all of its sheets)
### Note that the output of pd.read_excel() is a Python dictionary with sheet names as keys and corresponding DataFrames as corresponding values.
# Import package
import pandas as pd
# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheet_name = None)
# Print the sheetnames to the shell
print(xl.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(xl["1700"].head())


# # # Printing HTTP request results in Python using urllib
# Import packages
from urllib.request import urlopen, Request
# Specify the url
url = "http://www.datacamp.com/teach/documentation"
# This packages the request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Extract the response: html
html = response.read()
# Print the html
print(html)
# Be polite and close the response!
response.close()


# # # Performing HTTP requests in Python using requests (Requests 是一个最常用的library)
# Import package
import requests
# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"
# Packages the request, send the request and catch the response: r
r = requests.get(url)
# Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable text
text = r.text
# Print the html
print(text)


# # # Parsing HTML with BeautifulSoup
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = BeautifulSoup.prettify(soup)
# Print the response
print(pretty_soup)


# # # Turning a webpage into data using BeautifulSoup: getting the text
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extract the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Get the title of Guido's webpage: guido_title
guido_title = soup.title
# Print the title of Guido's webpage to the shell
print(guido_title)
# Get Guido's text: guido_text
guido_text = soup.get_text()
# Print Guido's text to the shell
print(guido_text)


# # # Turning a webpage into data using BeautifulSoup: getting the hyperlinks
# Import packages
import requests
from bs4 import BeautifulSoup
# Specify url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Print the title of Guido's webpage
print(soup.title)
# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all("a")
# Print the URLs to the shell
for link in a_tags:
    print(link.get("href"))
