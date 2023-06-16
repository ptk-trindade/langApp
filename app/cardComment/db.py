from models.comment import Comment

import database.db as db
# database connection imported from database/db.py

def addComment(card_id: int, user_id: int, text: str, parent_comment_id: int) -> Comment:
    # TODO

    # use cursor.lastrowid or connection.insert_id() to get the id of the inserted comment

    return None

def getComments(card_id: int) -> list[Comment]:
    # TODO

    return []