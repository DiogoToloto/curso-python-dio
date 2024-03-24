saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

conta_normal_sem_saldo_limite = (saldo >= saque and saque <= limite)
conta_especial_sem_saldo_limite = (conta_especial and saldo >= saque)

exp3 = conta_normal_sem_saldo_limite or conta_especial_sem_saldo_limite

print(exp)
print(exp2)
print(exp3)