import time
import Handle

class TestQuery:

    def setup(self):
        self.handle_index = Handle.HandleIndex()
        self.handle_css = Handle.HandleCss()

    def test_query(self):

        time.sleep(5)

        # 点击CSS频道
        self.handle_index.tap_css()

        # 断言
        self.handle_css.assert_art_exist()