from abc import ABC, abstractmethod

class PriceProvider(ABC):

    @abstractmethod
    def get_gold_price(self):
        pass

    @abstractmethod
    def get_silver_price(self):
        pass

    @abstractmethod
    def get_location(self):
        pass
