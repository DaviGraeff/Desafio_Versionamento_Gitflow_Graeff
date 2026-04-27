# Calculadora CLI - Desafio Gitflow

##  Descrição
Projeto desenvolvido em Python com o objetivo principal de praticar conceitos de Git, versionamento (Gitflow) e colaboração utilizando o GitHub. Recentemente, a aplicação passou por uma grande refatoração estrutural focada no **Princípio da Responsabilidade Única (SRP)** da arquitetura SOLID.

##  Objetivos do Projeto
* Exercitar o uso prático de Git e GitHub em equipe.
* Compreender, refatorar e adaptar códigos legados.
* Implementar boas práticas de arquitetura de software (SRP).
* Aplicar Integração Contínua (CI) e Testes Unitários.

##  Arquitetura e Refatoração (SRP)
O código principal foi dividido em módulos específicos, garantindo que cada arquivo tenha apenas uma responsabilidade:
* **`utils/operacoes.py`**: Contém exclusivamente as regras de negócio e cálculos matemáticos.
* **`interface.py`**: Responsável por toda a interação com o usuário (coletar inputs, exibir menus e imprimir mensagens coloridas).
* **`config.py` e `exceptions.py`**: Módulos utilitários para configurações globais e tratamento de erros customizados (`OperationError`, `NumericValueError`).
* **`main.py`**: Atua estritamente como orquestrador, ligando a interface às operações e gerenciando o histórico.

##  Como Executar Localmente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.9+ instalado em sua máquina.

### 2. Instalação das dependências
Recomenda-se o uso de um ambiente virtual para isolar os pacotes:
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executando a Aplicação
```bash
python main.py
```

##  Testes e Hooks de Pre-commit

O projeto conta com cobertura de testes unitários (`pytest`) para garantir a estabilidade das operações e da interface.

**Para rodar os testes manualmente:**
```bash
pytest tests/ -v
```

**Configuração do pre-commit hook:**
Para garantir a qualidade do código colaborativo, temos um hook que roda a suíte de testes automaticamente e impede commits com erros. Após clonar o repositório, ative-o executando:
```bash
./scripts/setup-hooks.sh
```
*(Isso configurará o `core.hooksPath` para `.githooks`.)*

## Tecnologias Utilizadas
* **Python** - Estrutura principal do código
* **Pandas** - Organização e exibição do histórico de operações
* **Colorama** - Estilização e cores no terminal para melhor UX
* **Pytest** - Framework para criação e execução de testes unitários

##  Aviso
Este é um projeto de estudo, sem fins comerciais. Não representa um produto final ou pronto para uso em produção.
