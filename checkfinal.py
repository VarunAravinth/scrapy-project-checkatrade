# -*- coding: utf-8 -*-
import scrapy


class CheckSpider(scrapy.Spider):
    name = "check"
    start_urls = [
		"https://www.checkatrade.com/Directory/A",
	]
    person=[]
    contact1=[]
    contact2=[]
    website=[]

    def parse(self, response):
        data=response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[2]/div/table/tbody/tr')
        linker=[]
        address=[]
        member=[]
        reports=[]
        rating=[]
        url=[]
        
        
        for each in data[:]:

            linker.append(each.xpath('td[1]/a/@href').extract_first().strip())
            address.append(each.xpath('td[2]/text()').extract_first().strip())
            member.append(each.xpath('td[3]/text()').extract_first().strip())
            reports.append(each.xpath('td[4]/text()').extract_first().strip())
            rating.append(each.xpath('td[5]/text()').extract_first().strip())    
            
        for link in linker:
            #temp = url.append(response.urljoin(link))
            temp='http://www.checkatrade.com'+link+'services.aspx'
            yield scrapy.Request(temp , callback=self.parse_results, dont_filter=True)
        
    def parse_results(self, response):
        items={}
        
        items['person'] = response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[1]/div[2]/div/div[1]/div/div/text()').extract_first().strip()
        items['company name'] = response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[1]/div[2]/div/div[1]/div/h1/text()').extract_first()
        items['phonenumber'] = response.xpath('//*[@id="ctl00_ctl00_content_ctlMobile"]/text()').extract_first()
        items['phonenumber2'] = response.xpath('//*[@id="ctl00_ctl00_content_ctlMobile"]/text()').extract_first()
        items['website'] = response.xpath('//*[@id="ctl00_ctl00_content_ctlWeb"]/text()').extract_first()
        items['rating'] = response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[1]/div[2]/div/div[2]/span[1]/text()').extract_first().strip()
        items['reviews:'] = response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[1]/div[2]/div/div[2]/span[2]/span/text()').extract_first().strip()


        main=[]
        sub=[]
        
        main.append(response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[2]/div[1]/div/div[1]/ul/li["some"]/span/span/text()').extract())
        sub.append(response.xpath('//*[@id="ctl00_ctl00_ctlMain"]/div[2]/div[1]/div/div[2]/ul/li["some"]/span/span/text()').extract())

        for num,each in enumerate(main):
            temp='main_name'+str(num)
            items[temp] = each

        for num2,each2 in enumerate(sub):
            tempp = 'sub_name'+str(num2)
            items[tempp] =each2
        
            

        yield items



        
        
        
                        
        
                



        
            
