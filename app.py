"""
RUN WITH:
FLASK_APP=app.py FLASK_ENV=development flask run 
"""

import json
from flask import Flask, jsonify, request
from peewee import *
from playhouse.flask_utils import FlaskDB
from playhouse.shortcuts import model_to_dict

DATABASE = SqliteDatabase('data.db')

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)
peewee_db = db_wrapper.database

#@app.route('/api/v1/events', methods=['GET'])
@app.route('/api/v1/events/<int:page>', methods=['GET'])
def events(page=0):
    limit  = 10
    offset = 0
    if page > 0:
        limit  = page * 10
        offset = page * 10

    rows   = Event.select().limit(limit).offset(offset)
    events = [model_to_dict(row) for row in rows]

    response = jsonify({
        'data': events,
        'meta': {
            'page': page,
            'offset': offset,
            'limit': limit,
            'results': rows.count()
            }
        })

    return response

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
