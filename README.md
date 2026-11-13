<div align="center">

# 👑 ClusteringRealities — Seletor de Candidatos

**Agrupamento de candidatos a um reality show por títulos de nobreza e fama, com k-means implementado de raiz em Python.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Sem dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-brightgreen)
![FCUL](https://img.shields.io/badge/FCUL-Programa%C3%A7%C3%A3o%20II-blue)

</div>

---

## 📋 Informação

| | |
|---|---|
| **Autores** | Pedro Rosa (60294) · Matias D'Avó (60259) — Grupo 35 |
| **Unidade curricular** | Programação II — Licenciatura em Tecnologias de Informação (LTI) |
| **Instituição** | Faculdade de Ciências da Universidade de Lisboa |
| **Ano letivo** | 2022/2023 |
| **Última atualização** | 13 de novembro de 2026 |

---

## 🎬 Sobre o projeto

A produtora fictícia **RealidadeInfeliz** recebe milhares de candidaturas para o seu novo reality show. Cada candidato traz consigo a "linhagem" da família: os títulos do pai, da mãe e dos quatro avós — de *imperador* a *plebeu*, passando por *tiktokStar* ou *vencedorFestivalRTP*.

O programa converte cada título num valor numérico e agrupa os candidatos em **k grupos** semelhantes, escolhendo para cada grupo um **exemplar** (o candidato mais representativo). Assim a produção consegue um elenco diverso, com um representante de cada "tipo" de candidato.

## ✨ Funcionalidades

- **K-means implementado de raiz** — sem `scikit-learn`, `SciPy` ou `Pyclustering` (proibidos no enunciado).
- **Distância euclidiana** entre vetores de 6 características (pai, mãe e quatro avós).
- **Exemplares opcionais** — o ficheiro de entrada pode indicar os exemplares iniciais; caso contrário, são escolhidos automaticamente.
- **Hierarquia de títulos configurável** através do ficheiro [titles.txt](titles.txt).

## 📁 Estrutura

```
ClusteringRealidadeInfeliz/
├── clusteringRealities.py   # Programa principal (leitura de argumentos e escrita do resultado)
├── clustering.py            # Classes Example e Cluster, k-means e leitura de ficheiros
├── titles.txt               # Hierarquia de títulos (grau; masculino; feminino)
├── conjuntosTeste/          # Ficheiros de candidatos e respetivas saídas esperadas
├── testSets/                # Conjuntos de teste adicionais
└── Relatório/relGrupo35.pdf # Relatório do projeto
```

---

## 🚀 Como executar

### Pré-requisitos

- **Python 3** (não são necessárias bibliotecas externas)

### Sintaxe

```bash
python clusteringRealities.py <k> <ficheiro_titulos> <ficheiro_candidatos>
```

| Argumento | Descrição |
|---|---|
| `k` | Número de grupos (clusters) a criar |
| `ficheiro_titulos` | Ficheiro com a hierarquia de títulos (ex.: `titles.txt`) |
| `ficheiro_candidatos` | Ficheiro com os candidatos (e, opcionalmente, os exemplares) |

> 💡 Em Linux/macOS pode ser necessário usar `python3` em vez de `python`.

### Exemplo

```bash
git clone https://github.com/pedrorosa3/ClusteringRealidadeInfeliz.git
cd ClusteringRealidadeInfeliz
python clusteringRealities.py 2 titles.txt conjuntosTeste/candidates1.txt
```

O resultado é escrito no ficheiro **`candidates.txt`**, na pasta onde o comando é executado.

---

## 📄 Formato dos ficheiros

### Ficheiro de títulos

```text
#degree; title name masculine; feminine
14; imperador; imperatriz
13; rei; rainha
12; regente; regente
...
```

### Ficheiro de candidatos

As três primeiras linhas são cabeçalho. A secção `#Exemplars:` é **opcional**; se existir, deve ter exatamente `k` exemplares.

```text
#Name and features:
#Name; father's title; mother's; paternal grandfather's; paternal grandmother's; maternal grandfather's; maternal grandmother's
#Candidates:
Ana; plebeu; plebeia; plebeu; plebeia; plebeu; plebeia
Catarina; imperador; imperatriz; imperador; imperatriz; imperador; imperatriz
#Exemplars:
Bruno; plebeu; plebeia; plebeu; plebeia; plebeu; plebeia
Diogo; imperador; imperatriz; imperador; imperatriz; imperador; imperatriz
```

### Ficheiro de saída (`candidates.txt`)

```text
#exemplar 1:
Bruno; plebeu; plebeia; plebeu; plebeia; plebeu; plebeia
#cluster 1:
Ana; plebeu; plebeia; plebeu; plebeia; plebeu; plebeia

#exemplar 2:
Diogo; imperador; imperatriz; imperador; imperatriz; imperador; imperatriz
#cluster 2:
Catarina; imperador; imperatriz; imperador; imperatriz; imperador; imperatriz
```

---

## 🧪 Testes

A pasta [conjuntosTeste/](conjuntosTeste/) contém ficheiros de entrada (`candidatesN.txt`) e as saídas esperadas (`saidaN.txt`) para comparar com o resultado do programa.

---

<div align="center">

Feito por **Pedro Rosa** e **Matias D'Avó** · FCUL 2022/2023

</div>
