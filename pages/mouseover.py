from playwright.sync_api import Page
class MouseOver:
    def __init__(self, page:Page):
        self.page=page
        self.clickme=page.get_by_text("Click me")
        self.linkButton=page.get_by_text("Link Button")
        
    def mouse_over(self):
        self.clickme.hover()
        self.linkButton.hover()