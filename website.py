import webbrowser

class Web :
    def __init__(self, web : str = "https://www.facebook.com"):
        self.web =web
        
    def open_browser(self):
       return webbrowser.open(self.web)