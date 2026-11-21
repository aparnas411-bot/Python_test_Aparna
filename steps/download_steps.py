from pytest_bdd import given, then, parsers
from playwright.sync_api import Page, expect
from pages.download import Download
@then(parsers.parse('I upload the file "{path}"'))
def upload_file(page:Page,path):
    download_obj=Download(page)
    download_obj.upload_item(path)

@then("I downloaded the file")
def download_file(page:Page):
    download_obj=Download(page)
    download_obj.download_file()
    

