import datetime

from flask import Blueprint
from flask import request, render_template, jsonify

import sys
sys.path.append("..")

from blockchain import Block, Transaction

page = Blueprint('page', __name__)

@page.route('/block')
def block():
    return render_template('block.html')

@page.route('/generate_block', methods=['POST'])
def generate_block():

    index = request.form['index']
    content = request.form['content']
    previous = request.form['previous']

    transaction = Transaction('satoshi', 'nakamoto', str(content))
    block = Block(int(index), [transaction], previous, 0)

    block.timestamp = datetime.datetime(2009, 1, 10, 12, 00)
    transaction.timestamp = datetime.datetime(2009, 1, 10, 12, 00)

    response = {'hash': block.calculate_hash() }

    return jsonify(response), 200
