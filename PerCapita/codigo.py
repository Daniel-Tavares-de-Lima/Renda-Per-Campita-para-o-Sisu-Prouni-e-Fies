#Perguntas

pergunta = int(input("Quantas pessoas moram com você? "))
pergunta2 = int(input("Dessas {} pessoas, quantas pessoas ganham salário?".format(pergunta)))
pergunta3 = int(input("OK, agora, informe o (TOTAL) que essas {} recebem! R$ ".format(pergunta2)))

#calculo
salario_minimo = 1100
conta = pergunta3 / pergunta
conta2 = float(conta / salario_minimo)

#conclusão

if conta2 <= 1.50:
     print("Sua renda Per Capita é de {:.2f} salários minimos.\n Como (atualmente) o Fies, Prouni e o Sisu estipulam como base um salário minimo e meio (1,5)\n Você tem direito a 100 percento do beneficio".format(conta2))

else:
     print("Sua renda Per Capita é de {:.2f} salários minimos\n Como (atualmente) o Fies, Prouni e o Sisu estipulam como base um salário minimo e meio (1,5)\n Você tem direito a 50 percento do beneficio".format(conta2))
