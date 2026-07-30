from toolkit.balances.core_mass import single_stream_balance


def test_single_stream() -> None:
    """Test single_stream_balance with positive value."""
    assert single_stream_balance(100) == 100


def test_single_stream_zero() -> None:
    """Test single_stream_balance with zero value."""
    assert single_stream_balance(0) == 0
