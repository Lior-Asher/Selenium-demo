from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from time import sleep

class AmazonExample:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url
        # Navigate to Amazon website
        self.driver.get(self.url)

    # Display departments list to choose from
    def print_departments(self):        
        search_drop_down = self.driver.find_element_by_id('searchDropdownBox')
        for option in search_drop_down.find_elements_by_tag_name('option'):
            print(option.text)
            
    # Sort items 
    # Options: 
    #   1: low to high
    #   2: high to low
    def sort_items(self, sort_option):
        # Sort by price, low to high
        sort_drop_down = self.driver.find_element_by_id('s-result-sort-select')

        if sort_option == 1:
            for option in sort_drop_down.find_elements_by_tag_name('option'):
                if 'low to high' in option.text.lower():
                    option.click()
                    break

        if sort_option == 2:
            for option in sort_drop_down.find_elements_by_tag_name('option'):
                if 'high to low' in option.text.lower():
                    option.click()
                    break

    # Search an item
    # Parameters:
    #   Department to search
    #   Item to find
    #   Sort items by price
    # Example:
    #   department: 'Sports & Outdoors'
    #   item_to_find: 'basketball'
    #   sort_price_by: 1 - low to high
    def search_item(self, department, item_to_find, sort_price_by):
        search_drop_down = self.driver.find_element_by_id('searchDropdownBox')
        for option in search_drop_down.find_elements_by_tag_name('option'):
            if option.text == department:
                option.click()
                break

        # Search an item
        search_box = self.driver.find_element_by_id('twotabsearchtextbox')
        search_box.send_keys(item_to_find)
        search_btn = self.driver.find_element_by_class_name('nav-input') 
        search_btn.click()

        # sort the items
        self.sort_items(sort_price_by)


    # Select item to print by index
    # First item's index is 0
    def get_item_by_index(self, index):
        sleep(3) # Give page componenets time to load
        page_items = self.driver.find_elements_by_class_name('sg-col-inner') # Items on the page, basketballs is this demo
        
        # page_items[3]: index 3 are the items in the center of the page
        items = page_items[3].text.split('Ships to Israel') # Split string on delimiter
        print(items[index])
