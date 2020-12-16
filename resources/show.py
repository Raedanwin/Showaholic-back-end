import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

show = Blueprint('shows', 'show')

@show.route('/', methods=['GET'])
def index():
    try:
        shows = [model_to_dict(show) for show in models.Show.select()]
        print(show)
        return jsonify(data=shows, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'error getting resources'})

@show.route('/', methods=['POST'])
def create():
    payload = request.get_json()
    new_show = models.Show.create(**payload)
    show_dict = model_to_dict(new_show)
    return jsonify(data=show_dict, status={'code': 201, 'message': 'Success'})

@show.route('/<id>', methods=['GET'])
def show_page(id):
    show = models.Show.get_by_id(id)
    print(show.__dict__)
    return jsonify(data=model_to_dict(show), status={'code': 200, 'message': 'Success'})

@show.route('<id>', methods=['PUT'])
def update(id):
    payload = request.get_json()
    query = models.Show.update(**payload).where(models.Show.id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Show.get_by_id(id)), status={"code": 200, "message": "Success"})

@show.route('/<id>', methods=["DELETE"])
def delete(id):
    query = models.Show.delete().where(models.Show.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})