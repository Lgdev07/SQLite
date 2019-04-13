import sqlite3

conn = sqlite3.connect('jogos.db')

c = conn.cursor()
c.execute("SELECT * FROM jogos ")
def incluir():
    t = 'Título: ' + input("Digite o nome do jogo: ")
    ano = 'Ano: ' + input("Digite o ano do jogo: ")
    r = 'Nota: ' + input("Qual a nota? ")
    a = 'Considerações: ' + input("Quais são suas considerações sobre ele? ")
    c.execute("INSERT INTO jogos VALUES (:titulo, :ano, :nota, :anotacao)", {'titulo': t, 'ano': ano, 'nota': r, 'anotacao': a})
    print('\nTítulo incluído com sucesso\n')
    conn.commit()
def atualizar():
    t = 'Título: ' + input("Qual o titulo da anotação que quer mudar? ")
    q = 'Ano: ' + input("Atualizar ANO = ")
    i = 'Nota: ' + input("Atualizar NOTA = ")
    f = 'Considerações: ' + input("Atualizar CONSIDEREÇÕES = ")
    with conn:
            c.execute("""UPDATE jogos SET ano = :q,
                                          nota = :i,
                                          anotacao = :f       
                        WHERE titulo = :t""", {'t': t, 'q': q, 'i': i, 'f': f})
    print('\nTítulo atualizado com sucesso\n')
    conn.commit()
def removertudo():
    with conn:
        c.execute("DELETE FROM jogos")
    print('\nAnotações excluídas com sucesso\n')
    conn.commit()
def removerum():
    t = 'Título: ' + input('Digite o título que deseja excluir: ')
    with conn:
        c.execute("DELETE FROM jogos WHERE titulo = :t", {'t':t})
    print('\nTítulo excluído com sucesso\n')
    conn.commit()

# c.execute(""" CREATE TABLE jogos (
#                 titulo text,
#                 ano integer,
#                 nota integer,
#                 anotacao text
#                 )""")


print('\n', '=+' * 10, "Bem-Vindo a sua coleção de jogos", '+=' * 10, '\n')

print('Atualmente elas são: \n')

for i in c.fetchall():
    for k in i:
        print(k)
    print()


while True:
    escolha = int(input("""Gostaria de fazer o que?\n\n1 - Incluir jogo\n2 - Alterar informações de sua anotação\n3 - Remover uma anotação\n4 - Remover todas as anotações\n5 - Ver anotações\n6 - Sair\n"""))
    if escolha == 1:
        incluir()
    elif escolha == 2:
        atualizar()
    elif escolha == 3:
        removerum()
    elif escolha == 4:
        removertudo()
    elif escolha == 5:
        c.execute("SELECT * FROM jogos ")
        for i in c.fetchall():
            for k in i:
                print(k)
            print()
    elif escolha == 6:
        break


conn.close()