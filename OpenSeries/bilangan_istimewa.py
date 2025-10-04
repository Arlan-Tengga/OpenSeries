from typing import Union
from .util.error import ErrorTipeData, Error
import numpy as np


def angka_armstrong(angka: int) -> Union[str, ErrorTipeData]:
    """
    angka armstrong adalah bilangan bulat positif yang sama dengan jumlah
    pangkat tiga dari digit-digitnya

    contoh:
    153 = 1^3 + 5^3 + 3^3 = 153

    Parameter:
        angka(int): angka yang akan di cek
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka armstrong", "bukan angka armstrong"
    # cek tipe data dari variable angka
    if isinstance(angka, (float, str)):
        return ErrorTipeData(["int"])
    angka_str = str(abs(angka))
    jumlah_digit = len(angka_str)

    digit_array = np.fromiter((int(digit) for digit in angka_str), dtype=int)
    total = np.sum(np.power(digit_array, jumlah_digit))
    return benar if abs(angka) == total else bukan


def angka_automorphic(angka: int) -> Union[str, ErrorTipeData]:
    """
    angka automorphic adalah bilangan asli dalam basis bilangan tertentu yang kuadratnya
    berakhir dengan angka yang sama dengan bilangan itu sendiri

    dalam basis 10, 5 adalah angka automorphic karena 5^2 = 25, dan keduanya diakhiri dengan
    angka 5
    dalam basis 2, 110 adalah angka automorphic karena 110^2 = 12100, dan anga diakhiri dengan
    digit 0

    Parameter:
        angka (int): mengecek angka tersebut automorphic atau tidak

    Return:
        str: mengembalikan informasi jika benar atau bukan
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka automorphic", "bukan angka automorphic"
    # cek dari tipe data angka
    if not isinstance(angka, int):
        return ErrorTipeData(["int"])
    if angka < 0:
        return bukan.capitalize()

    kuadrat_angka = angka * angka
    angka_str = str(angka)
    kuadrat_str = str(kuadrat_angka)
    if kuadrat_str.endswith(angka_str):
        return benar.capitalize()
    else:
        return bukan.capitalize()


def angka_pronic(angka: int) -> Union[str, ErrorTipeData]:
    """
    angka pronic adalah bilangan bulat positif yang merupakan hasil perkalian
    dari dua bilangan bulat berurutan
    6 = 2 * (2 + 1) = 2 * 3 = 6
    12 = 3 * (3 + 1) = 3 * 4 = 12
    20 = 4 * (4 + 1) = 4 * 5 = 20

    Parameter:
        angka(int): angka yang akan di cek

    Return:
        str: mengembalikan informasi jika benar atau bukan
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka pronic", "bukan angka pronic"
    # cek dari tipe data angka
    if not isinstance(angka, int):
        return ErrorTipeData(["int"])
    if angka < 0 or angka % 2 == 1:
        return bukan.capitalize()
    angka_pangkat = int(angka**0.5)
    return (
        benar.capitalize()
        if angka == angka_pangkat * (angka_pangkat + 1)
        else bukan.capitalize()
    )


def angka_segitiga(angka: int) -> Union[int, ErrorTipeData, Error]:
    """
    bilangan segitiga adalah bilangan yang dapat disusun dalam bentuk segitiga sama sisi

    Parameter:
        angka (int): angka yang ingin dimasukkan

    Return:
        int: angka segitiga di posisi yang ditentukan
        error.Error: jika angka negatif
        error.ErrorTipeData: jika tipe data salah
    """
    # jika tipe data dari angka tidak integer
    if not isinstance(angka, int):
        return ErrorTipeData(["int"])
    # jika value dari angka diisi nilai negatif
    if angka < 0:
        return Error("angka tidak boleh negatif")
    return angka * (angka + 1) // 2
