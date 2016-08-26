#coding:utf-8
not_suc_urls = set()
temp_urls = set()
class UrlManager(object):
    
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
            
    def add_new_urls(self,urls):
        for url in urls:
            self.add_new_url(url)
            
            
    def add_not_suc_url(self, url):
        temp_urls.add(url)
    
    
    def add_not_suc_urls(self,urls):
        for url in urls:
            not_suc_urls.add(url)
            
            
    def has_new_url(self):
        return len(self.new_urls) != 0


    def has_not_suc_url(self):
        print (len(not_suc_urls))
        return len(not_suc_urls) != 0
    
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
    def get_not_suc_url(self):
        up_url = not_suc_urls.pop()
        return up_url


    
    def had_craw_url(self, url):
        if url not in self.new_urls and url not in self.old_urls:
            self.old_urls.add(url)
            return 0
        else :
            return 1
    
    

    


    

    
    
    
    
    
    


