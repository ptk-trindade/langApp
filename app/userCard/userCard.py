from models.user import User
from models.card import Card

import userCard.db as userCard_db


class UserCard(User):
    def __init__(self, user_id):
        self.id = user_id
        

    def getCard(self) -> Card:
        
        card = userCard_db.pickCard(self.id)

        return card

    
    def getCardByConcept(self, concept_id) -> Card:

        # TODO: Get the card (filtering by concept)

        return Card(123, 'Chair', 'Cadeira', False, [{'id': 1, 'name': 'Chair', 'description': 'Used to sit on', 'type': 'word'}])
    

    def postFeedback(self, card_id, difficulty):

        # TODO: Update user_concept table (reviewed_at = now(), retention *= 2 (0.75, 2 or 4 depends on difficulty))

        return
