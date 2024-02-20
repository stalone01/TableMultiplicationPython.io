# ............TABLES DE MULTIPLICATIONS................

def afficher_table_multiplication(n):
    min = 1
    max = 11
    for i in range(min, max):
        print(i,"x", n, "=", i*n)
    print()

n=10
for j in range(n):
    afficher_table_multiplication(j+1)