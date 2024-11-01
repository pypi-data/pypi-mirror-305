from .get_downloadable_links import get_links
from .download import download

class ApaDown():

    def __init__(self):
        self.base_url = input("base url: ")
        self.output_folder = input("output folder: ")

    def start(self):
        _, file_ = get_links(self.base_url, output_file=self.output_folder+"/links.txt")
        download(file_, output_dir=self.output_folder)