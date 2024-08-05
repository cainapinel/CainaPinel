import os, re, requests
from selenium.webdriver.common.by import By
from WebScrapper.locators.AlJazeeraLocators import AlJazeeraLocators as LOCATORS
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class AlJazeeraPage:
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

    def acess_website(self):
        self.webdriver.got_to_url('https://www.aljazeera.com/')

    def click_search_button(self):
        try:
            elements = self.webdriver.driver.find_elements(By.TAG_NAME, 'div')
            for element in elements:
                if element.get_attribute('class') == LOCATORS.CLASS_NAME_SEARCH_BUTTON:
                    print('Search element found')
                    element.click()
                    print('Search element clicked')
                    return element
            print('Search element NOT found')
            return False
        except Exception as error:
            print(error)
            return False

    def type_search_option(self, news_tag):
        try:
            search_bar_input = self.webdriver.wait(locator = LOCATORS.CLASS_SEARCH_BAR_INPUT)
            search_bar_input.send_keys(news_tag)
            search_bar_input.send_keys(Keys.ENTER)
            return True
        except Exception as error:
            print(error)
            return False
        
    def select_search_sort(self):
        try:
            self.webdriver.wait(locator = LOCATORS.ID_SEARCH_SORT_TOPIC)
            self.webdriver.select_by_text(locator = LOCATORS.ID_SEARCH_SORT_TOPIC, visible_text = LOCATORS.SORT_BY_DATE)
            return True
        except Exception as error:
            print(error)
            return False

    def define_results_list(self):
        try:
            results_element = self.webdriver.wait(locator = LOCATORS.CLASS_RESULT_LIST)
            return results_element
        except Exception as error:
            print(error)
            return False
    
    def bring_all_periods(self, stop_period):
        self.webdriver.wait(LOCATORS.TAG_NAME_ARTICLE)
        counter = 1
        error_counter = 0
        print('Searching for periods...')
        articles = self.webdriver.driver.find_elements(By.TAG_NAME, 'article')
        while len(articles) <= 100:
            try:
                articles = self.webdriver.driver.find_elements(By.TAG_NAME, 'article')
                last_article = articles[-1]
                print(f'{len(articles)} articles found')
                print(f'Searching {counter} page results.')
                last_article_footer = last_article.find_element(By.TAG_NAME, 'footer')
                footer_text = last_article_footer.text
                if len(articles) == 100:
                    print('All articles are displayed')
                    return True, articles
                elif not stop_period in footer_text:
                    print('Period not complete at website.. Expanding results!')
                    print('Scrolling to end of page')
                    self.webdriver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    button_show_more = self.webdriver.driver.find_element(By.CLASS_NAME, 'show-more-button')
                    button_show_more.click()
                    counter += 1
                    print('Expanding results!')
                    self.webdriver.driver.execute_script("window.scrollTo(0, 0);")
                    sleep(2) 
                else:
                    print('Final period reached. All articles are displayed')
                    return True, articles
            except Exception as error:
                print(error)   
                sleep(5)
                error_counter += 1
                if error_counter > 5:
                    return False, False

    def extract_from_articles(self, articles, search_phrases):
        try:
            data = []
            for article in articles:
                title = article.find_element(By.CSS_SELECTOR, "h3.gc__title span").text
                try:
                    date = article.find_element(By.CSS_SELECTOR, "div.gc__date__date span[aria-hidden='true']").text
                except Exception:
                    date = 'Not Available'
                description_element = article.find_elements(By.CSS_SELECTOR, "div.gc__excerpt p")
                description = description_element[0].text if description_element else ""
                img_element = article.find_element(By.CSS_SELECTOR, "div.article-card__image-wrap img")
                img_url = img_element.get_attribute("src")
                search_phrase_count = title.count(search_phrases) + description.count(search_phrases)
                money_pattern = re.compile(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?|(?:\d+\s(?:dollars|USD))")
                contains_money = bool(money_pattern.search(title) or money_pattern.search(description))

                img_data = requests.get(img_url).content
                image_directory = f'{os.getcwd()}\\downloads'
                if not os.path.exists(image_directory):
                    os.makedirs(image_directory)

                img_filename = f"{title.replace('.', '')}.png"
                img_filename = re.sub(r'[\\/*?:"<>|]', "", img_filename)  
                img_path = os.path.join(image_directory, img_filename)
                with open(img_path, 'wb') as handler:
                    handler.write(img_data)

                data.append({
                            "title": title,
                            "date": date,
                            "description": description,
                            "picture_filename": img_filename,
                            "search_phrase_count": search_phrase_count,
                            "contains_money": contains_money
                        })
            return True, data
        except Exception as error:
            print(error)
            return False, None
