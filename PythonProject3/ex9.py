qtdeH=int(input("Quantos alunos do sexo MASCULINO? "))
qtdeM=int(input("Quantas alunas do sexo FEMININO? "))
qtdeAP=int(input("Quantos alunos aprovados tem na turma? "))
total=qtdeH+qtdeM
qtdeREP=total-qtdeAP
porc_H=(qtdeH*100)/total
porc_F=(qtdeH*100)/total
porc_REP=(qtdeREP*100)/total
print("\n\nResultados dos cálculos")
print("\nPORCENTAGEM DE ALUNOS DO SEXO MASCULINO: %3.2f"%porc_H,"%")
print("\nPORCENTAGEM DE ALUNOS DO SEXO FEMININO: %3.2f"%porc_F,"%")
print("\nPORCENTAGEM DE ALUNOS REPROVADOS: %3.2f"%porc_REP,"%")
print("\nTOTAL DE ALUNOS DA TURMA: ",total,"alunos")