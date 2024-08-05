from robocorp.tasks import task
from WebScrapper.WebScrapper import WebScrapper
import pandas as pd

webscrapper = WebScrapper()

@task
def webscrapping_aljazeera_page():
    '''This tasks webscrapes AlJazeera news'''
    aljazera, data_scrapped = webscrapper.webscrape_aljaeera()
    if aljazera == 'fail':
        raise TypeError('THERE WAS AN FATAL ERROR')
    unique_data = {entry['title']: entry for entry in data_scrapped}.values()
    df = pd.DataFrame(unique_data)
    df.to_excel('scraped_data.xlsx', index=False, engine='openpyxl', sheet_name='Aljazeera')
    print('News scraped')
