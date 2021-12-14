from fraction.fraction import Fraction

if __name__ == "__main__":


    print(Fraction(4, 0) + Fraction(2, 1))

    print(Fraction(4, "a") + Fraction(2, 1))

    print("line9, addition : {}".format(Fraction(4, 2) + Fraction(2, 1)))

    print("line11, soustraction : {}".format(Fraction(4, 2) - Fraction(2, 1)))

    print("line13, multiplication : {}".format(Fraction(4, 2) * Fraction(2, 1)))

    print("line15, division :{}".format(Fraction(4, 2) / Fraction(2, 1)))

    print("line17, puissance : {}".format(Fraction(4, 2) ** Fraction(2, 1)))

    print("line19, égalité :{}".format(Fraction(4, 2) == Fraction(8, 4)))
    print("line20, égalité :{}".format(Fraction(4, 2) == Fraction(7, 4)))

    print("line22, flotant :{}".format(Fraction(10, 3).__float__()))

    print("line24, is zéro : {}".format(Fraction(1, 1).is_zero()))
    print("line25, is zéro : {}".format(Fraction(0, 1).is_zero()))

    print("line27, is int : {}".format(Fraction(10, 3).is_integer()))
    print("line28, is int : {}".format(Fraction(10, 2).is_integer()))

    print("line30, is unit : {}".format(Fraction(10, 3).is_unit()))
    print("line31, is unit : {}".format(Fraction(10, 10).is_unit()))

    print("line33, is ajd : {}".format((Fraction(10, 3).is_adjacent_to(Fraction(2, 1)))))
    print("line34, is ajd : {}".format((Fraction(1, 3).is_adjacent_to(Fraction(1, 4)))))

