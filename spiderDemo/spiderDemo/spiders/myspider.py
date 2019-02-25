import scrapy
from scrapy.selector import HtmlXPathSelector

class BlogSpider(scrapy.Spider):
    name = 'schoolSpider_v1.0'
    start_urls = ['https://www.4icu.org/us/']
    allowed_domains = ["4icu.org"]
    # 'https://blog.scrapinghub.com'
    #'https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2'

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        #hxs = HtmlXPathSelector(response)
        #titles = response.xpath("//span[@data-component-type = 's-search-results']")
        titles = response.xpath("//tbody")
        for titles in titles:
            #item = SpiderdemoItem()
            item = []
            #yield {'link': titles.select("//a/@href").extract()}
            item["link"] = titles.xpath("./td[0]/a/text()").extract()[0]

            # self.logger.info(item["link"])
            #yield {'title': titles.select("//span[@class = 'a-size-medium a-color-base a-text-normal']").extract()}
            #item["title"] = titles.xpath("./td[1]//text()").extract()[0]

            #yield {'price': titles.select("//span[@class = 'a-price-whole']").extract()}
            #item["price"] = titles.xpath("//span[@class = 'a-price-whole']").extract()
            yield item
        #print(result)
        #return result
