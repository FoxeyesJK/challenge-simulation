import requests

BASE = "http://localhost:5000/"

requests.post(BASE + "clients", {"name":"The Client Institute", "code":"TCI", "traineeId":1})
requests.post(BASE + "clients", {"name":"Trainee Sim Zone", "code":"TSZ", "traineeId":2})
requests.post(BASE + "clients", {"name":"VR Training Facility", "code":"VTF", "traineeId":3})

# response = requests.get(BASE + "clients")
# print(response)

requests.post(BASE + "simulations", {"name":"Rounding Decimals"})
requests.post(BASE + "simulations", {"name":"Engine Oil Change"})
requests.post(BASE + "simulations", {"name":"Data Structures and Algorithms"})
requests.post(BASE + "simulations", {"name":"Mixed Cocktails"})
requests.post(BASE + "simulations", {"name":"Battery Replacement"})

# response = requests.get(BASE + "simulations")
# print(response)

requests.post(BASE + "trainees", {"firstName":"Jesse", "lastName":"Pinkman"})
requests.post(BASE + "trainees", {"firstName":"Walter", "lastName":"White"})
requests.post(BASE + "trainees", {"firstName":"Saul", "lastName":"Goodman"})

# requests.post(BASE + "client-simulation-mapping", {"clientId": 1, "simulationId": 2})
