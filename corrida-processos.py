import time
import os
import random

NUM_PROCESSOS = random.randint(3, 5)
# uso de IA
QUANTUM = 0.2  # tempo de fatia para Round Robin e Prioridade Preemptiva (segundos)
TAMANHO_BARRA = 30

nomes = ["Bubble Sort", "Shell Sort", "Quick Sort", "Insertion Sort", "Selection Sort"]
processos = []
for i in range(NUM_PROCESSOS):
    tempo_total = random.uniform(4, 12) 
    proc = {
        "nome": nomes[i],
        "tempo_total": tempo_total,
        "restante": tempo_total,
        "progresso": 0.0,
        "prioridade": random.randint(1, 10),  
        "finalizado": False,
        "tempo_conclusao": None
    }
    processos.append(proc)

def desenhar_barras(lista_procs):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Corrida de Processos ===")
    for p in lista_procs:
        porcent = (p['progresso'] / p['tempo_total']) * 100
        preenchido = int((p['progresso'] / p['tempo_total']) * TAMANHO_BARRA)
        barra = '█' * preenchido + '-' * (TAMANHO_BARRA - preenchido)
        simbolo = '⚙️ ' if not p['finalizado'] else '🏁 '
        print(f"{simbolo}{p['nome']:<6} |{barra}| {porcent:6.2f}% | Rest: {p['restante']:4.1f}s | Prio: {p['prioridade']}")
    print()
# uso de IA
# Simulação Round Robin (quantum circular)
def simular_round_robin(lista_procs):
    inicio = time.time()
    fila = lista_procs.copy()
    while any(not p['finalizado'] for p in fila):
        for p in fila:
            if p['finalizado']:
                continue
            rodar = min(QUANTUM, p['restante'])
            time.sleep(rodar)
            p['restante'] -= rodar
            p['progresso'] = p['tempo_total'] - p['restante']
            if p['restante'] <= 0:
                p['finalizado'] = True
                p['tempo_conclusao'] = time.time() - inicio
            desenhar_barras(fila)
    return fila

#Uso de IA
# Simulação de Prioridade Preemptiva
def simular_prioridade_preemptiva(lista_procs):
    inicio = time.time()
    # Continua enquanto houver processos não finalizados
    while any(not p['finalizado'] for p in lista_procs):
        # Seleciona pronto com maior prioridade
        disponiveis = [p for p in lista_procs if not p['finalizado']]
        # Em caso de empate, maior tempo_restante quebra
        atual = max(disponiveis, key=lambda x: (x['prioridade'], x['restante']))
        rodar = min(QUANTUM, atual['restante'])
        time.sleep(rodar)
        atual['restante'] -= rodar
        atual['progresso'] = atual['tempo_total'] - atual['restante']
        if atual['restante'] <= 0:
            atual['finalizado'] = True
            atual['tempo_conclusao'] = time.time() - inicio
        desenhar_barras(lista_procs)
    return lista_procs


def escolher_politica():
    print("Escolha a política de escalonamento:")
    print("1) Round Robin")
    print("2) Prioridade Preemptiva")
    escolha = input("> ")
    return 'rr' if escolha == '1' else 'preemp'
def principal():
    politica = escolher_politica()
    nome_pol = 'Round Robin' if politica == 'rr' else 'Prioridade Preemptiva'
    print(f"Executando política: {nome_pol}...\n")
    time.sleep(1)

    
    simulacao = [dict(p) for p in processos]
    print("Estado inicial dos processos:")
    desenhar_barras(simulacao)
    time.sleep(1)

   
    if politica == 'rr':
        resultado = simular_round_robin(simulacao)
    else:
        resultado = simular_prioridade_preemptiva(simulacao)

    vencedor = min(resultado, key=lambda x: x['tempo_conclusao'])
    print(f"\n🏆 Vencedor: {vencedor['nome']} em {vencedor['tempo_conclusao']:.2f}s!")
    print("Fim da corrida!")

if __name__ == '__main__':
    principal()
