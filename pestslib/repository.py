import abc
from pestslib.pests import Pest


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, pests: Pest):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, pests) -> Pest:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __int__(self, pests):
        self.pests = pests

    def add(self, pest):
        self.pests.add(pest)
