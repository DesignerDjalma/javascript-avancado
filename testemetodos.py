import calendar
import datetime


class Calendario:
    @classmethod
    def from_json(cls, nome_arquivo: str):
        c = cls()
        ...
        return c


class CalendarioTrabalho(Calendario):
    pass


def main():
    c = Calendario.from_json("normal.calendar")
    ct = CalendarioTrabalho.from_json("trabalho.calendar")
    print(c)
    print(ct)



if __name__ == "__main__":
    main()