

while True:
    n = str(input("para saber todos os números impares e pares entre 1 e 50 digite: \n (A) impar \n (B) par \n")).upper()
    if "B" in n:
        for n in range(2, 51, 2):
            print(n, end='.')
        print("\nEsses são os números pares entre 1 e 50")
        break
    if "A" in n:
        for n in range(1, 51, 2):
            print(n, end='.')
        print("\nEsses são os números ímpares entre 1 e 50")
        break
    if n != "A" or "B":
        print("Somente a opção A ou B são permitidas")
print("Espero que tenha sido uma experiência agradável")
