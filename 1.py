import random

list_de_compras = ["Leite", "Ovos", "Açucar"] # ESTA LISTA CONTEM COMPRAS PARA FAZER PARA CASA
list_de_quem_compra = ["Tiago", "Martim"]

valor_aleatorio1_da_list = random.choice(list_de_quem_compra) # PEGA VALOR ALEATORIO DA LISTA list_de_quem_compra
valor_aleatorio2_da_list = random.choice(list_de_compras) # PEGA VALOR ALEATORIO DA LISTA list_de_compras

print(f"{valor_aleatorio1_da_list} Vai comprar {valor_aleatorio2_da_list}")

################## DESAFIO | Um jogo que escolha um personagem aleatorio de uma lista e diga a sua qualidade de uma outra lsita ###############

list_de_personagens = ["Hulk", "Iron MAN", "SpiderMan"]
list_de_qualidades = ["rápido", "Agil", "forte"]

valor_aleatorio1_da_list1 = random.choice(list_de_personagens)
valor_aleatorio2_da_list2 = random.choice(list_de_qualidades)

print(f"O personagem é {valor_aleatorio1_da_list1} e a sua qualidade é {valor_aleatorio2_da_list2}")