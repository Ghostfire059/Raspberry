from selenium import webdriver
import os

class search():
    """Contains functions linked to a book's ISBN
        - name(ISBN) return the book's title
        - creators(ISBN) return book's creators
        
    """

    def __init__(self, ISBN):
        self.__driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")
        self.__driver.get("http://chasse-aux-livres.fr/prix/"+ISBN)
    
    def name(self):
        return self.__driver.find_element_by_tag_name('h1').text

    def creators(self):
        return self.__driver.find_element_by_id('creators').text
        
    def cover(self):
        return self.__driver.find_element_by_id('book-cover').get_attribute("src")

    def all(self):
        name = self.name()
        creators = self.creators()
        cover = self.cover()
            #             #
            # TO COMPLETE #
            #             #
        return (name, creators, cover) # TO COMPLETE #
    
    def tearDown(self):
        self.__driver.close()
