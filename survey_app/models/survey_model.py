from survey_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Survey:
    def __init__(self,data):
        self.id= data['id']
        self.name= data['name']
        self.comment= data['comment']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.location_id= data['location_id']
        self.language= data['language']

@classmethod
def create_new_survey(cls,data):
    query = '''
            INSERT INTO surveys (name,comment,location_id,language_id)
            VALUES (%(name)s,%(comment)s,%(language_id)s,%(location_id)s);
            '''
    response_query_id=connectToMySQL('dojo_survey').query_db(query,data)
    return response_query_id

@staticmethod
def validate_survey(survey):
    is_valid = True
    if len(survey['name']) < 3:
        is_valid = False
        flash("el nombre debe tener al menos 3 caracteres")
    if len(survey['location']) == 0:
        is_valid = False
        flash("debe elejir una locacion")
    if len(survey['language']) == 0:
        is_valid = False
        flash("debe elegir un lenguaje")
    if len(survey['comment']) < 5:
        is_valid = False
        flash("debe escribir un comentario al menos 5 palabras")
    return is_valid