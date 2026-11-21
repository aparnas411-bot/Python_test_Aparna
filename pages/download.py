from playwright.sync_api import Page
from pathlib import Path
from datetime import datetime
import os
class Download:
    def __init__(self,page:Page):
        self.page=page
        self.download_btn=page.locator("[id=\"downloadButton\"]")
        self.upload_file=page.locator("[id=\"uploadFile\"]")
    def upload_item(self,path):
        self.upload_file.set_input_files(path)
        self.page.pause()
    def download_file(self):
        # I'm expecting a file download so the expect_download() is a listener.CWhen download happenes, the all info will be stored in download_info variable
        with self.page.expect_download() as download_info:
            self.download_btn.click()
            # to get the downloaded object
        download=download_info.value
        extension=Path(download.suggested_filename).suffix
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        # To get the default file name
        # file_name=download.suggested_filename
        file_name=f"download_{timestamp}{extension}"
        # Saving the file
        #Setting the Download folder
        download_folder=Path("Download")
        download_folder.mkdir(exist_ok=True)
        download.save_as(f"Download/{file_name}")
        file_path=Path("Download")/file_name
        os.remove(file_path)    




        