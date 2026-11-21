from playwright.sync_api import Page
class Registration:
    def __init__(self,page:Page):
        self.page=page
        self.firstname=page.locator("[id=\"firstName\"]")
        self.lastname=page.locator("[id=\"lastName\"]")
        self.email=page.get_by_role("textbox", name="name@example.com")
        self.gender_male = page.get_by_text("Male", exact=True)
        self.gender_female=page.get_by_text("Female")
        self.gender_other=page.locator("[value=\"Other\"]")
        self.mobile=page.locator("[id=\"userNumber\"]")
        self.dob=page.locator("[id=\"dateOfBirthInput\"]")
        self.subjects=page.locator("[id=\"subjectsInput\"]")
        self.sports=page.get_by_role("checkbox", name="Sports")
        self.reading=page.get_by_role("checkbox", name="Reading")
        self.music=page.get_by_role("checkbox", name="Music")
        self.choosefile=page.get_by_role("button", name="Choose File")
        self.currentAddress=page.locator("[id=\"currentAddress\"]")
        self.state=page.get_by_text("Select State")
        # self.state=page.locator("[id=\"stateCity-wrapper\"] [id=\"state\"] [id=\"react-select-3-placeholder\"]")
        self.state_value=page.get_by_text("Haryana")
        self.submit_btn=page.locator("[id=\"submit\"]")
        # self.city=page.locator("div").filter(has_text=re.compile(r"^Select City$")).first


    def select_radio(self):
        self.gender_male.check()
        self.submit_btn.scroll_into_view_if_needed()
        self.page.pause()
        
    def select_checkbox(self):
        self.sports.check()
        self.page.pause()

    def select_dropdown(self):
        self.page.pause()
        # self.state.select_option(value) 
        self.state.click(force=True)
        self.state_value.click(force=True)
        self.page.pause()

           



        

