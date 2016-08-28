#coding:utf-8
import html_download, html_parser, data_outputer, url_manager
project_num = 0
project_hash = {}
researcher_num = 0
update_num = 0
import time
import sched

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = data_outputer.DataOutputer()
        
        
    def craw(self):
        MainHtml_Cont = self.downloader.downloadMain()
        Pro_urls = self.parser.get_new_urls(MainHtml_Cont)
        self.urls.add_new_urls(Pro_urls)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                self.parser.parse(new_url, html_cont)
                time.sleep(5)
            except:
                print("Craw Failed")
        
        self.urls.add_not_suc_urls(url_manager.temp_urls)
        url_manager.temp_urls = set()
    
    def update(self,i):
        while self.urls.has_not_suc_url():
            try:
                up_url = self.urls.get_not_suc_url()
                html_cont = html_cont = self.downloader.download(up_url)
                self.parser.updateParser(up_url, html_cont, i)
                time.sleep(5)
            except:
                print("Craw Failed")
            
        self.urls.add_not_suc_urls(url_manager.temp_urls)
        url_manager.temp_urls = set()  
        
        MainHtml_Cont = self.downloader.downloadMain60() 
        New_urls = self.parser.get_new_urls(MainHtml_Cont)
        for new_url in New_urls :
            if self.urls.had_craw_url(new_url) == 0 :
                html_cont = self.downloader.download(new_url)
                self.parser.parse(new_url, html_cont)
                time.sleep(5)
                
        self.urls.add_not_suc_urls(url_manager.temp_urls)
        url_manager.temp_urls = set()

if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.craw()
    schedule = sched.scheduler(time.time, time.sleep)  
    i = 0
    while i < 60 :
        obj_spider.update(i)
        time.sleep(86400)
        i += 1
    
