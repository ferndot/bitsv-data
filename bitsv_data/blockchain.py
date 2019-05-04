# -*- coding: utf-8 -*-
import json

from bitsv.network import NetworkAPI


def store_data(key, data):
    """
    Stores a python object on the blockchain

    :param data: The data to store
    :returns: The completed transaction's ID
    """

    transaction_data = [(json.dumps(data), 'utf-8')]
    return key.send_op_return(transaction_data)['data']['txid']


def load_data(key, transaction_id):
    """
    Retrieves data from the blockchain

    :param transaction_id: The transaction ID to look up
    """

    # Get transaction
    transaction = NetworkAPI.get_transaction(transaction_id)

    # Get data
    data = transaction['data']['vout'][1]['scriptPubKey']['hex']

    # Decode to utf-8
    data = bytes.fromhex(data).decode('utf-8')

    # Decode from json
    data = json.loads(data[2:])

    return data
