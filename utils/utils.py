from playwright.sync_api import Page
class Utils:
    def __init__(self,page:Page):
        self.page=page

    def launchUrl(self,url):
        self.page.goto(url)

    def go_back1(self):
        self.page.go_back()

    def go_forward1(self):
        self.page.go_forward() 

    def reload_page(self):
        self.page.reload()    

    def close_page(self):
        self.page.close()           