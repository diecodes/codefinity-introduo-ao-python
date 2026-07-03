"""
O sistema do seu supermercado foi projetado para rastrear o inventário de itens em diferentes prateleiras usando tuplas, pois as tuplas garantem que os dados sejam imutáveis após serem definidos.

No entanto, a loja precisa monitorar certos itens e acompanhar suas quantidades ou posições para auxiliar no reabastecimento ou reorganização.

Sua tarefa é analisar e gerenciar os dados de inventário utilizando tuplas para determinar certos indicadores e tomar decisões com base em critérios específicos.

Tarefa

Gerencie uma tupla representando uma prateleira de frutas realizando operações para contar, localizar e verificar os níveis de estoque.

    Contar quantas vezes "apples" aparece na tupla shelf. Armazene esse valor em apple_count e imprima: "Number of Apples: <apple_count>".

    Localizar o índice da primeira ocorrência de "bananas" na tupla shelf. Armazene o índice em banana_index e imprima: "First Banana Index: <banana_index>".

    Verificar se o número de maçãs é menor que 5. Se for verdadeiro, imprima: "Apples need to be restocked." Caso contrário, imprima: "Apples are sufficiently stocked."

    Contar quantas vezes "grapes" aparece na tupla shelf. Se as uvas aparecerem apenas uma vez, imprima: "Grapes need to be restocked." Caso contrário, imprima: "Grapes are sufficiently stocked."

    Verificar se "oranges" existe na tupla shelf. Se existir, imprima o índice com: "Oranges are at index: <orange_index>". Se não existir, imprima: "Oranges are out of stock."

Requisitos de Saída

    Imprimir o número de maçãs: "Number of Apples: <apple_count>".
    Imprimir o índice da primeira ocorrência de bananas: "First Banana Index: <banana_index>".
    Imprimir uma mensagem sobre o status do estoque de maçãs: "Apples need to be restocked." ou "Apples are sufficiently stocked."
    Imprimir uma mensagem sobre o status do estoque de uvas: "Grapes need to be restocked." ou "Grapes are sufficiently stocked."
    Imprimir o índice das laranjas se existirem: "Oranges are at index: <orange_index>", ou "Oranges are out of stock."


"""
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")