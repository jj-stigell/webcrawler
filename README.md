# webcrawler for JLPTsensei.com

Goes through all grammar points at specified pages on jlptsensei.com.
Creates structured csv file that includes all grammar rules and example sentences (jpn/eng) related to the grammar rule.

It is recommended to install adblock for the browser used, because the jlptsensei website is bloated with advertisements.

Other notes:
- robot.txt defines if scraping allowed on specific website. website.com/robot.txt

To extract data using web scraping with python, you need to follow these basic steps:

1. Find the URL that you want to scrape
2. Inspecting the Page
3. Find the data you want to extract
4. Write the code
5. Run the code and extract the data
6. Store the data in the required format 

Used libraries:

Selenium https://www.selenium.dev/
- Webtesting library. To automate browser activities.

BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Helps collecting data from html/xml files.

Pandas https://pandas.pydata.org/
- Python library for data manipulation and analyzing. Can collect and save data to desired format.
- Format used for this project csv, as ANKI support trasforming it to flash cards based on column values.
