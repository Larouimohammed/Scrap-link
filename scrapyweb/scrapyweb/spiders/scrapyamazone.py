
import scrapy
from scrapy.linkextractors import LinkExtractor
class ScrapyamazoneSpider(scrapy.Spider):
    name = "amazonscrapyweb"
    # update this link with your purpose
    start_urls = ["https://aws.amazon.com/fr/about-aws/global-infrastructure/regions_az/"]
    
    def parse(self, response):
            link_extractor = LinkExtractor() 
            links = link_extractor.extract_links(response)

            for link in links: 
             yield {"url": link.url, "text": link.text}
           

            

      
         


     