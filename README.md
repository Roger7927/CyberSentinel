# 🛡️ Cyber Sentinel v8.0 - Terminal Defense System

**Cyber Sentinel** é um simulador dinâmico de monitoramento de rede desenvolvido em **C#** para o ambiente **Linux (Ubuntu)**. O projeto foca em lógica de programação, manipulação de buffers de console e interatividade em tempo real.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** C# (.NET 8.0)
- **Interface:** Spectre.Console (TUI - Terminal User Interface)
- **Ambiente:** Linux Ubuntu no Acer Aspire 5 (Ryzen 7)
- **Conceitos:** Loops infinitos, Programação Orientada a Eventos e Persistência de Dados (Logs).

## 🧠 Lógica de Funcionamento (Abstração ADS)
O sistema utiliza uma metáfora de **"Bolinhas e Caixas"**:
1. **As Caixas (Vetores/Arrays):** Representam os Nodes da rede carregados na Memória RAM.
2. **As Bolinhas (Dados):** Representam o status de integridade sorteado via algoritmos de probabilidade (Random).
3. **O Radar (Processamento):** Analisa o conteúdo de cada caixa e decide visualmente se o sistema entra em modo crítico ou nominal.

## 🛠️ Como Executar
1. Certifique-se de ter o .NET SDK instalado.
2. Instale as dependências: `dotnet add package Spectre.Console`
3. Execute o motor: `dotnet run`

---
*Projeto acadêmico desenvolvido por Guillermo Roger Hernandez Chandia para portfólio de ADS.*
