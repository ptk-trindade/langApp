from models.concept import Concept

import database.db as db

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
        json = {
            'card_id': self.id,
            'concepts': [concept.toJson() for concept in self.concepts],
            'hasAudio': self.hasAudio,
            'front': self.front,
            'back': self.back,
            'sourceLanguage_id': self.sourceLanguage_id,
            'targetLanguage_id': self.targetLanguage_id,
            'creator_id': self.creator_id
        }

        return json
