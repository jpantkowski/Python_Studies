def woda(koszt_netto: float,
         podatek: int = 23,
         opakowanie: str = "plastik") -> float:
    return koszt_netto + koszt_netto * podatek / 100

print(woda(1, podatek = 12))
print(woda(1))

koszt_brutto = woda(2.0, opakowanie = "szkło")
print(koszt_brutto)