from pytest_bdd import given, then, parsers
from playwright.sync_api import Page
from pages.alerts import Alerts

@then ('I handled all the alerts')
def handlingalerts(page:Page):
    alert_obj =Alerts(page)
    alert_obj.click_alertbtn()
    alert_obj.click_confirmalert()
    alert_obj.click_promptalert()
    