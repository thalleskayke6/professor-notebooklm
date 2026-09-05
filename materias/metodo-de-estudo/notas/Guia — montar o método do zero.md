---
tags: [pcpr2026, metodo, anki, setup]
atualizado: 2026-08-18
---

# Guia — montar o método do zero

Como reproduzir o projeto que transforma excertos de lei, doutrina e jurisprudência em itens **Certo ou Errado** no estilo FGV, já exportados em CSV pronto para o Anki. ~10 minutos de instalação, sem programar.

Ver também: [[Método FGV — instruções do projeto]] · [[Workflow de exportação Anki]] · [[Mapa de baralhos Anki]]

## Passos

1. **Criar o projeto** — claude.ai → Projetos → Criar projeto.
2. **Colar as instruções** — o conteúdo de [[Método FGV — instruções do projeto]] vai inteiro no campo *Instruções do projeto*. Vale para toda conversa dentro do projeto; não se repete o prompt a cada uso.
3. **Subir a base de conhecimento** — o workflow de exportação e o mapa de baralhos. Subir também cadernos de questões reais da FGV em PDF: servem de calibragem de estilo, não só de conteúdo.
4. **Adaptar o mapa de baralhos** — o mapa traz a coleção da PCPR 2026. Em outra coleção, substituir a raiz e a lista de matérias pelos nomes exatos da barra lateral do Anki. Alternativa preguiçosa: exportar a coleção, mandar para o Claude e pedir que reescreva o mapa com a árvore real.
5. **Usar** — abrir conversa dentro do projeto e mandar os excertos, um lote por vez. Lotes de **8 a 12 excertos** funcionam bem; acima disso a proporção Certo/Errado desanda.
6. **Importar no Anki** — Arquivo → Importar → escolher o `.csv`. Em **Duplicatas**, deixar *Atualizar nota existente*.

## O que volta em cada lote

1. Os itens em texto, com gabarito e código da pegadinha.
2. O mesmo gabarito em HTML, pronto para colar no editor do Anki.
3. Dois CSVs para importar direto (**só quando pedido** — ver [[Workflow de exportação Anki]]).
4. Relatório curto, apenas em lote de 6+ itens: quantos Certos, quantos Errados, quais pegadinhas apareceram.

## Note types pressupostos

- `Concurso - Pergunta e Resposta` → Pergunta | Fonte | Resposta | Detalhe | Pegadinha | Mnemonico | Extra
- `Concurso - Cloze` → Texto | Fonte | Detalhe | Pegadinha | Mnemonico | Extra

A **ordem dos campos** importa mais do que parece: é ela que define em qual campo cada coluna do CSV cai.

## Ajustes que costumam valer a pena

- **Tirar o código da pegadinha do verso** — para não enviesar a revisão seguinte.
- **Baixar o nível de 8/10 para 6/10** em matéria ainda em primeira leitura: item nível 8 nessa fase vira frustração, não estudo.
- **Só Certo/Errado, sem Cloze** — editar a regra 2 do workflow de exportação.
- **Outra banca** — a camada FGV (micro-hipótese fática, erro em uma palavra, jurisprudência tratada como lei) é o que dá a identidade. Migrar para Cebraspe significa reescrever a seção inteira, não trocar o nome da banca.
