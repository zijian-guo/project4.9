import Page

class HandleIndex(Page.PageIndex):

    # 点击CSS频道
    def tap_css(self):
        self.execute_tap(self.get_css_ele())