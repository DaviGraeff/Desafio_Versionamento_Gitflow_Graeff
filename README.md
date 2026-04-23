# Desafio_Versionamento_Gitflow


# Descrição
Projeto desenvolvido com objetivo principal de praticar conceitos de Git, versionamento e colaboração utilizando o GitHub.


# Objetivos
* Exercitar o uso de Git e GitHub em equipe
* Compreender e adaptar códigos existentes


# Tecnologias utilizadas
* Python - estrutura do código
* Pandas - organizar e exibir o histórico das operações de forma estruturada 
* Colorama - adicionar cores ao terminal melhorando a experiência visual


# Aviso
Este é um projeto de estudo, sem fins comerciais.
Não representa um produto final ou pronto para uso em produção.

# Configuração do pre-commit hook
Após clonar o repositório, execute o script abaixo para ativar os hooks locais:

```bash
./scripts/setup-hooks.sh
```

Esse script configura o `core.hooksPath` para `.githooks`, garantindo que o hook de pre-commit seja executado antes de cada commit local.
