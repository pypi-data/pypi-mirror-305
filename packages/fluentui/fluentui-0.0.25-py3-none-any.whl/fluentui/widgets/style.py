from dataclasses import dataclass, field
from typing import Self


@dataclass
class Qss:
    styles: dict = field(default_factory=dict)

    def merge(self, a: 'dict | Qss') -> Self:
        self.__merge(a if isinstance(a, dict) else a.styles)
        return self

    def accept(self, a: 'dict | Qss') -> Self:
        self.styles = self.__merge(self.styles, a)
        return self

    def __merge(self, dst: dict, src: dict = None) -> dict:
        src = self.styles if src is None else src
        for name, elem in dst.items():
            if isinstance(elem, dict):
                src[name] = self.__merge(elem, src.get(name, {}))
            else:
                src[name] = elem
        return src

    def build(self, styles: dict = None) -> str:
        if not (styles := styles or self.styles):
            return ''

        base, elems = [], {}
        for k, v in styles.items():
            if isinstance(v, dict):
                elems[k] = v
                continue
            base.append(f"    {k}: {v};")

        result = "{\n" + "\n".join(base) + "\n}"
        return result + ''.join(f"\n{k} {self.build(v)}" for k, v in elems.items())
