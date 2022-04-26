#O parakatw crawler koitaei sto sitemap tou bbc kai katebazei tis html selides gia kathe arthro. Xrhsimopoihthike to srappy gia thn ylopoihsh tou.

#Ta imports mas
from scrapy.spiders import SitemapSpider
import pathlib
import os
import scrapy

#To spider mas
class MySpider(SitemapSpider):
    name = 'bbc'
    download_delay = 0.5
    sitemap_urls = ['https://www.bbc.co.uk/sitemaps/https-index-uk-news.xml'] #to sitemap pou kanoume crawl
    
    #dhmiourgia tou fakelou pou tha apothikeutoun ta html mas
    if not os.path.exists('news'):
        os.mkdir('news')
    
    #edw kanoume parse tis seldies kai tis apothikeuoume
    def parse(self, response):
        page = response.url.split("/")[-2:]
        #print(response.body)
        #print(page)
        filename = f'news/{page[1]}.html'
        name = os.path.join(os.path.abspath(os.getcwd()), filename)
        #print("\n" + name + "\n")
        with open(filename, 'wb') as f:
            f.write(response.body)
            