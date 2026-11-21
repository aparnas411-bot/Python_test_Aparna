from pytest_bdd import given, then, parsers
from playwright.sync_api import Page
from pages.mouseover import MouseOver
@then('I mouse over the item')
def mouseoveraction(page:Page):
    mouseover_obj=MouseOver(page)
    mouseover_obj.mouse_over()
    