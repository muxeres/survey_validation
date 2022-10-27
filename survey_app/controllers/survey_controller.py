from survey_app import app
from flask import request, session, redirect, render_template
from survey_app.models.language_model import Language
from survey_app.models.location_model import Location
from survey_app.models.survey_model import Survey

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if not Survey.validate_survey(request.form):
            return redirect("/")
        data_create_survey = {
            'name':request.form['name'],
            'comment':request.form['comment'],
            'location_id':request.form['location'],
            'language_id':request.form['language']
        }
        response_create_survey=Survey.create_new_survey(data_create_survey)
        print('Se creo correctamente',response_create_survey)
        data_language_id={
            'id':request.form['language']
        }
        data_location_id={
            'id':request.form['location']
        }
        language = Language.get_language_by_id(data_language_id)
        location = Location.get_location_by_id(data_location_id)
        session['form']={
            'name':request.form['name'],
            'location':location.location_name,
            'language':language.language_name,
            'comment':request.form['comment']
        }
        return redirect("/results")
    else:
        response_languages=Language.get_all_languages()
        response_locations=Location.get_all_locations()
        print("renderizando pagina index.html")
        return render_template("index.html",languages=response_languages,locations=response_locations)

@app.route("/results", methods=['GET'])
def results_survey():
    # print(session['form'])
    return render_template("result.html")
