from models.comment import Comment

import database.db as db
import card.db as card_db


class Card:
    concepts = []
    hasAudio = False
    front = ''
    back = ''

    def __init__(self, card_id: int, 
                       concepts = [], 
                       hasAudio = False, 
                       front = '', 
                       back = '', 
                       sourceLanguage_id = int, 
                       targetLanguage_id = int, 
                       creator_id = int):
        
        self.id = card_id
        self.concepts = concepts
        self.hasAudio = hasAudio
        self.front = front
        self.back = back
        self.sourceLanguage_id = sourceLanguage_id
        self.targetLanguage_id = targetLanguage_id
        self.creator_id = creator_id

    def getComments(self) -> list[Comment]:
        
        # TODO: get comments of this card from database

        # TODO: adjust comments structure (which one is reply of which) (Eu ignoraria isso por enquanto, faz os comentários todos sem reply e aí não precisa disso)

        return []
    
    
    def addComment(self, user_id: int, text: str, parent_comment_id: int = None) -> Comment:

        # Add comment to database (and create a comment object)
        comment = card_db.addComment(self.id, user_id, text, parent_comment_id)

        return comment

    def toJson(self):
        concepts = [concept.toJson() for concept in self.concepts]

        x = {
            'concepts': [{'id': 1, 'name': 'Chair', 'description': 'Used to sit on', 'type': 'word'}],
            'hasAudio': False,
            'front': 'Chair',
            'back': 'Cadeira',
            'card_id': 123
        }

        return {
            'concepts': [concept.toJson() for concept in self.concepts],
            'hasAudio': self.hasAudio,
            'front': self.front,
            'back': self.back,
            'card_id': self.id
        }
