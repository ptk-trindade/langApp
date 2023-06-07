from models.comment import Comment

import database.db as db
import card.db as card_db


class Card:
    
    def __init__(self, card_id):
        self.id = card_id

    def getComments(self) -> list[Comment]:
        
        # TODO: get comments of this card from database

        # TODO: adjust comments structure (which one is reply of which) (Eu ignoraria isso por enquanto, faz os comentários todos sem reply e aí não precisa disso)

        return []
    
    
    def addComment(self, user_id: int, text: str, parent_comment_id: int = None) -> Comment:

        # Add comment to database (and create a comment object)
        comment = card_db.addComment(self.id, user_id, text, parent_comment_id)

        return comment