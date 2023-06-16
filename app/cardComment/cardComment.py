from models.comment import Comment
from models.card import Card

# import database.db as db
import cardComment.db as cardComment_db

# Manipulate comments on a card
class CardComment(Card):
    def __init__(self, card_id: int):
        self.id = card_id
        
    def getComments(self) -> list[Comment]:
        
        # TODO: get comments of this card from database

        return []
    
    
    def addComment(self, user_id: int, text: str, parent_comment_id: int = None) -> Comment:

        # Add comment to database (and create a comment object)
        comment = cardComment_db.addComment(self.id, user_id, text, parent_comment_id)

        return comment

    # soLid -> liskov substitution principle (cardComment is a Card, so it has toJson method)
    def toJson(self):

        data = Card.toJson(self)
        data['comments'] = [comment.toJson() for comment in self.getComments()]

        return data
