from playwright.sync_api import Page,expect
import pytest_check as check
class TextBox:
    def __init__(self,page:Page):
        self.page=page
        self.fullname=page.locator("[id=\"userName\"]")
        self.email=page.locator("[id=\"userEmail\"]")
        self.currentAddress=page.get_by_role("textbox", name="Current Address")
        self.permenantAddress=page.locator("[id=\"permanentAddress\"]")

    def add_text(self,fname,email,caddress,paddress):
        # Hard assert negative assertion
        # expect(self.page).not_to_have_title("test")
        #Hard assert (+ve)
        # expect(self.page).to_have_title("test")
        # Soft assert
        page_title = self.page.title()
        check.not_equal(page_title,"test")
        self.fullname.fill(fname)
        self.email.fill(email)
        self.currentAddress.fill(caddress)
        self.permenantAddress.fill(paddress)
        self.permenantAddress.clear()
        self.currentAddress.click()
        self.currentAddress.press("Control+A")
        self.currentAddress.press("Control+C")
        self.permenantAddress.click()
        self.permenantAddress.press("Control+V")
        self.fullname.focus()
        self.fullname.blur()
        self.page.pause()

    def read_text(self):
        value = self.permenantAddress.input_value()
        expect(self.permenantAddress).to_contain_class("col-md-3")
        expect(self.permenantAddress).not_to_have_attribute("role","link")
        print("value is "+value)    


