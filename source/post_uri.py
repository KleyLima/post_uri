# -*- coding: utf-8 -*-

class Uri:
    def __init__(self, connector):
        self.conn = connector
        self.url = 'https://www.urionlinejudge.com.br'
        self.login = 'email'  # id
        self.psswrd = 'password'  # id
        self.btn_login = 'send-green send-right'  # class
        self.logged = 'h-user'  # class
        self.search_question = 'q'  # id
        self.btn_search_question = 'send-red'  # class
        self.question = "//a[@href='/judge/pt/problems/view/{}']".fortmat(#questao_desejada) # xpath



    def goto_uri(self):
        self.conn.get(self.url)


