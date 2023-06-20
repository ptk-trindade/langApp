import mysql.connector

from database.db import conn
from models.card import Card

# database connection imported from database/db.py

def pickCard(user_id: int) -> Card:
    """
    Picks a card from the database and returns it
    """
    try:
        query = """
                SELECT  cards.id, 
                        cards.hasAudio, 
                        GROUP_CONCAT(card_concept.concept_id) AS concepts,
                        cards.front, 
                        cards.verse, 
                        cards.sourceLanguage_id,
                        cards.targetLanguage_id,
                        cards.creator_id
                FROM cards
                LEFT JOIN card_concept
                    ON cards.id = card_concept.card_id
                GROUP BY cards.id, 
                        cards.hasAudio,
                        cards.front, 
                        cards.verse, 
                        cards.sourceLanguage_id,
                        cards.targetLanguage_id,
                        cards.creator_id
                LIMIT 1
            """
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        card = Card(card_id=result[0],
                    hasAudio=result[1],
                    concepts=result[2].split(','),
                    front=result[3],
                    back=result[4],
                    sourceLanguage_id=result[5],
                    targetLanguage_id=result[6],
                    creator_id=result[7])
        
        return card
    except Exception as e:
        # Handle other unexpected exceptions
        raise(e)
