from playwright.sync_api import Page
class Alerts:
    def __init__(self,page:Page):
        self.page=page
        self.simple_alert=page.locator("[id=\"alertButton\"]")
        self.confirm_alert = page.locator("[id=\"confirmButton\"]")
        self.prompt_alert = page.locator("[id=\"promtButton\"]")

    
    def click_alertbtn(self):
        self.page.pause()
        # with self.page.expect_event("dialog")as dialog_info:
        #     self.page.wait_for_timeout(5000)
        #     self.simple_alert.click()
        # dialog = dialog_info.value
        # dialog.accept()
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.simple_alert.click()

    def click_confirmalert(self):
        # with self.page.expect_event("dialog")as dialog_info:
        #     self.confirm_alert.click()
        # dialog = dialog_info.value
        # dialog.dismiss()
        self.page.once("dialog",lambda dialog:dialog.dismiss())
        self.confirm_alert.click()

    def click_promptalert(self):
        # with self.page.expect_event("dialog")as dialog_info:
        #     self.prompt_alert.click()
        # dialog = dialog_info.value
        # dialog.accept("testing") 
        # # Wait for selector
        # self.prompt_alert.wait_for(state="visible") 
        # self.page.wait_for_load_state("load")
        # self.page.wait_for_url("")
        self.page.once("dialog",lambda dialog:dialog.accept("testing"))
        self.prompt_alert.click()  
        self.page.pause()           