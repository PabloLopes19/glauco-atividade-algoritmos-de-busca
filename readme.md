# 🧩 Reflexão (responda em grupo ou individualmente):

**Alunos:** Anna Loz, Lucas Gadonski, Matheus Lofy, Pablo Lopes, Sabine Freiman.

Os dois algoritmos retornaram os mesmos resultados?

**1. Qual algoritmo foi mais rápido?**

Foi o KMP, com 0.016781 segundos.

**2. O tamanho do texto ou do trecho buscado influencia no tempo de execução?**

Usando KMP, segue o tempo de execução de cada trecho buscado:

**"love"** 0.017691s
**"to be or not to be"**: 0.017047s
**"Capitu"**: 0.017371s

**3. Em que situações um algoritmo pode ser preferido ao outro?**

**Rabin-Karp**

- Você tem várias palavras para procurar (ex: blacklist de palavras).
- Tolerância a hash collisions é aceitável.

**Knuth-Morris-Pratt (KMP)**

- Precisa de consistência no tempo (ex: sistemas embarcados ou tempo real).
- Busca única e frequente.
- Padrão com muitos prefixos/sufixos repetidos.
