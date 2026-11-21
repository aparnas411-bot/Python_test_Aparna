from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from pages.registration import Registration
from utils.utils import Utils

@then("I click the radio button")
def click_radiobtn(page:Page):
    radio_obj=Registration(page)
    radio_obj.select_radio()

@then("I click the check box")
def click_checkbox(page:Page):
    checkbox_obj=Registration(page)
    checkbox_obj.select_checkbox() 

@then("I select the dropdown value")
def select_dropdownvalue(page:Page):
    dropdown_obj =Registration(page)
    dropdown_obj.select_dropdown()          

    