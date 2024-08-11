from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_iphone(self) -> AbstractProductIphone:
        pass

    @abstractmethod
    def create_galaxy(self) -> AbstractProductGalaxy:
        pass


class AppleFactory(AbstractFactory):

    def create_iphone(self) -> AbstractProductIphone:
        return Iphone15Pro()

    def create_galaxy(self) -> AbstractProductGalaxy:
        raise NotImplementedError("AppleFactory does not create Galaxy products.")


class SamsungFactory(AbstractFactory):
    def create_galaxy(self) -> AbstractProductGalaxy:
        return GalaxyS24()

    def create_iphone(self) -> AbstractProductIphone:
        raise NotImplementedError("SamsungFactory does not create iPhone products.")


class AbstractProductIphone(ABC):

    @abstractmethod
    def applepay(self) -> str:
        pass


class AbstractProductGalaxy(ABC):

    @abstractmethod
    def samsungpay(self) -> str:
        pass


class Iphone15Pro(AbstractProductIphone):
    def applepay(self) -> str:
        return "애플페이"


class GalaxyS24(AbstractProductGalaxy):
    def samsungpay(self) -> str:
        return "삼성페이"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    try:
        product_a = factory.create_iphone()
        print(f"{product_a.applepay()}")
    except NotImplementedError as e:
        print(e)

    try:
        product_b = factory.create_galaxy()
        print(f"{product_b.samsungpay()}")
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    client_code(AppleFactory())
    client_code(SamsungFactory())
