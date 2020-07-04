# Selenium-demo
Find an item in a website and print it to the console using Selenium.  
  
# Usage example:  
Create an object:  
url = 'https://www.amazon.com/'  
example = AmazonExample(url)  
  
Display departments list:  
example.print_departments()  
  
Select department to search an item:  
department = 'Sports & Outdoors'  
  
item = 'basketball'  

Sort items by price low to high (see documentation in the code):  
sort_price_by = 1  

Select the second item (zero based):  
item_index = 1  
delim = 'string to split into separate items'  
  
example.search_item(department, item, sort_price_by)  
example.get_item_by_index(item_index, delim)  
 

