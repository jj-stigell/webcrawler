from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def get_next_grammar():
    pass



def generate_csv(sentences_jpn, sentences_eng, grammar_rules, grammar_tables):
    df = pd.DataFrame({'Expression': sentences_jpn, 'Meaning': sentences_eng, 'Vocabulary': grammar_rules, 'Table': grammar_tables})
    df.to_csv('cards.csv', index=False, encoding='utf-8')
    return True


def main():
    driver = webdriver.Chrome("/home/jj-stigell/Downloads/chromedriver")  # path to chromedriver, change if needed
    sentences_jpn = []  # sentences in japanese
    sentences_eng = []  # sentences in english
    grammar_rules = []  # grammar points in text
    grammar_tables = []  # grammar tables in html format

    # TODO go through all grammar pages, function that gives new url to driver, implement in loop?
    # TODO add grammar point title so it will be easier to find grammar page if manual fixing required
    driver.get("https://jlptsensei.com/learn-japanese-grammar/%e3%81%8b%e3%81%ad%e3%81%aa%e3%81%84-kanenai-meaning/")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    grammar = soup.find('div', class_='grammar-notes my-3')  # search the grammar information
    grammar_table = soup.find('table', class_='table table-bordered table-sm usage')

    split_grammar = grammar.text.split('Click the', 1)  # delete the advertisement and everything after that
    stripped_grammar_point = split_grammar[0].replace(';', ',')  # replace ; with , so there is no problems with csv

    i = 1
    text = 'example_'

    while i < 10:
        search = text + str(i)  # example_1, example_2 etc. for all example sentences
        for a in soup.find_all(id=search):
            sentence_jpn = a.find('p', class_='m-0 jp')
            sentences_jpn.append(sentence_jpn.text)
            sentence_eng = a.find('div', class_='alert alert-primary')
            sentences_eng.append(sentence_eng.text)
            grammar_rules.append(stripped_grammar_point)
            grammar_tables.append(grammar_table)
        i += 1

    if generate_csv(sentences_jpn, sentences_eng, grammar_rules, grammar_tables):
        print("New csv created succesfully")
    else:
        print("something went wrong, terminating the process")


main()
