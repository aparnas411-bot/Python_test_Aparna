from pytest_bdd import given, then, parsers
from playwright.sync_api import Page
from pages.draganddrop import DragandDrop
@then('I drag and drop the item')
def draganddropaction(page:Page):
    drag_dropobj=DragandDrop(page)
    drag_dropobj.drag_drop()
    