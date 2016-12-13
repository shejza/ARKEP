from flask import Blueprint, render_template, request
from bson import json_util, ObjectId
from app import mongo

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET', 'POST'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    db = mongo.db.arkep

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        db.insert(data)
        return json_util.dumps(data)
    else:
        return 'bad request'

    
@mod_main.route('/<string:id>', methods=['GET'])
def get_doc(id):
    ''' Renders the App index page.
    :return:
    '''
    db = mongo.db.arkep

    if request.method == 'GET':
        doc = db.find({"_id":ObjectId(id)})
        doc_json = json_util.dumps(doc)
        return render_template('doc.html', doc=doc_json)
    else:
        return 'bad request'
