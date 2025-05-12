name = ["Daniel" , "therock balairino" , "gustavo viadin" , "erick pablo vitar" , "zecarlos " , "celia"]
message = f" Vamos para faculdade {name[4].title()}"
print(message)

moto = ["cb300" , "cb500" , "mt07" , "ducati" , "capacete top" , "BMW R1000"]
message = f" Vou usar a moto {moto[2].title()}"
print(message)

moto = ["Honda" , "Yamaha" , "Suzuki"]
print(moto)
moto[0] = "Ducati"
print(moto)

moto = ["Honda" , "Yamaha" , "Suzuki"]
print(moto)
moto.append("Ducati")
print(moto)

moto = []
moto.append("Honda")
moto.append("Suzuki")
moto.append("Ducati")
moto.append("Yamaha")
moto.append("BMW")
moto.append("Kawazaki")
moto.insert(0, "Ducati")
del moto[3]
print(moto)


carro = ["golf" , "onix" , "HB20"]
print(carro)
popped_carro = carro.pop()
print(carro)
print(popped_carro)
last_owned = carro.pop()
print(f"the last car I Owned wa a {last_owned.title()}.")

carro = ["onix", "hb20" , "golf"]
first_owned = carro.pop(0)
print(f"the first car i owned was a {first_owned.title()}.")

onibus = ["mercedes" , "bmw" , "wolks"]
print(onibus)
too_expensive = "wolks"
onibus.remove(too_expensive)
print(onibus)
print(f"\nA {too_expensive.title()} is too expensive for me." )


#Exercicio da pagina 77 3.4 Lista de convidado.
jantar = ["mãe" , "pai" , "irmã"]
print(jantar)
print(message)
message = f"Gostaria de jantar comigo {jantar[1].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[2].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[0].title()}"
print(message)
print("mãe" , "pai")
jantar[0] = "irmão"
jantar[1] = "Primo"
print(jantar)
message = f"Gostaria de jantar comigo {jantar[2].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[0].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[1].title()}"
print(message)
jantar.insert(0, "Vó")
jantar.insert(3, "prima")
jantar.append("Tia")
print(jantar)
message = f"Gostaria de jantar comigo {jantar[1].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[0].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[2].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[3].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[4].title()}"
print(message)
message = f"Gostaria de jantar comigo {jantar[5].title()}"
print(message)
print()

