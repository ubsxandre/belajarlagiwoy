from app import app #import variabel app dari (default __init__.py) yang berada di folder app
from app.controller import DosenController

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/dosen', methods=['GET'])   # INGAATT!! GET itu untuk menampilkan data
def dosens():
    return DosenController.index()

@app.route('/dosen/<id>', methods=['GET']) # tadinya ini GET, tapi nanti akan bisa update (PUT)
def dosensDetail(id):
    return DosenController.detail(id)