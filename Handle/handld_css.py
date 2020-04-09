import Page

class HandleCss(Page.PageCss):

    # 断言文章标题是否存在
    def assert_art_exist(self):
        obj = self.get_art_fea()
        assert True if obj else False