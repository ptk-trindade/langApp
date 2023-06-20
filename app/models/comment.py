
class Comment:

    def __init__(self, comment_id, creator_id: int, text: str, responses = []):
        self.id = comment_id
        self.creator_id = creator_id
        self.text = text
        self.responses = responses

    def toJson(self):
        json = {
            'comment_id': self.id,
            'creator_id': self.creator_id,
            'text': self.text,
            'responses': [response.toJson() for response in self.responses]
        }
        
        return json