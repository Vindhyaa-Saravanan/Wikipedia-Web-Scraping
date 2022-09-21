# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:53:30 2022

@author: Vindhyaa Saravanan

WIKIPEDIA SCRAPER

Objective: To scrape data from Wikipedia pages to print summary of the six 
best selling books that have sold over 100 million copies.
"""

# IMPORTING REQUIRED MODULES
import wikipedia
import numpy as np


# PREPARING WIKIPEDIA PAGE AND SECTION NAMES
# List of titles of the books' Wikipedia pages
page_titles = ["A Tale of Two Cities","The Little Prince", 
"Harry Potter and the Philosopher's Stone", "And Then There Were None",
"Dream of the Red Chamber", "The Hobbit"]


# THE DATA FETCHING
# For each page title:
for title in page_titles:
# Loading the Wikipedia page and handling page not found exception
    try:
        wiki_page = wikipedia.WikipediaPage(title[0])
        
    except:
        wiki_page = np.NaN
        print("Page not found")
                
    # PRINTING GATHERED INFORMATION
    print("_____________________________________________________________")
    print("")
    print(title)
    print("")
    print(wikipedia.WikipediaPage(title = title).summary)
    print("")

    