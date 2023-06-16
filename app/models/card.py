from models.concept import Concept

import database.db as db
import card.db as card_db


class Card:
    
    def __init__(self, card_id: int, concepts = [], hasAudio = False, front = '', back = '', sourceLanguage_id = 0, targetLanguage_id = 0, creator_id = 0):
        self.id = card_id
        self.concepts = concepts
        self.hasAudio = hasAudio
        self.front = front
        self.back = back
        self.sourceLanguage_id = sourceLanguage_id
        self.targetLanguage_id = targetLanguage_id
        self.creator_id = creator_id


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