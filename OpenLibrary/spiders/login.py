import scrapy
from scrapy import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login/']

    def parse(self, response):
        
        yield FormRequest.from_response(
            response,
            formxpath = "//form[@id='register']",
            formdata = {
                "username" : "mohamudgull@gmail.com",
                "password" : "qwerty12345",
                "redirect"  :   "/",
                "debug_token" : "",
                "login" : "Log In"
            },
            
            callback = self.after_login
        )

    def after_login(self, response):
        if response.xpath("//*[@id='header-bar']/div[3]/details/div/ul/li[8]/form/button/text()").get() :
            print("========================================================================================")
            print("============================LOGGED IN SUCCESSFULLY======================================")
            print("========================================================================================")
        
        
