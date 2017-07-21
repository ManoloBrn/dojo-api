#!/usr/bin/env python
"""
Main module for the dojo mvp application.

Here we handle the base configurations for the application.

"""
# @api.route('/my-resource/<id>', endpoint='my-resource')
# @api.doc(params={'id': 'An ID'})
# class MyResource(Resource):
#     def get(self, id):
#         return {}
#
#     @api.doc(responses={403: 'Not Authorized'})
#     def post(self, id):
#         api.abort(403)

from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
from flask_swagger import swagger

from api import app
import dojo_api_v1.dojo
import dojo_api_v1.test


api = Api(app, version='1.0', title='Sample API', description='A sample API')

# URLS:
SMOKE_URL = '/_t/smoke'


@api.route(SMOKE_URL)
@api.doc(params={'id': 'An ID'})
class SmokeTest(Resource):

    def get(self):
        _id = request.args.get('id')
        ctx = {'id': _id}

        return jsonify(ctx)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    return 'An internal error occurred.', 500
