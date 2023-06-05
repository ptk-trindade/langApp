from models.comment import Comment

class Card:
    
    def __init__(self, card_id):
        self.id = card_id

    def getComments(self) -> list[Comment]:
        
        # TODO: get comments from database

        # TODO: adjust comments structure (Eu ignoraria isso por enquanto, faz os comentários todos sem reply e aí não precisa disso)

        return []
    
    
    def addComment(self, user_id: int, text: str, parent_comment_id: int = None) -> Comment:

        # TODO: add comment to database

        # TODO: create Comment object

        return None