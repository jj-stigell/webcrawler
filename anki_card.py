from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def main():

    driver = webdriver.Chrome("/home/jj-stigell/Downloads/chromedriver") #path to chromedriver, temp for now
    sentences_jpn = []  # sentence in japanese
    sentences_eng = []  # sentence in english
    grammar = []  # grammar point

    driver.get("https://jlptsensei.com/learn-japanese-grammar/%e3%81%8b%e3%81%88%e3%81%a3%e3%81%a6-kaette-meaning/")

    content = driver.page_source
    soup = BeautifulSoup(content)

    for a in soup.find_all('a', href=True, attrs={'class': 'example-cont py-5'}):
        sentence_jpn = a.find('p', attrs={'class': 'm-0 jp'})
        sentence_eng = a.find('div', attrs={'class': 'alert alert-primary'})
        sentences_jpn.append(sentence_jpn.text)
        sentences_eng.append(sentence_eng.text)

    df = pd.DataFrame({'Expression': sentences_jpn, 'Meaning': sentences_eng})
    df.to_csv('products.csv', index=False, encoding='utf-8')


main()
