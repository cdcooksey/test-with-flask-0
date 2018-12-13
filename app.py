"""
RUN WITH:
FLASK_APP=app.py FLASK_ENV=development flask run 
"""

from flask import Flask
from flask import jsonify
from peewee import *
import json
from playhouse.flask_utils import FlaskDB
# from playhouse.shortcuts import model_to_dict

DATABASE = SqliteDatabase('data.db')

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)
peewee_db = db_wrapper.database

@app.route('/api/v1/events', methods=['GET'])
@app.route('/api/v1/events/<int:page>', methods=['GET'])
def events(page=1):
    delimiter = page * 30

    data = []
    data = [event_dict(row) for row in Event.select().get_page()]
    
    return jsonify({'data': data})

def event_dict(row={}):
    return { 'id':                       row.id,
             'status':                   row.status,
             'start_date':               row.start_date,
             'end_date':                 row.end_date,
             'description':              row.description,
             'official':                 row.official,
             'visibility':               row.visibility,
             'guests_can_invite_others': row.guests_can_invite_others,
             'modified_date':            row.modified_date,
             'created_date':             row.created_date,
             'participant_count':        row.participant_count,
             'reason_for_private':       row.reason_for_private,
             'order_email_template':     row.order_email_template,
             'name':                     row.name
             }

class Event(db_wrapper.Model):
    status                   = CharField()
    start_date               = DateField()
    end_date                 = DateField()
    description              = CharField()
    official                 = BooleanField(default = True)
    visibility               = CharField()
    guests_can_invite_others = CharField()
    modified_date            = DateField()
    created_date             = DateField()
    participant_count        = IntegerField()
    reason_for_private       = CharField()
    order_email_template     = CharField()
    name                     = CharField()

    class Meta:
        table_name = 'events'
