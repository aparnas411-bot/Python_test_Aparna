from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from pages.textbox import TextBox
from utils.utils import Utils

@then(parsers.parse('I enter all details "{fname}" "{email}" "{caddress}" "{paddress}"'))
def enter_details(page:Page,fname,email,caddress,paddress):
    textbox_obj=TextBox(page)
    textbox_obj.add_text(fname,email,caddress,paddress)

      

    