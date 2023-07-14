# Crawl Data Examples

![license](https://img.shields.io/github/license/nitsvutt/crawl-data-examples)
![stars](https://img.shields.io/github/stars/nitsvutt/crawl-data-examples)
![forks](https://img.shields.io/github/forks/nitsvutt/crawl-data-examples)

## Abstract

This repository contains 2 underlying ways to crawl data from a specific website. There are **HTML crawling** with _Python_, _Selenium_, _BeautifulSoup_, and **API crawling** with _Python_, _requests_.

## Approach

### HTML crawling
  
The **HTML crawling** way ussualy is benefical to coping with highly secure website that requires login and does not have API, data only represents by html syntax.

- _Selenium_ bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. In this case, I use it to interact with the website automaticaly.

- _BeautifulSoup_ is a Python package for parsing HTML and XML documents.

### API crawling
The **API crawling** way is the easiest and fastest way to crawl data, but it requires you to have an specific API.

-  _requests_ is an HTTP client library for the Python programming language allowing you to send HTTP requests using Python.
