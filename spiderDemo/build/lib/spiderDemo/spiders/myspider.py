import scrapy
from scrapy.selector import HtmlXPathSelector
class BlogSpider(scrapy.Spider):
    name = 'amazonSpier_v1.4'
    allowed_domains = ['https://www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2']
    # 'https://blog.scrapinghub.com'
    start_ulrs2 = []

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        #hxs = HtmlXPathSelector(response)
        titles = response.xpath("//span[@data-component-type = 's-search-results']")

        result = []
        for titles in titles:
            item = SpiderdemoItem()
            #yield {'link': titles.select("//a/@href").extract()}
            item["link"] = titles.select("//a/@href").extract()

            self.logger.info(item["link"])
            #yield {'title': titles.select("//span[@class = 'a-size-medium a-color-base a-text-normal']").extract()}
            item["title"] = titles.select("//span[@class = 'a-size-medium a-color-base a-text-normal']").extract()

            #yield {'price': titles.select("//span[@class = 'a-price-whole']").extract()}
            item["price"] = titles.select("//span[@class = 'a-price-whole']").extract()
            yield item
        #print(result)
        #return result
