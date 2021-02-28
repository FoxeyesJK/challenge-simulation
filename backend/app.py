from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class TraineeModel(db.Model):
    __tablename__ = 'trainee'
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    clients = db.relationship("ClientModel")

simulations = db.Table('simulations',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('simulation_id', db.Integer, db.ForeignKey('simulation.id'), primary_key=True)
)

class ClientModel(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)
    trainee_id = db.Column(db.Integer(), db.ForeignKey('trainee.id'))
    simulations = db.relationship("SimulationModel", secondary=simulations, lazy='subquery', backref=db.backref('clients', lazy=True))

class SimulationModel(db.Model):
    __tablename__ = 'simulation'
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)

trainee_get_args = reqparse.RequestParser()
trainee_get_args.add_argument("clientId", type=int)

trainee_post_args = reqparse.RequestParser()
trainee_post_args.add_argument("firstName", type=str, help="First Name of the trainee is required", required=True)
trainee_post_args.add_argument("lastName", type=str, help="Last Name of the trainee is required", required=True)

client_get_args = reqparse.RequestParser()
client_get_args.add_argument("traineeId", type=int)

client_post_args = reqparse.RequestParser()
client_post_args.add_argument("name", type=str, help="Name of the client is required", required=True)
client_post_args.add_argument("code", type=str, help="Code of the client is required", required=True)
client_post_args.add_argument("traineeId", type=int)

simulation_get_args = reqparse.RequestParser()
simulation_get_args.add_argument("traineeId", type=int)

simulation_post_args = reqparse.RequestParser()
simulation_post_args.add_argument("name", type=str, help="Name of the simulation is required", required=True)

client_simulation_post_args = reqparse.RequestParser()
client_simulation_post_args.add_argument("clientId", type=int)
client_simulation_post_args.add_argument("simulationId", type=int)
client_simulation_post_args.add_argument("simulationIds", action='append')

db.drop_all()
db.create_all()

trainee_resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String(attribute='first_name'),
    'lastName': fields.String(attribute='last_name')
}

client_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'code': fields.String,
    'traineeId': fields.Integer(attribute='trainee_id')
}

simulation_resource_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class Trainee(Resource):
    @marshal_with(trainee_resource_fields)
    def get(self):
        args = trainee_get_args.parse_args()
        client_id = args['clientId']

        if not client_id:
            trainees = TraineeModel.query.all()
            return trainees
        
        trainee = TraineeModel.query.filter(ClientModel.id==client_id).first()
        return trainee
    
    @marshal_with(trainee_resource_fields)
    def post(self):
        args = trainee_post_args.parse_args()
        trainee = TraineeModel(first_name=args['firstName'], last_name=args['lastName'])
        db.session.add(trainee)
        db.session.commit()
        return trainee, 201

class Client(Resource):
    @marshal_with(client_resource_fields)
    def get(self):
        args = client_get_args.parse_args()
        trainee_id = args['traineeId']

        if not trainee_id:
            clients = ClientModel.query.all()
            return clients
        
        client = ClientModel.query.filter_by(trainee_id=trainee_id).first()
        return client
    
    @marshal_with(client_resource_fields)
    def post(self):
        args = client_post_args.parse_args()
        client = ClientModel(name=args['name'], code=args['code'], trainee_id=args['traineeId'])
        db.session.add(client)
        db.session.commit()
        return client, 201

class Simulation(Resource):
    @marshal_with(simulation_resource_fields)
    def get(self):
        args = simulation_get_args.parse_args()
        trainee_id = args['traineeId']
        if not trainee_id:
            simulations = SimulationModel.query.all()
            return simulations

        trainee_client_id = ClientModel.query.filter_by(trainee_id=trainee_id).first().id
        simulations = ClientModel.query.filter_by(id=trainee_client_id).first().simulations
        return simulations

    @marshal_with(simulation_resource_fields)
    def post(self):
        args = simulation_post_args.parse_args()
        simulation = SimulationModel(name=args['name'])
        db.session.add(simulation)
        db.session.commit()
        return simulation, 201

class ClientSimulationMapping(Resource):
    def post(self):
        args = client_simulation_post_args.parse_args()
        client_id = args['clientId']
        simulations_id = args['simulationIds']
        client = ClientModel.query.filter_by(id=client_id).first()
        
        client.simulations = []
        db.session.commit()

        if simulations_id:
            for simulationId in simulations_id:
                simulation = SimulationModel.query.filter_by(id=simulationId).first()
                if simulation:
                    client.simulations.append(simulation)

        db.session.commit()
        return '', 201


api.add_resource(Trainee, "/trainees")
api.add_resource(Client, "/clients")
api.add_resource(Simulation, "/simulations")
api.add_resource(ClientSimulationMapping, "/client-simulation-mapping")

if __name__ == "__main__":
    app.run(debug=True)


