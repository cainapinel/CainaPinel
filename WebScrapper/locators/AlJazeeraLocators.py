from selenium.webdriver.common.by import By


class AlJazeeraLocators:
    ABA_TICKETS_HREF = "#/dados/tickets"
    ABA_EXPORTAR_HREF = "#/dados/tickets/exportar/"
    CLASS_NAME_SEARCH_BUTTON = 'site-header__search-trigger'
    CLASS_SEARCH_BAR_INPUT = (By.CLASS_NAME, 'search-bar__input')
    ID_SEARCH_SORT_TOPIC = (By.ID, 'search-sort-option')
    SORT_BY_DATE = 'Date'
    CLASS_RESULT_LIST = (By.CLASS_NAME, 'search-result__list')
    TAG_NAME_ARTICLE = (By.TAG_NAME, 'article')
    FOOTER_TAG_NAME = (By.TAG_NAME, 'footer')
    CLASS_BUTTON_CLICK_HERE_TO_SHOW_MORE_CONTENT = (By.CLASS_NAME, 'show-more-button grid-full-width')