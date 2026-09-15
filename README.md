# Gov Spend Analyzer

**Grupo 5 | AI Talent Academy White Cube**

Este projeto tem como objetivo processar, limpar e analisar os dados do **Cartão de Pagamento do Governo Federal (CPGF)**. Utilizamos a **Arquitetura Medalhão** (Bronze, Silver e Gold) para garantir a integridade, governança e otimização dos dados para futuras visualizações em Business Intelligence e modelagens estatísticas.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Manipulação de Dados:** Pandas
* **Armazenamento Otimizado:** PyArrow (formato `.parquet`)
* **Controle de Versão:** Git / GitHub

---

## Estrutura do Projeto

O repositório está organizado seguindo boas práticas de Engenharia de Dados:

```text
analise_cpgf/
│
├── data/
│   ├── 01_bronze/       # Dados brutos originais (.csv) - Ignorados no Git
│   ├── 02_silver/       # Dados limpos e tipados (.parquet) - Ignorados no Git
│   └── 03_gold/         # Agregações e regras de negócio futuras
│
├── docs/                # Entregáveis de Governança (LGPD, Dicionário)
├── notebooks/           # Exploração e validação de dados (Jupyter)
│
├── src/                 # Scripts de processamento (ETL)
│   └── processamento_silver.py
│
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Omissão de arquivos sensíveis/pesados
```

---

## Status do Projeto

### Concluído — Fundações

* Definição da Arquitetura Medalhão e Governança (*Privacy by Design*).
* Diagnóstico inicial de conformidade com a LGPD.
* Configuração do repositório e dos ambientes virtuais.
* **Camada Bronze:** alocação segura dos dados brutos.

### Em Revisão / Testes — Engenharia de Dados

O pipeline principal da **Camada Silver** foi executado e gerou o arquivo `.parquet` otimizado.

Os seguintes tratamentos aguardam validação por meio de *Code Review*:

* Tratamento e preservação de valores nulos relacionados a dados sigilosos.
* Padronização de strings, incluindo cabeçalhos e variáveis categóricas.
* Conversão de valores financeiros para formato numérico decimal.
* Padronização temporal e conversão para o tipo `datetime`.

### Em Andamento — Trabalho Paralelo da Equipe

* **Governança de Dados:** construção da documentação oficial e estruturação do **Dicionário de Dados**, desenvolvidos ativamente pelos membros da equipe com base na versão finalizada da Camada Silver.

### Próximos Passos — Backlog

* **Engenharia — Camada Silver:** implementação de agrupadores lógicos e tratamento de anomalias logísticas.
* **Engenharia — Camada Gold:** pseudonimiz
