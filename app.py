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

@app.route('/api/v1/events/<int:eventId>', methods=['GET'])
def events_details(eventId=0):
    try:
        event = Event.select().where(Event.id == eventId).get()
        response = {'data': model_to_dict(event)}
    except DoesNotExist:
        response = {'error': 'No instance of MyModel exists at {}'.format(eventId)}

    return jsonify(response)

@app.route('/api/v1/events', methods=['GET'])
def events_summary():
    page      = int(request.args.get('page', '0'))
    delimiter = 10
    offset    = 0
    limit     = delimiter
    if page > 0:
        limit  = page * delimiter
        offset = page * delimiter

    rows   = Event.select(Event.id, Event.name).limit(limit).offset(offset)
    events = [{'id': row.id, 'name': row.name} for row in rows]

    return jsonify({
        'data': events,
        'meta': {
            'page': page,
            'offset': offset,
            'limit': limit,
            'results': rows.count()
            }
        })

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
