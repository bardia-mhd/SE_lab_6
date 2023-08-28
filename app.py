# app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db.init_app(app)
    return app


app = create_app()


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Resource {self.id}>"


with app.app_context():
    db.create_all()


@app.route('/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{'id': resource.id, 'name': resource.name} for resource in resources])


@app.route('/resources', methods=['POST'])
def create_resource():
    name = request.json.get('name')

    if not name:
        return jsonify({'error': 'Missing required field: name'}), 400

    resource = Resource(name=name)
    db.session.add(resource)
    db.session.commit()

    return jsonify({'message': 'Resource created successfully', 'id': resource.id}), 201


@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = Resource.query.get(resource_id)

    if not resource:
        return jsonify({'error': 'Resource not found'}), 404

    name = request.json.get('name')

    if not name:
        return jsonify({'error': 'Missing required field: name'}), 400

    resource.name = name
    db.session.commit()

    return jsonify({'message': 'Resource updated successfully'})


@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = Resource.query.get(resource_id)

    if not resource:
        return jsonify({'error': 'Resource not found'}), 404

    db.session.delete(resource)
    db.session.commit()

    return jsonify({'message': 'Resource deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
