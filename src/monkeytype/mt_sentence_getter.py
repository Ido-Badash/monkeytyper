from web_scrap import SentenceGetter

class MTsentenceGetter(SentenceGetter):
    def __init__(self):
        self.mt_url = "https://www.mturk.com/"
        super().__init__(self.mt_url)

    def get_sentence(self):
        return super().get_sentence()