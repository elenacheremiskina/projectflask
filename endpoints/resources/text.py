from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from flask import redirect, request, url_for
from endpoints.models.text import Text
from app import db, app
import os
from werkzeug.utils import secure_filename
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)
import uuid
from endpoints.resources.frequency import frequency

text_fields = {
    'id_text': fields.Integer,
    'file': fields.String
}

text_list_fields = {
    'count': fields.Integer,
    'texts': fields.List(fields.Nested(text_fields)),
}

text_post_parser = reqparse.RequestParser()
text_post_parser.add_argument('file', type=str, required=True, location=['json'],
                              help='file parameter is required')

class TextResource(Resource):
    @jwt_required
    def get(self, id_text=None):
        text = Text.query.filter_by(id_text=id_text).first()
        file = text.file
        return frequency(file)

    @jwt_required
    @marshal_with(text_fields)
    def post(self):

        file = request.files['file']
        filename = secure_filename(file.filename)

        fileExt = filename.split('.')[1]
        autoGenFileName = uuid.uuid4()

        newFileName = str(autoGenFileName) + '.' + fileExt

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newFileName))

        file = Text(file=newFileName)

        db.session.add(file)
        db.session.commit()
        return file
