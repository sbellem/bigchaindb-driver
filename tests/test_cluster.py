from os import environ
from time import sleep

from pytest import mark

BDB_HOST_1 = environ.get('BDB_HOST_1', 'bdb1')
BDB_HOST_2 = environ.get('BDB_HOST_2', 'bdb2')
BDB_HOST_3 = environ.get('BDB_HOST_3', 'bdb3')


@mark.skipif(int(environ.get('BDB_DRIVER_TEST_CLUSTER', 0)),
             reason=('env var BDB_DRIVER_TEST_CLUSTER'
                     'must be set to 1 for cluster tests'))
@mark.parametrize('bdb_node', (BDB_HOST_1,), indirect=True)
#def test_retrieve_from_cluster_nodes(persisted_transaction, cluster_node):
def test_retrieve_from_cluster_nodes(persisted_transaction,
                                     bdb_node_1, bdb_node_2):
    from bigchaindb_driver import BigchainDB
    #driver = BigchainDB(cluster_node)
    driver = BigchainDB(bdb_node_1)
    sleep(2)
    txid = persisted_transaction['id']
    tx = driver.transactions.retrieve(txid)
    assert tx['id'] == txid
    assert 'transaction' in tx
