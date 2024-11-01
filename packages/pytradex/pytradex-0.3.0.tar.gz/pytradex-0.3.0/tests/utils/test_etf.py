import pytest

from tradex.utils.etf import ETFConverter


@pytest.mark.parametrize(
    ("index_price", "etf_price", "tgt_index_price", "expected"),
    [
        (683.397, 0.78, 1021.3213, 1.17),
        (683.397, 0.782, 1135, 1.299),
        (683.397, 1, 1700, 2.49),
    ],
)
def test_tgt_etf_price(index_price, etf_price, tgt_index_price, expected):
    converter = ETFConverter(index_price=index_price, etf=etf_price)
    tgt_etf_price = converter.tgt_etf_price(tgt_index_price)
    assert tgt_etf_price == expected
