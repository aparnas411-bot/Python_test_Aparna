from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from utils.utils import Utils
@given("I open the Playwright website")
def open_playwright_website(page: Page):
    page.goto("https://playwright.dev/")
@then('the page title should contain "Playwright"')
def verify_page_title(page: Page):
    expect(page).not_to_have_title("Playwright")

@given("I navigate to a webpage") 
def navigate_url(page:Page):
       utils_obj=Utils(page)
       utils_obj.launchUrl("https://playwright.dev/")

@then("I navigate to page two")   
def navigate_pagetwo(page:Page):
     utils_obj=Utils(page)
     utils_obj.launchUrl("https://demoqa.com/")   
     page.pause() 

@then("I go back")  
def navigate_back(page:Page):
     utils_obj=Utils(page)
     utils_obj.go_back1()

@then("I come forward")
def navigate_forward(page:Page):
     utils_obj=Utils(page)
     utils_obj.go_forward1()

@then("I reload the page")
def reload_page(page:Page):
     utils_obj=Utils(page)
     utils_obj.reload_page()

@then("I close the page")
def close_page(page:Page):
     utils_obj=Utils(page)
     utils_obj.close_page()

@given(parsers.parse('I navigate to a webpage "{url}"'))
def navigate_url(page:Page,url):
       utils_obj=Utils(page)
       utils_obj.launchUrl(url)




