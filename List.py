from datetime import datetime

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(descricao, data=None):
    tarefa = {
        "descricao": descricao,
        "data": data if data else datetime.now().strftime("%Y-%m-%d"),
        "concluida": False
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para marcar uma tarefa como concluída
def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")

# Função para editar uma tarefa
def editar_tarefa(indice, nova_descricao, nova_data=None):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["descricao"] = nova_descricao
        if nova_data:
            tarefas[indice]["data"] = nova_data
        print("Tarefa editada com sucesso!")
    else:
        print("Índice inválido.")

# Função para remover uma tarefa
def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida com sucesso!")
    else:
        print("Índice inválido.")

# Função para filtrar tarefas por status ou data
def filtrar_tarefas(status=None, data=None):
    resultado = []
    for tarefa in tarefas:
        if (status is None or tarefa["concluida"] == status) and (data is None or tarefa["data"] == data):
            resultado.append(tarefa)
    return resultado

# Função para listar todas as tarefas
def listar_tarefas():
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - {tarefa['data']} - {status}")

# Exemplo de uso
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer compras", "2024-11-10")
listar_tarefas()

marcar_concluida(0)
editar_tarefa(1, "Fazer compras no mercado", "2024-11-11")
listar_tarefas()

tarefas_concluidas = filtrar_tarefas(status=True)
print("\nTarefas concluídas:", tarefas_concluidas)

remover_tarefa(0)
listar_tarefas()
