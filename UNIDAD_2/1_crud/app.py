"""
Nombre: Rincon Ulloa Yazmin Elizabeth
Fecha: 10 de noviembre del 2023
Descripcion: Creas un servidor web con flask para proporcionar servicios
mediante los metodos GET, PUT, DELATE Y POST.
"""

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('titulo')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM musica')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO musica(titulo, cantante, disquera, plataforma) VALUES(?,?,?,?)'
    cursor.execute(insert, [record['titulo'], record['cantante'], record['disquera'], record['plataforma']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM musica WHERE titulo= ?'
    cursor.execute(delete, [record['titulo']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE musica SET cantante = ? WHERE titulo= ?'
    cursor.execute(delete, [record['cantante'], record['titulo']])
    conn.commit()
    conn.close()
    return jsonify(record)

app.run(debug=True)
