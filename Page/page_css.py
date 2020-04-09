from selenium.webdriver.common.by import By
import Base

class PageCss(Base.BaseAction):

    art_fea = By.XPATH, "//*[contains(@test, '划分和电话')]"

    def get_art_fea(self):
        return self.get_element(self.art_fea)


