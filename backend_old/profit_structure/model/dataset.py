from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    balance: object
    income_statement: object
    id: str
    label: str

    @property
    def context(self) -> str:return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str:return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def balance(self) -> object:return self._balance

    @balance.setter
    def balance(self, balance): self._balance = balance

    @property
    def income_statement(self) -> object: return self._income_statement

    @income_statement.setter
    def income_statement(self, income_statement): self._income_statement = income_statement

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return  self._label

    @label.setter
    def label(self, label): self._label = label