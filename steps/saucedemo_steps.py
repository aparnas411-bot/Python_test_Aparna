from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from pages.saucedemo import SauceDemo
from utils.utils import Utils

@then(parsers.parse('I login to the application with credentials "{user}" "{pwd}"'))
def loginto_application(page:Page,user,pwd):
    saucedemo_obj=SauceDemo(page)
    saucedemo_obj.login(user,pwd)

@then(parsers.parse('I verify the page title is "{title}"'))  
def verify_pagetitle(page:Page,title):
    verify_obj=SauceDemo(page)
    verify_obj.verify_title(title)

@then(parsers.parse('I added "{num}" products in the cart'))
def add_products_incart(page:Page,num):
    add_prod_obj=SauceDemo(page)
    add_prod_obj.add_product()
    add_prod_obj.verify_count(num)
    

@then('I delete one item')
def delete_one_item(page:Page):
    delete_item_obj = SauceDemo(page)
    delete_item_obj.remove_product()

@then(parsers.parse('I verify the count is updated to "{num}"'))
def updated_count_in_cart(page:Page,num):
    update_cart_obj = SauceDemo(page)
    update_cart_obj.verify_count(num)

@then('I check out the cart')
def checkout_cart(page:Page):
    checkout_obj = SauceDemo(page) 
    checkout_obj.checkout_c()



       