"""
Chain of responsability (COR) é um padrão de projeto comportamental que tem a intenção de evitar o acoplamento do remetente de uma solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar essa solicitação. Encadear os objetos receptores passando a solicitação ao longo da cadeia até que um objeto a trate.
"""


# Implementando com funções
def handler_ABC(letter: str) -> str:
    letters = ["A", "B", "C"]

    if letter in letters:
        return f"handler_ABC conseguiu tratar o valor {letter}"
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ["D", "E", "F"]

    if letter in letters:
        return f"handler_DEF conseguiu tratar o valor {letter}"
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f"handler_unsolved: não foi possível tratar o valor {letter}"


if __name__ == "__main__":
    print(handler_ABC("A"))
    print(handler_ABC("B"))
    print(handler_ABC("C"))
    print(handler_ABC("D"))
    print(handler_ABC("E"))
    print(handler_ABC("F"))
    print(handler_ABC("H"))