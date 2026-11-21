from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import Error as PlaywrightError
class Button:
    def __init__(self,page:Page):
        self.page=page
        self.doubleClickme=page.get_by_role("button", name="Double Click Me")
        self.rightClickme=page.locator("[id=\"rightClickBtn\"]")
        self.clickme=page.get_by_role("button", name="Click Me", exact=True)
        self.testclick = page.locator("[id=\"leftClickBtn\"]")

    def single_click(self):
        self.clickme.click()

    def double_click(self):
        self.doubleClickme.dblclick()

    def right_click(self):
        self.rightClickme.click(button="right")

# Timeout error handling
    def test_click(self):
        try:
            self.testclick.click() 
            print("Button click sucessfully")  
        except PlaywrightTimeoutError:
            print("Login button not found")  
            self.page.screenshot(path="Screenshot/failure.png")  
            raise 

# Any operational error handling (eg: actions)
    def test_error(self):
        try:
            self.clickme.check() 
        except PlaywrightError as E:
            print(f"Error Details : {E}")
            raise

# Target close exception(browser close, crash etc)
    def target_close(self):
        try:
            self.page.close()
            self.clickme.click() 
        except PlaywrightError as E:
            print(f"Error Details : {E}")
            raise

# Assertion error handling
    def title_fail(self):
        try:
            actual_title = self.page.title() 
            expected_title = "Test Page"  
            assert actual_title==expected_title,(f"expected:{expected_title},"f"actual:{actual_title}")
        except AssertionError as E:
            print(f"Error Details : {E}")
            raise     
    