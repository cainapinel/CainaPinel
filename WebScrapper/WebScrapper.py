from selenium.webdriver.common.by import By
from WebScrapper.pages.AlJazeeraPage import AlJazeeraPage
from Xdriver.xDriver import Xdriver
from datetime import datetime
import calendar


class WebScrapper(Xdriver):
    def __init__(self,
                 download_path=None,
                 chromedriver_path=None
                 ,news_tags=None
                 ,period_months=None):
        super().__init__(headless=False,
                         download_path=download_path,
                         chromedriver_path=chromedriver_path)
 
        self.aljazeera = AlJazeeraPage(webdriver=self)
        self.news_tags = news_tags
        self.period_months = period_months
        self.stop_at_period = ''
        self.data_extracted = []
        self.get_periods()
    
    def get_periods(self):
        
        current_date = datetime.now()
        periods_list = []

        for i in range(self.period_months + 1):
            month = (current_date.month - i) % 12 or 12
            year = current_date.year - ((current_date.month - i - 1) // 12)
            
            abbreviated_month_name = calendar.month_abbr[month]

            periods_list.append(f'{abbreviated_month_name} {year}')

        self.stop_at_period = periods_list[-1]
    
    def webscrape_aljaeera(self):
        for news_topic in self.news_tags:
            print(f'Running for topic: {news_topic}')
            try:
                aljazerahomepage = self.aljazeera.acess_website()
                if aljazerahomepage is False:
                    return "fail"
                click_search_button = self.aljazeera.click_search_button()
                if click_search_button is False:
                    return "fail"
                type_news_tag = self.aljazeera.type_search_option(news_tag=news_topic)
                if type_news_tag is False:
                    return "fail"
                select_search_sort = self.aljazeera.select_search_sort()
                if select_search_sort is False:
                    return "fail"
                bring_all_periods, articles  = self.aljazeera.bring_all_periods(self.stop_at_period)
                if bring_all_periods is False:
                    return "fail"
                extract_from_articles, data_extracted = self.aljazeera.extract_from_articles(articles, search_phrases=news_topic)
                if extract_from_articles is False:
                    return "fail", data_extracted
                self.data_extracted.append(data_extracted)
            except Exception as error:
                self.driver.quit()
                print(str(error))
                return "fail", str(error)
            else:
                self.driver.quit()
                return "ok", self.data_extracted
            