import datetime

from flask import Blueprint
from flask import request, render_template, jsonify,redirect, url_for

import sys
sys.path.append("..")

from blockchain import generate_genesis
from blockchain import Block, Transaction, BlockChain, Wallet

page = Blueprint('page', __name__)

blockchain, satoshi = generate_genesis()

@page.route('/')
def index():
    return redirect(url_for('.block'))

@page.route('/block')
def block():
    return render_template('block.html', active='block')

@page.route('/generate_block', methods=['POST'])
def generate_block():

    index = request.form['index']
    content = request.form['content']
    previous = request.form['previous']

    transaction = Transaction(satoshi.private_key, satoshi.public_key, str(content))
    block = Block(int(index), [transaction], previous, 0)

    block.timestamp = datetime.datetime(2009, 1, 10, 12, 00)
    transaction.timestamp = datetime.datetime(2009, 1, 10, 12, 00)

    response = {'hash': block.calculate_hash() }

    return jsonify(response), 200

@page.route('/proof_of_work')
def proof_of_work():
    return render_template('proof_of_work.html',
                            active='proof_of_work',
                            difficulty=BlockChain.DIFFICULTY)

@page.route('/generate_nonce', methods=['POST'])
def generate_nonce():
    index = request.form['index']
    content = request.form['content']
    previous = request.form['previous']
    nonce = request.form['nonce']

    transaction = Transaction(satoshi.private_key, satoshi.public_key, str(content))
    block = Block(int(index), [transaction], previous, 0)

    block.nonce = int(nonce)
    block.timestamp = datetime.datetime(2009, 1, 10, 12, 00)
    transaction.timestamp = datetime.datetime(2009, 1, 10, 12, 00)

    Block.proof_of_work(block, BlockChain)
    response = {'nonce' : block.nonce, 'hash': block.hash }

    return jsonify(response), 200

@page.route('/wallet')
def wallet():
    return render_template('wallet.html', active='wallet')

@page.route('/generate_wallet', methods=['POST'])
def generate_wallet():
    wallet = Wallet()
    return jsonify(wallet.to_hash()), 200

@page.route('/transaction')
def transaction():
    return render_template('transaction.html', active='transaction')

@page.route('/generate_transaction', methods=['POST'])
def generate_transaction():
    public_key = request.form['public_key']
    private_key = request.form['private_key']
    amount = request.form['amount']
    fees = request.form['fees']

    transaction = Transaction(private_key, public_key, amount, fees)
    transaction.sign()

    response = {'signature' : transaction.signature}
    return jsonify(response), 200
