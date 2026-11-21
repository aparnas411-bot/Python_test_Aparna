from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from pages.button import Button
@then("I perform all the click actions")
def perform_click(page):
    button_obj=Button(page)
    page.pause()
    button_obj.single_click()
    button_obj.double_click()
    button_obj.right_click()
    button_obj.title_fail()
