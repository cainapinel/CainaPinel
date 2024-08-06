from robocorp.tasks import task
from WebScrapper.WebScrapper import WebScrapper
from robocorp import workitems
import pandas as pd
import ast
import robocorp.log
from robocorp.log import info


robocorp.log.setup_log(log_level='info')

@task
def handle_item():
    item = workitems.inputs.current
    print("Received payload:", item.payload)
    workitems.outputs.create(payload={"key": "value"})
 

@task
def webscrapping_aljazeera_page():
    '''This tasks webscrapes AlJazeera news'''
    item = workitems.inputs.current
    news_tags_str = item.payload.get('news_tags')
    print(f'News tags to search: {news_tags_str}')
    news_tags = ast.literal_eval(news_tags_str)
    period_months = item.payload.get('period_months')
    print(f'Period to search {str(period_months)}')

    webscrapper = WebScrapper(news_tags=news_tags, period_months=period_months)
    aljazera, data_scrapped = webscrapper.webscrape_aljaeera()

    if aljazera == 'fail':
        raise TypeError('THERE WAS AN FATAL ERROR')
    combined_data = []
    for data_list in data_scrapped:
        combined_data.extend(data_list)
    unique_data = {entry['title']: entry for entry in combined_data}.values()

    df = pd.DataFrame(unique_data)
    df.to_excel('.\\output\\scraped_data.xlsx', index=False, engine='openpyxl', sheet_name='Aljazeera')
    print('News scraped')
