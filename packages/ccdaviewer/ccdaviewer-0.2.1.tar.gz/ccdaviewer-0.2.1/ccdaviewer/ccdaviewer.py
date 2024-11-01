import os
import shutil
import requests


class CcdaViewerClient():

    def __init__(self, api_key, api_url="https://www.ccdaviewer.com"):
        self.api_key = api_key
        self.api_url = api_url

    def _preprocess_folders(self, folname:str):
        try:
            shutil.rmtree(folname)
            os.mkdir(folname)
        except:
            os.mkdir(folname)

    def convert_xml_to_html(self, src:str, dst:str|None=None, dst_folder:str|None=None, return_as_byte:bool=False):

        file = {'files': open(src, 'rb')} 
        input_data = {"api_key": self.api_key}
        response = requests.post(f"{self.api_url}/api", json=input_data, files=file)
        if return_as_byte:
            return response.content
        sname = dst if dst is not None else src.split(".xml")[0]
        dst_folder = dst_folder.replace("/", "") if dst_folder is not None else "ccda_html_files"
        if not os.path.isdir(dst_folder):
            self._preprocess_folders(dst_folder)
        with open(f"{dst_folder}/{sname}.html", "wb") as binary_file:
            binary_file.write(response.content)

        return

