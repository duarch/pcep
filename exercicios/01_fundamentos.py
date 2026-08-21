def media_de_tres(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def par_ou_impar(numero: int) -> str:
    return "par" if numero % 2 == 0 else "impar"


if __name__ == "__main__":
    print("Média de 6, 7 e 8:", media_de_tres(6, 7, 8))
    print("9 é", par_ou_impar(9))
