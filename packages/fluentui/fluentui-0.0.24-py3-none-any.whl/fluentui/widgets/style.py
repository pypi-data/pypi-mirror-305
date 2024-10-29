from dataclasses import dataclass, field
from typing import Self


@dataclass
class Qss:
    styles: dict = field(default_factory=dict)

    def merge(self, d: dict | 'Qss') -> Self:
        self.__merge(d if isinstance(d, dict) else d.styles)
        return self

    def __merge(self, dst: dict, src: dict = None) -> dict:
        src = src or self.styles
        for name, elem in dst.items():
            if isinstance(elem, dict):
                src[name] = self.__merge(elem, src.get(name, {}))
            else:
                src[name] = elem
        return src

    def build(self, table: dict = None) -> str:
        base, elems = [], {}
        for k, v in (table or self.styles).items():
            if isinstance(v, dict):
                elems[k] = v
                continue
            base.append(f"    {k}: {v};")

        result = "{\n" + "\n".join(base) + "\n}"
        return result + ''.join(f"\n{k} {self.build(v)}" for k, v in elems.items())
