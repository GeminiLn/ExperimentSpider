#coding:utf-8

import xlwt


class DataOutputer(object):
    def __init__(self):
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.ps = self.wb.add_sheet('Project Information')
        self.rs = self.wb.add_sheet('Researcher Information')
        self.us = self.wb.add_sheet('Project Update')
        
        
        self.ps.write(0, 0, '项目id（自行编码）')
        self.ps.write(0, 1, 'Current date')
        self.ps.write(0, 2, '项目链接href')
        self.ps.write(0, 3, 'project-title')
        self.ps.write(0, 4, 'research institution')
        self.ps.write(0, 5, 'Funded')
        self.ps.write(0, 6, 'Funding Goal')
        self.ps.write(0, 7, 'Time left')
        self.ps.write(0, 8, 'Pledged')
        self.ps.write(0, 9, 'Backers (The number of backers)')
        self.ps.write(0, 10, 'lab notes')
        self.ps.write(0, 11, 'Category1')
        self.ps.write(0, 12, 'Category2')
        self.ps.write(0, 13, 'About This Project')
        self.ps.write(0, 14, 'Research Context')
        self.ps.write(0, 15, 'Project Significance')
        self.ps.write(0, 16, 'Project Goals')
        self.ps.write(0, 17, 'Endorsement (The number of people who endorse this project)')
        self.ps.write(0, 18, 'researcher_href 1')
        self.ps.write(0, 19, 'researcher_href 2')
        self.ps.write(0, 20, 'researcher_href 3')
        self.ps.write(0, 21, 'researcher_href 4')
        
        
        self.rs.write(0, 0, 'Researcher_href （unique）')
        self.rs.write(0, 1, 'Name')
        self.rs.write(0, 2, 'Title')
        self.rs.write(0, 3, 'Affiliation')
        self.rs.write(0, 4, 'Biography')
        self.rs.write(0, 5, 'Joined Date')
        self.rs.write(0, 6, 'Twitter')
        self.rs.write(0, 7, 'Achievements')
        self.rs.write(0, 8, 'User-projects1')
        self.rs.write(0, 9, 'User-projects2')
        self.rs.write(0, 10, 'User-projects3')
        self.rs.write(0, 11, 'Backed Project1')
        self.rs.write(0, 12, 'Backed Project2')
        self.rs.write(0, 13, 'Backed Project3')
        
        
        
        self.us.write(0, 0, '项目id（自行编码）')
        self.us.write(0, 1, '项目链接href')
        self.us.write(0, 2, 'Record Date')
        self.us.write(0, 3, 'Pledged')
        self.us.write(0, 4, 'Funded')
        self.us.write(0, 5, 'The number of lab notes')
        self.us.write(0, 6, 'Time left')
        self.us.write(0, 7, 'Fail or not')
        
        
        
            
    def output_pro_data(self, pro_data):
        ID = pro_data['Project ID']
        self.ps.write(ID, 0, pro_data['Project ID'])
        self.ps.write(ID, 1, pro_data['Current Date'])
        self.ps.write(ID, 2, pro_data['Project href'])
        self.ps.write(ID, 3, pro_data['Project Title'])
        self.ps.write(ID, 4, pro_data['Res Institution'])
        self.ps.write(ID, 5, pro_data['Funded'])
        self.ps.write(ID, 6, pro_data['Funded Goal'])
        self.ps.write(ID, 7, pro_data['Time left'])
        self.ps.write(ID, 8, pro_data['Pledged'])
        self.ps.write(ID, 9, pro_data['Backers'])
        self.ps.write(ID, 10, pro_data['Lab notes'])
        self.ps.write(ID, 11, pro_data['Category 1'])
        self.ps.write(ID, 12, pro_data['Category 2'])
        self.ps.write(ID, 13, pro_data['About This Project'])
        self.ps.write(ID, 14, pro_data['Research Context'])
        self.ps.write(ID, 15, pro_data['Project Significance'])
        self.ps.write(ID, 16, pro_data['Project Goal'])
        self.ps.write(ID, 17, pro_data['Endorsement'])
        i = 1
        while (i <= pro_data['Reser_num']):
            self.ps.write(ID, 17 + i, pro_data['Researcher_href'+ str(i)])
            i += 1
        self.wb.save('Result.xls')    
            
    
    def output_reser_data(self, reser_data):
        ID = reser_data['Reser Number']
        self.rs.write(ID, 0, reser_data['Researcher Href'])
        self.rs.write(ID, 1, reser_data['Name'])
        self.rs.write(ID, 2, reser_data['Title'])
        self.rs.write(ID, 3, reser_data['Affiliates'])
        self.rs.write(ID, 4, reser_data['Biography'])
        self.rs.write(ID, 5, reser_data['Joined Date'])
        self.rs.write(ID, 6, reser_data['Twitter'])
        self.rs.write(ID, 7, reser_data['Achievement'])
        i = 1
        while (i <= reser_data['user-pro num'] and i <= 3):
            self.rs.write(ID, 7 + i ,reser_data['user-projects'+str(i)])
            i += 1
        i = 1
        while (i <= reser_data['backed num'] and i <= 3):
            self.rs.write(ID, 11 + i, reser_data['Backed Projects'+str(i)])
            i += 1
        self.wb.save('Result.xls')

    
    def update_pro_data(self, up_data, num):
        ID = num
        self.us.write(ID, 0, up_data['Project ID'])
        self.us.write(ID, 1, up_data['Project href'])
        self.us.write(ID, 2, up_data['Date'])
        self.us.write(ID, 3, up_data['Pledged'])
        self.us.write(ID, 4, up_data['Funded'])
        self.us.write(ID, 5, up_data['Lab notes'])
        self.us.write(ID, 6, up_data['Time left'])
        self.us.write(ID, 7, up_data['Fail'])
        
        self.wb.save('Result.xls')
        
    
    
    




