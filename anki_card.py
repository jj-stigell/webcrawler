from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def main():
    driver = webdriver.Chrome("/home/jj-stigell/Downloads/chromedriver")  # path to chromedriver, change if needed
    sentences_jpn = []  # sentences in japanese
    sentences_eng = []  # sentences in english
    grammar_rules = []  # grammar points in text
    grammar_tables = []  # grammar tables in html format

    # TODO go through all grammar pages, function that gives new url to driver, implement in loop?
    driver.get(
        "https://jlptsensei.com/learn-japanese-grammar/%e3%81%93%e3%81%a8%e3%81%a0%e3%81%8b%e3%82%89-koto-dakara-meaning/")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    grammar = soup.find('div', class_='grammar-notes my-3')  # search the grammar information
    grammar_table = soup.find('table', class_='table table-bordered table-sm usage')

    i = 1
    text = 'example_'

    while i < 10:
        search = text + str(i)  # example_1, example_2 etc. for all example sentences
        for a in soup.find_all(id=search):
            sentence_jpn = a.find('p', class_='m-0 jp')
            sentences_jpn.append(sentence_jpn.text)
            sentence_eng = a.find('div', class_='alert alert-primary')
            sentences_eng.append(sentence_eng.text)
            grammar_rules.append(grammar.text)
            grammar_tables.append(grammar_table)
        i += 1

    df = pd.DataFrame({'Expression': sentences_jpn, 'Meaning': sentences_eng, 'Vocabulary': grammar_rules, 'Table': grammar_tables})
    df.to_csv('cards.csv', index=False, encoding='utf-8')


main()
