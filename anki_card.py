from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/home/jj-stigell/Downloads/chromedriver")  # path to chromedriver, change if needed
sentences_jpn = []  # sentences in japanese
sentences_eng = []  # sentences in english
grammar_rules = []  # grammar points in text
grammar_tables = []  # grammar tables in html format

def get_grammar_page(first_page, start_page, end_page):

    #  in form: https://jlptsensei.com/jlpt-n2-grammar-list/page/, 40 grammar points per page
    for i in range(start_page, end_page + 1):  # go through all pages one by one, one page has 40 grammar pages
        print('Working on page ' + str(i))
        page_to_open = first_page + str(i)
        driver.get(page_to_open)

        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        x = 1

        for link in soup.find_all('a', class_='jl-link jp'):
            grammar_x = link.get('href')
            print('Working on grammar point ' + str(x) + ' :' + grammar_x)
            current_grammar_rule(grammar_x)
            x += 1


def current_grammar_rule(link):

    i = 1
    text = 'example_'

    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    grammar = soup.find('div', class_='grammar-notes my-3')  # search the grammar information
    grammar_table = soup.find('table', class_='table table-bordered table-sm usage')

    try:
        split_grammar = grammar.text.split('Click the', 1)  # delete the advertisement and everything after that
        stripped_grammar_point = split_grammar[0].replace(';', ',')  # replace ; with , so there is no problems with csv
    except AttributeError:
        print("Problem deleting the advertisement\n")

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


def generate_csv(sentences_jpn, sentences_eng, grammar_rules, grammar_tables):
    df = pd.DataFrame({'Expression': sentences_jpn, 'Meaning': sentences_eng, 'Vocabulary': grammar_rules, 'Table': grammar_tables})
    df.to_csv('cards.csv', index=False, encoding='utf-8')
    return True


def main():

    # TODO go through all grammar pages, function that gives new url to driver, implement in loop?
    # TODO add grammar point title so it will be easier to find grammar page if manual fixing required

    #  in form: https://jlptsensei.com/jlpt-n2-grammar-list/page/
    first_page = str(input("Give the first page link:\n"))
    start_page = int(input("Give the number of first page:\n"))
    end_page = int(input("Give the number of last page:\n"))

    get_grammar_page(first_page, start_page, end_page)

    if generate_csv(sentences_jpn, sentences_eng, grammar_rules, grammar_tables):
        print("New csv created succesfully")
    else:
        print("something went wrong, terminating the process")


main()
