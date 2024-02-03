from datetime import datetime


class Comment:
    def __init__(self, text, category):
        self.text = text
        self.category = category
        self.created_at = datetime.now()

