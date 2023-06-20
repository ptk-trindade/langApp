from dotenv import dotenv_values
import mysql.connector

def init_values_sql():
    env_vars = dotenv_values("database/.env")
    
    # Add cards to db
    try:
        with mysql.connector.connect(
            host = env_vars["DB_HOST"],
            user = env_vars["DB_USER"],
            password = env_vars["DB_PASSWORD"],
            database = 'langapp'
        ) as db:
            query_add_languages = "INSERT INTO languages (id, name, hasCourse) VALUES (12, 'English', 1)"
            query_add_concepts = "INSERT INTO concept (id, name, description, type) VALUES (14, 'Greeting', 'A greeting', 'noun')"
            query_add_user = "INSERT INTO user (id, username, email, password, sourceLanguage_id, targetLanguage_id) VALUES (13, 'test', 'test', 'test', 12, 12)"
            query_add_card = "INSERT INTO cards (id , hasAudio, front, verse, sourceLanguage_id, targetLanguage_id, creator_id) VALUES (1, 0, 'Hello', 'Hola', 12, 12, 13)"
            query_add_card_concept = "INSERT INTO card_concept (card_id, concept_id) VALUES (1, 14)"
            
            with db.cursor() as cursor:

                cursor.execute(query_add_languages)
                cursor.execute(query_add_concepts)
                cursor.execute(query_add_user)
                cursor.execute(query_add_card)
                cursor.execute(query_add_card_concept)
                db.commit()
    
    except Exception as e:
        # Handle other unexpected exceptions
        raise(e)
    

init_values_sql()