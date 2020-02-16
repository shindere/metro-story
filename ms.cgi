#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

def print_header():
  print("Content-type: text/html; charset=utf-8\r\n\r\n")
  print('<html lang="fr"><head><title>Metro Story</title></head>')
  print("<body>")

def print_footer():
  print("</body></html>")

def print_search_form():
  print("<p>Formulaire de recherche</p>")

def print_results(address):
  print("<p>Bouches situees autour du " + address + "</p>")

def print_main_content():
  form = cgi.FieldStorage()
  if form.getvalue('q') == None:
    print_search_form()
  else:
    print_results(form.getvalue('q'))



def main():
  print_header()
  print_main_content()
  print_footer()

main()
