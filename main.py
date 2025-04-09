import time

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Rabin-Karp
def rabin_karp(text, pattern):
    d = 256  # Número de caracteres possíveis
    q = 101  # Um número primo
    M = len(pattern)
    N = len(text)
    h = pow(d, M - 1) % q
    p = 0  # hash do padrão
    t = 0  # hash da janela de texto
    result = []

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(N - M + 1):
        if p == t:
            if text[s:s + M] == pattern:
                result.append(s)
        if s < N - M:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + M])) % q
            t = (t + q) % q  # corrigir valor negativo
    return result


# Knuth-Morris-Pratt
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(text, pattern):
    lps = compute_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return result


# Boyer-Moore (bad character heuristic)
def bad_char_heuristic(pattern):
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

# Executando tudo
if __name__ == '__main__':
    path = 'shakespeare.txt'
    pattern = 'love'
    content = read_file(path)

    print(f'🔍 Buscando a palavra "{pattern}"...\n')

    start = time.time()
    result_rk = rabin_karp(content, pattern)
    print(f'📌 Rabin-Karp encontrou {len(result_rk)} ocorrência(s)')
    print(f'⏱️ Tempo: {time.time() - start:.6f} segundos\n')

    start = time.time()
    result_kmp = kmp(content, pattern)
    print(f'📌 KMP encontrou {len(result_kmp)} ocorrência(s)')
    print(f'⏱️ Tempo: {time.time() - start:.6f} segundos\n')