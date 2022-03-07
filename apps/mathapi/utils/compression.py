# -*- coding: utf-8 -*-
from itertools import groupby


def encode(in_str: str) -> int:
    """
    Esta función debe devolver el string codificado de la siguiente manera:
    Por cada grupo de caracteres alfabéticos (de la A a la Z sin incluir la Ñ y sin distinguir mayúsculas
    de minúsculas) iguales consecutivos, se incluira dicho caracter en mayúsculas seguido del número de repeticiones.
    Por ejemplo para la entrada "aaAabaccCBb", la salida debe ser "A4B1A1C3B2"
    :param in_str: string de entrada. Estará formado por letras de la A a la Z sin incluir la Ñ
    :return: string codificado como se describe más arriba
    """
    
    return "".join(f"{c}{sum(1 for i in group)}"
                     for c, group in groupby(in_str.lower())
                     ).upper()

