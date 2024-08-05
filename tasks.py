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
    news_tags = ast.literal_eval(news_tags_str)
    period_months = item.payload.get('period_months')
    webscrapper = WebScrapper(news_tags=news_tags, period_months=period_months)
    aljazera, data_scrapped = webscrapper.webscrape_aljaeera()
    if aljazera == 'fail':
        raise TypeError('THERE WAS AN FATAL ERROR')
    unique_data = {entry['title']: entry for entry in data_scrapped}.values()
    df = pd.DataFrame(unique_data)
    df.to_excel('.\\output\\scraped_data.xlsx', index=False, engine='openpyxl', sheet_name='Aljazeera')
    info('News scraped')
