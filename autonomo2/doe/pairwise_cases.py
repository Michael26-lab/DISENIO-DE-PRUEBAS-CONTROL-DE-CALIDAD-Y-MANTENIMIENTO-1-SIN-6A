from allpairspy import AllPairs
import csv

def main():
    # Define factores con niveles (ejemplo)
    factors = [
        ["size1","size2","size3","size4","size5"],        # 5 niveles
        ["order1","order2","order3","order4","order5","order6"],  # 6 niveles
        ["methodA","methodB","methodC","methodD","methodE"],     # 5 niveles
        ["low","med","high","veryhigh","extreme","peak","idle"],  # 7 niveles
        ["env1","env2","env3","env4"]                         # 4 niveles
    ]

    pairs = list(AllPairs(factors))
    # Guardar CSV
    with open("../reports/pairwise_cases.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["factor1","factor2","factor3","factor4","factor5"])
        for p in pairs:
            writer.writerow(p)

    print(f"Generadas {len(pairs)} casos pairwise -> reports/pairwise_cases.csv")

if __name__ == "__main__":
    main()
