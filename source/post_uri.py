#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from sys import argv
from getpass import getpass
from os import system

class Uri:
    def __init__(self, connector):
        self.conn = connector
        self.url = 'https://www.urionlinejudge.com.br'
        self.login = 'email'  # id
        self.psswrd = 'password'  # id
        self.btn_login = 'send-green.send-right'  # class
        self.logged = 'h-user'  # class
        self.search_question = 'q'  # id
        self.btn_search_question = 'send-red'  # class
        self.result = "//a[@href='/judge/pt/problems/view/"  # xpath
        self.btn_send_question = "//a[@href='/judge/pt/runs/add/"  # xpath
        self.combox_language = "language-id"  # id
        self.code_frame = "ace_scroller"  # class
        self.code_edit = "ace_text-input"  # class
        self.btn_send_code = "send-green"  # class

    def log(self, email, senha):
        self.conn.find_element_by_id(self.login).send_keys(email)
        self.conn.find_element_by_id(self.psswrd).send_keys(senha)
        self.conn.find_element_by_class_name(self.btn_login).click()

    def goto_uri(self):
        self.conn.get(self.url)

    def question(self, number):
        self.conn.find_element_by_id(self.search_question).send_keys(number)
        self.conn.find_element_by_class_name(self.btn_search_question).click()
        self.conn.find_element_by_xpath(self.result+ number+ "']").click()
        self.conn.find_element_by_xpath(self.btn_send_question + number + "']").click()

    def select_language(self):
        combox = Select(self.conn.find_element_by_id(self.combox_language))
        combox.select_by_value('5')

    def clear_code_frame(self):
        self.conn.find_element_by_class_name('ace_text-input').send_keys(Keys.LEFT_CONTROL, 'a')
        self.conn.find_element_by_class_name('ace_text-input').send_keys(Keys.DELETE)

    def write_code(self, source):
        with open(source, 'r') as file:
            code = file.read().splitlines()

        for line in code:
            self.conn.find_element_by_class_name('ace_text-input').send_keys(line)
            self.conn.find_element_by_class_name('ace_text-input').send_keys(Keys.ENTER)
            self.conn.find_element_by_class_name('ace_text-input').send_keys(Keys.HOME)

    def commit(self):
        btn_send = self.conn.find_element_by_class_name(self.btn_send_code)
        self.conn.execute_script("arguments[0].scrollIntoView();", btn_send)
        btn_send.click()

if __name__ == '__main__':
    options = Options()
    options.add_argument("--headless")
    brw = webdriver.Firefox(firefox_options=options)
    #brw = webdriver.Firefox()
    system('clear')
    nav = Uri(brw)
    nav.goto_uri()
    nav.log(input('Login:'), getpass("PassWord:"))
    nav.question(argv[1])
    nav.select_language()
    nav.clear_code_frame()
    nav.write_code(argv[2])
    nav.commit()
    print('Code Commited!')
