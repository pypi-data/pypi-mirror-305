from dataclasses import dataclass, field
from typing import Self


@dataclass
class Qss:
    style: dict = field(default_factory=dict)

    def merge(self, d: dict) -> Self:
        self.__merge(d)
        return self

    def __merge(self, d: dict, **kwargs) -> Self:
        table = kwargs.get('table', self.style)
        for name, elem in d.items():
            if isinstance(elem, dict):
                table[name] = self.__merge(elem, table=table.get(name, {}))
            else:
                table[name] = elem
        return table

    def build(self, table: dict = None) -> str:
        base, elems = [], {}
        for k, v in (table or self.style).items():
            if isinstance(v, dict):
                elems[k] = v
                continue
            base.append(f"    {k}: {v};")

        result = "{\n" + "\n".join(base) + "\n}"
        return result + ''.join(f"\n{k} {self.build(v)}" for k, v in elems.items())
