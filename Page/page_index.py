from selenium.webdriver.common.by import By
import Base


class PageIndex(Base.BaseAction):

    # CSS频道
    css_fea = By.XPATH, "//*[contains(@text,'css')]"

    def get_css_ele(self):
        return self.get_element(self.css_fea)