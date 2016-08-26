#-*-coding:utf8-*-
import requests
import json
import urllib.request
import time

class HtmlDownloader(object):
    
    def downloadMain(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
           'Referer': 'https://experiment.com/discover?order=newest',
           'X-Requested-With': 'XMLHttpRequest',
           'Accept': 'application/json, text/javascript, */*; q=0.01'}

        count = 0
        htmlContent = ''
        while (count < 6):
            url = "https://experiment.com/discover/more?offset="+ str(count) +"&order=newest"
            jsContent = requests.get(url, headers=headers).text
            jsDict = json.loads(jsContent)
            jsData = jsDict['cards']
            htmlContent = htmlContent + jsData + '\n'
            count += 6
            time.sleep(2)
            
        return htmlContent

    

    def download(self,full_url):
        response = urllib.request.urlopen(full_url)
        return response.read()

    
    def downloadMain60(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
           'Referer': 'https://experiment.com/discover?order=newest',
           'X-Requested-With': 'XMLHttpRequest',
           'Accept': 'application/json, text/javascript, */*; q=0.01'}

        count = 0
        htmlContent = ''
        while (count < 60):
            url = "https://experiment.com/discover/more?offset="+ str(count) +"&order=newest"
            jsContent = requests.get(url, headers=headers).text
            jsDict = json.loads(jsContent)
            jsData = jsDict['cards']
            htmlContent = htmlContent + jsData + '\n'
            count += 6
            time.sleep(2)
            
        return htmlContent
    


