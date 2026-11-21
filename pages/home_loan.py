from playwright.sync_api import Page,expect
import pytest_check as check
class HomeLoan:
    def __init__(self,page:Page):
        self.page=page
        self.application_type=page.locator("[id=\"application_type_single\"]")
        self.no_of_dependants = page.locator("[title=\"Number of dependants\"]")
        self.number=page.get_by_label("Number of dependants").select_option("0")
        self.annual_income_before = page.get_by_role("textbox", name="Your annual income (before")
        self.other_annual_income=page.get_by_role("textbox", name="Your annual other income (")
        self.expenses = page.locator("[id=\"expenses\"]")
        self.home_loan = page.locator("[id=\"homeloans\"]")
        self.other_loan = page.locator("[id=\"otherloans\"]")
        self.montly_commit = page.get_by_role("textbox", name="Other monthly commitments")
        self.credit_limit = page.get_by_role("textbox", name="Total credit card limits")
        self.borrow_calc_button = page.locator("[id=\"btnBorrowCalculater\"]")

    def select_application_type(self):
          self.application_type.click()

    def select_no_applicants(self):
         self.no_of_dependants.click(force=True)

    def add_income(self,income_before,other_income):
         self.annual_income_before.click()
         self.annual_income_before.fill(income_before)
         self.other_annual_income.click()
         self.other_annual_income.fill(other_income)

         
    def add_otherexpenses(self,exp):
         self.expenses.click()
         self.expenses.fill(exp)
