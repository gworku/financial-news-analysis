import pytest
from src.data_processing import download_stock_data

def test_valid_stock_data():
    data = download_stock_data("AAPL", "2023-01-01", "2023-01-10")
    assert data is not None
    assert not data.empty

def test_invalid_stock_data():
    data = download_stock_data("INVALID", "2023-01-01", "2023-01-10")
    assert data is None
