class ETFConverter:
    """Main index price convert into ETF price"""

    _default_precision = 2

    def __init__(self, index_price: float, etf: float) -> None:
        self.index_price = index_price
        self.etf = etf

    @property
    def etf_precision(self) -> int:
        return len(str(self.etf).split(".")[1]) if "." in str(self.etf) else self._default_precision

    def tgt_etf_price(self, tgt_index_price: float) -> float:
        return round(self.etf * tgt_index_price / self.index_price, self.etf_precision)
