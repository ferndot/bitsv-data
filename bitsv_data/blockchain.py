# -*- coding: utf-8 -*-
from bitsv.network import NetworkAPI


def store_data(key, data):
    """
    Stores data on the blockchain

    :param key: The key to use for the transaction
    :param data: The data to store
    :returns: The completed transaction's ID
    """

    transaction_data = [(data, 'utf-8')]
    return key.send_op_return(transaction_data)['data']['txid']


def load_data(transaction_id):
    """
    Retrieves a data transaction from the blockchain

    :param transaction_id: The transaction ID to look up
    """

    # Get transaction
    transaction = NetworkAPI.get_transaction(transaction_id)

    # Get data
    data = transaction['data']['vout'][1]['scriptPubKey']['hex']

    # Decode to bytes
    data = bytes.fromhex(data)

    # Handle op codes
    if data[1] == 76:
        # Clear 3 bytes
        data = data[2:]

    elif data[1] == 77:
        # Clear 5 bytes
        data = data[4:]

    elif data[1] == 78:
        # Clear 7 bytes
        data = data[6:]

    else:
        data = data[1:]

    # Decode into utf-8
    data = data.decode('utf-8', errors='ignore')

    return data
