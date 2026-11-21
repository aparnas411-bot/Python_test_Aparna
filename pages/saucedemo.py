from playwright.sync_api import Page,expect
import pytest_check as check 
class SauceDemo:
    def __init__(self,page:Page):
        self.page=page
        self.username=page.locator("[id=\"user-name\"]")
        self.password=page.locator("[id=\"password\"]")
        self.login_btn=page.locator("[id=\"login-button\"]")
        self.page_title=page.locator("[id=\"login-button\"]")
        self.addtocart_btn=page.locator("[id=\"add-to-cart\"]")
        self.backtoproduct=page.locator("[id=\"back-to-products\"]")
        self.product_jacket=page.locator("[data-test=\"item-5-title-link\"]")
        self.prodcut_backpack=page.locator("[data-test=\"item-4-title-link\"]")
        self.product_tshirt=page.locator("[data-test=\"item-1-title-link\"]")
        self.shopping_cart=page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_jacket=page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]")
        self.checkout_btn=page.locator("[data-test=\"checkout\"]")
        self.cart_link = page.locator('[data-test=\"shopping-cart-link\"]')
        self.cart_count = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postcode = page.locator("[data-test=\"postalCode\"]")
        self.products_title = page.locator("[data-test=\"title\"]")
        self.continue_btn = page.locator("[data-test=\"continue\"]")
        self.finish_btn = page.locator("[data-test=\"finish\"]")
        self.complete_header = page.locator("[data-test=\"complete-header\"]")


    def login(self,user,pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def verify_title(self,title):
        expect(self.page).to_have_title(title)
   

    def add_product(self):
        self.product_jacket.click()
        self.addtocart_btn.click()
        self.backtoproduct.click()
        self.prodcut_backpack.click()
        self.addtocart_btn.click()
        self.backtoproduct.click()
        self.product_tshirt.click()
        self.addtocart_btn.click()
        self.backtoproduct.click()

    def verify_count(self,count):
        # ccount=self.cart_count.inner_text()
        expect(self.cart_count).to_have_text(count)
        
    def remove_product(self):
        self.shopping_cart.click()
        self.remove_jacket.click()

    def checkout_c(self):  
        self.checkout_btn.click()
        