from selenium import webdriver
from bs4 import BeautifulSoup

class Parser():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.depart_info_url = "https://www.cqut.edu.cn/tzgg/bmtz.htm"
        self.school_info_url = "https://www.cqut.edu.cn/tzgg/xxtz1.htm"

    def parse(self):
        self.driver.get(self.depart_info_url)
        source = self.driver.page_source
        soup = BeautifulSoup(source,"lxml")
        self.depart_date_divs = list(map(lambda x:x.text,soup.select(".day.fs36")))
        self.depart_title_divs = list(map(lambda x:x.text,soup.select(".title.fs16")))

        self.driver.get(self.school_info_url)
        source = self.driver.page_source
        soup = BeautifulSoup(source,"lxml")
        self.school_date_divs = list(map(lambda x:x.text,soup.select(".time.fs14")))
        self.school_title_divs = list(map(lambda x:x.text,soup.select(".title.fs16")))
        self.driver.quit()
