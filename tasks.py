def add_task(lista_zadan):
    zadanie = input("Podaj treść zadania: ").strip()

    if zadanie:
        lista_zadan.append(zadanie)
        print("Dodano zadanie")
    print("Zadanie nie może być puste")    
