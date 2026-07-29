from toolkit.balances.core_mass import single_stream_balance

def test_single_stream():
    assert single_stream_balance(100) == 100

def test_single_stream():
    assert single_stream_balance(0) == 0
