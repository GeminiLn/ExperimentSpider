#coding:utf-8

from bs4 import BeautifulSoup
import re
import urllib
import spider_main, data_outputer, html_download, url_manager
import time
page_url = 'https://experiment.com/discover?order=newest'

class HtmlParser(object):
    
    def __init__(self):
        self.downloader = html_download.HtmlDownloader()
        self.outputer = data_outputer.DataOutputer()
        self.urls = url_manager.UrlManager()
    
    def get_new_urls(self, MainHtml):
        new_urls = set()
        soup = BeautifulSoup(MainHtml, "html.parser") 
        links = soup.find_all('a',class_ = re.compile("project-link"), href = re.compile("/projects/"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_res_data(self, page_url, soup):
        res_data = {}
        
        print ('First Craw  ' + page_url)
        spider_main.project_num += 1
        spider_main.project_hash[page_url] = spider_main.project_num
        res_data['Project ID'] = spider_main.project_num
        res_data['Current Date'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        res_data['Project href'] = page_url
        res_data['Project Title'] = soup.find('div',class_="project-page").find('div', class_="container").find('h1',class_="title").get_text()
        res_data['Res Institution'] = soup.find('div', class_="tags").find('div',class_="tag").get_text()
        successful = soup.find('div',class_='state-indicator state-')
        if successful != None and successful.get_text() == 'Successfully Funded' :
            res_data['Funded'] = soup.find('div',class_="funding-box").find_all('span',class_="focus-stat")[1].get_text()
            res_data['Funded Goal'] = 'N/A'
            res_data['Time left'] = 0
            res_data['isSu'] = 1
        if successful != None and successful.get_text() == 'Campaign Ended' :
            res_data['Funded'] = soup.find('div',class_="funding-box").find_all('span',class_="focus-stat")[1].get_text()
            res_data['Funded Goal'] = 'N/A'
            res_data['Time left'] = 0
            res_data['isSu'] = 1
        if successful == None :
            stats = soup.find('div',class_="funding-bar-stats").find_all('div',class_="stat")
            res_data['Funded'] = stats[0].find('span').get_text()
            res_data['Funded Goal'] = stats[1].find('span').get_text()
            res_data['Time left'] = soup.find('div',class_="funding-bar-stats").find('div',class_="stat float-right text-right").find('span').get_text()
            res_data['isSu'] = 0
        res_data['Pledged'] = soup.find('div',class_="funding-raised").find('span',class_="focus-stat").get_text()
        res_data['Backers'] = soup.find('li',class_="backer-stat first").find('span',class_="stat-number").get_text()
        res_data['Lab notes'] = 0
        Lab_Notes = soup.find('a',class_='drilldown-link more-updates-link')
        if Lab_Notes != None :
            res_data['Lab notes'] = Lab_Notes.find('span').get_text()
        categorys = soup.find('div',class_="hero").find_all('a',)
        
        res_data['Category 1'] = ''
        res_data['Category 2'] = ''
        i = 1
        for category in categorys:
            if re.compile(r'/discover').match(category['href']) :
                res_data['Category '+str(i)] = category.get_text()
                i += 1
        
        res_data['About This Project'] = soup.find('div',class_="project-page-content").find('p').get_text()
        what = soup.find('section',id="ask-the-scientists").find_all('h3',class_="question")
        res_data['Research Context'] = what[0].next_sibling.get_text()
        res_data['Project Significance'] = what[1].next_sibling.get_text()
        res_data['Project Goal'] = what[2].next_sibling.get_text()
        endorse = soup.find('section', id="endorsements")
        if endorse != None :
            res_data['Endorsement'] = len(endorse.find_all('div',class_="col-md-6"))
        else :
            res_data['Endorsement'] = 'N/A'
        res_ers = soup.find('section',id = "team").find('div',class_="col-md-5").find_all('div',class_="researcher")
        i = 0
        for res_er in res_ers:
            spider_main.researcher_num += 1
            i += 1
            reser_href = res_er.find('div',class_="media-img").find('a')['href']
            res_data['Researcher_href'+ str(i)] = reser_href[22:]
            time.sleep(5)
            self._get_reser_data(reser_href[22:])
        res_data['Reser_num'] = i 
        if res_data['isSu'] == 0 :
            self.urls.add_not_suc_url(page_url)
        
        self.outputer.output_pro_data(res_data)
    
    
    
    def _get_reser_data(self, href):
        reser_data = {}
        
        full_url = urllib.parse.urljoin(page_url,href)
        html_cont = self.downloader.download(full_url)
        soup = BeautifulSoup(html_cont, "html.parser")
        reser_data['Reser Number'] = spider_main.researcher_num
        reser_data['Researcher Href'] = href
        reser_data['Name'] = soup.find('h1',class_="name").get_text()
        if soup.find('p',class_="title") != None :
            reser_data['Title'] = soup.find('p',class_="title").get_text()
        else :
            reser_data['Title'] = ''
        if soup.find('p',class_="affiliates") != None :
            reser_data['Affiliates'] = soup.find('p',class_="affiliates").get_text()
        else :
            reser_data['Affiliates'] = ''
        if soup.find('p',class_="biography") != None :
            reser_data['Biography'] = soup.find('p',class_="biography").get_text()
        else :
            reser_data['Biography'] = ''
        reser_data['Joined Date'] = soup.find('span',class_="label").next_sibling
        Twitter = soup.find_all('p',class_="mtm")
        if len(Twitter) > 1:
            reser_data['Twitter'] = Twitter[1].find('a')['href']
        else :
            reser_data['Twitter'] =''
        achievements = soup.find_all('p',class_="achievement-title")
        reser_data['Achievement'] = ''
        if len(achievements) > 0:
            for achievement in achievements:
                reser_data['Achievement'] += achievement.get_text()
                reser_data['Achievement'] += '\n'
        pros = soup.find_all('div',class_="project-summaries")
        i = 0
        if len(pros) > 0 : 
            cur_pros = pros[0].find_all('a',class_="project-link")
            for cur_pro in cur_pros:
                i += 1
                reser_data['user-projects'+str(i)] = cur_pro['href']
        reser_data['user-pro num'] = i;
        i = 0
        if len(pros) > 1 :
            backed_pros = pros[1].find_all('a',class_="project-link")
            for backed_pro in backed_pros:
                i += 1
                reser_data['Backed Projects'+str(i)] = backed_pro['href']
        reser_data['backed num'] = i
        self.outputer.output_reser_data(reser_data)
        
        
    
    def parse(self, page_url, html_cont):
        soup = BeautifulSoup(html_cont, "html.parser")      
        self._get_res_data(page_url, soup)

    
    def updateParser(self, up_url, html_cont, T):
        up_data = {}
        
        spider_main.update_num += 1
        
        print ('Update  ' + up_url)
        soup = BeautifulSoup(html_cont, "html.parser")
        up_data['Project ID'] = spider_main.project_hash[up_url]
        up_data['Project href'] = up_url
        up_data['Date'] = 'T+' + str(T)
        up_data['Pledged'] = soup.find('div',class_="funding-raised").find('span',class_="focus-stat").get_text()
        successful = soup.find('div',class_='state-indicator state-')
        if successful != None and successful.get_text() == 'Successfully Funded' :
            up_data['Funded'] = soup.find('div',class_="funding-box").find_all('span',class_="focus-stat")[1].get_text()
            up_data['Time left'] = 0
            up_data['Fail'] = 'Successful'
        if successful != None and successful.get_text() == 'Campaign Ended' :
            up_data['Funded'] = soup.find('div',class_="funding-box").find_all('span',class_="focus-stat")[1].get_text()
            up_data['Time left'] = 0
            up_data['Fail'] = 'Fail'
        if successful == None :
            stats = soup.find('div',class_="funding-bar-stats").find_all('div',class_="stat")
            up_data['Funded'] = stats[0].find('span').get_text()
            up_data['Time left'] = soup.find('div',class_="funding-bar-stats").find('div',class_="stat float-right text-right").find('span').get_text()
            up_data['Fail'] = 'Continue'
        up_data['Lab notes'] = 0
        Lab_Notes = soup.find('a',class_='drilldown-link more-updates-link')
        if Lab_Notes != None :
            up_data['Lab notes'] = Lab_Notes.find('span').get_text()

        if up_data['Fail'] == 'Continue' :
            self.urls.add_not_suc_url(up_url)
            
        self.outputer.update_pro_data(up_data,spider_main.update_num)



