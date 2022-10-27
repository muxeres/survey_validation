from survey_app.config.mysqlconnection import connectToMySQL

class Location:
    def __init__(self,data):
        self.id=data['id']
        self.location_name=data['location_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_locations(cls):
        query = '''
                SELECT * FROM locations
                '''
        response_query_locations = connectToMySQL('dojo_survey').query_db(query)
        locations=[]
        for location in response_query_locations:
            locations.append(cls(location))
        return locations
    
    @classmethod
    def get_location_by_id(cls,data):
        query = '''
                SELECT * FROM locations WHERE id = %(id)s
                '''
        response_query_location = connectToMySQL('dojo_survey').query_db(query,data)
        location = cls(response_query_location[0])
        return location