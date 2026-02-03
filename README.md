# Corrida de Processos

Este minijogo em Python simula uma **corrida entre processos** no terminal, demonstrando conceitos de escalonamento de CPU, tempo de execução e concorrência.

## 🚀 Como rodar o jogo

1. **Pré-requisitos**:
   - Python 3.6 ou superior instalado.
   - Terminal (Windows, macOS ou Linux).
2. **Passos**:
   ```bash
   # Clone ou baixe o repositório
   git clone https://github.com/jjvaldezzzzz/corrida-de-algoritmos-de-escalonamento
   cd corrida-processos

   # Execute o script
   python corrida_processos.py
   ```
3. **Interaja**:
   - Escolha a política de escalonamento (Round Robin ou Prioridade Preemptiva).
   - Observe as barras de progresso atualizarem em tempo real.

## 🏁 Algoritmos de escalonamento implementados

1. **Round Robin**
   - Cada processo recebe uma fatia fixa de tempo (`QUANTUM = 0.2s`).
   - Ao final da fatia, o processo volta para o fim da fila se não tiver terminado.

2. **Prioridade Preemptiva**
   - A cada fatia, seleciona-se o processo **com maior prioridade** (1–10).
   - Em caso de empate, é escolhido o que tiver **maior tempo restante**.
   - Após cada fatia, o escalonador reavalia prioridades para decidir o próximo processo.

> **Observação**: As prioridades são atribuídas aleatoriamente a cada execução para variar o comportamento.

## ℹ️ Informações extras

- **Número de processos**: gerado aleatoriamente entre 3 e 5.
- **Tempos de execução**: cada processo tem entre 4 e 12 segundos de duração.
- **Visual**: as barras usam blocos `█` para progresso e `-` para espaço restante, além de símbolos `⚙️` (em execução) e `🏁` (finalizado).
- **Personalização**: é possível ajustar no código:
  - `NUM_PROCESSOS` (quantidade de processos)
  - `QUANTUM` (tamanho da fatia de tempo)
  - `TAMANHO_BARRA` (comprimento gráfico da barra)
- **Uso de IA**: Chat GPT o4-mini-high foi utilizado para ajudar a implementar os algoritmos de escalonamento
---

© 2025 — Projeto desenvolvido em Python para aprendizado de sistemas operacionais e escalonamento de processos.
