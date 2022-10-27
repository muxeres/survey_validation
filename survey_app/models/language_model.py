from survey_app.config.mysqlconnection import connectToMySQL

class Language:
    def __init__(self,data):
        self.id=data['id']
        self.language_name=data['language_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_languages(cls):
        query='''
            SELECT * FROM languages    
            '''
        response_query_languages=connectToMySQL('dojo_survey').query_db(query)
        languages = []
        for language in response_query_languages:
            languages.append(cls(language))
        return languages
    
    @classmethod
    def get_language_by_id(cls,data):
        query='''
            SELECT * FROM languages WHERE id=%(id)s    
            '''
        response_query_language=connectToMySQL('dojo_survey').query_db(query,data)
        language = cls(response_query_language[0])
        return language