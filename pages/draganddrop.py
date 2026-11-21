from playwright.sync_api import Page
class DragandDrop:
    def __init__(self,page:Page):
        self.page=page
        self.simpledrag=page.get_by_role("tabpanel", name="Simple").get_by_text("Drag Me")
        self.simpledrop=page.locator("[id=\"droppable\"]").get_by_text("Drop Here",exact=True)

    def drag_drop(self):
        self.simpledrag.drag_to(self.simpledrop)