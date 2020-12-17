import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

watchlist = Blueprint('watchlists', 'watchlist')

@watchlist.route('/', methods=['GET'])
def index():
    try:
        watchlists = [model_to_dict(watchlist) for watchlist in models.Watchlist.select()]
        print(watchlist)
        return jsonify(data=watchlists, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'error getting resources'})

@watchlist.route('/', methods=['POST'])
def create():
    payload = request.get_json()
    print(type(payload), 'payload')
    watchlist = models.Watchlist.create(**payload)
    print(watchlist.__dict__)
    print(dir(watchlist))
    print(model_to_dict(watchlist), 'model to dict')
    watchlist_dict = model_to_dict(watchlist)
    return jsonify(data=watchlist_dict, status={'code': 201, 'message': 'Success'})

@watchlist.route('/<id>', methods=['GET'])
def show(id):
    watchlist = models.Watchlist.get_by_id(id)
    print(watchlist.__dict__)
    return jsonify(data=model_to_dict(watchlist), status={'code': 200, 'message': 'Success'})

@watchlist.route('<id>', methods=['PUT'])
def update(id):
    payload = request.get_json()
    query = models.Watchlist.update(**payload).where(models.Watchlist.watchlist_id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Watchlist.get_by_id(id)), status={"code": 200, "message": "Success"})

@watchlist.route('/<id>', methods=["DELETE"])
def delete(id):
    query = models.Watchlist.delete().where(models.Watchlist.watchlist_id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})