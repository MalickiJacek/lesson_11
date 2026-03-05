class RejestracjaUzytkownika:
    def __init__(self, email: str, haslo: str):
        if "@" not in email:
            raise ValueError("Email musi zawierać znak @")

        if len(haslo) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków")

        self.email = email
        self.haslo = haslo


try:
    u1 = RejestracjaUzytkownika("jan@example.com", "tajnehaslo")
    print("Użytkownik utworzony:", u1.email)
except ValueError as e:
    print("Błąd:", e)


try:
    u2 = RejestracjaUzytkownika("janexample.com", "tajnehaslo")
except ValueError as e:
    print("Błąd:", e)


try:
    u3 = RejestracjaUzytkownika("anna@example.com", "123")
except ValueError as e:
    print("Błąd:", e)