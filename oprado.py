# TAD posicao
# Construtor

def cria_posicao(x, y):
    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        raise ValueError('cria_posicao: argumentos invalidos')

    posicao = [x, y]

    return posicao


def cria_copia_posicao(posicao):
    if not eh_posicao(posicao):
        raise ValueError('cria_copia_posicao: argumento invalido')

    copia_posicao = list(posicao)

    return copia_posicao


# Seletores

def obter_pos_x(posicao):
    return posicao[0]


def obter_pos_y(posicao):
    return posicao[1]


# Reconhecedor

def eh_posicao(posicao):
    if not (isinstance(posicao, list) and all(isinstance(axis, int) for axis in posicao) and
            len(posicao) == 2 and posicao[0] >= 0 and posicao[1] >= 0):
        return False
    return True


# Teste

def posicoes_iguais(pos1, pos2):
    return eh_posicao(pos1) and eh_posicao(pos2) and pos1 == pos2


# Transformador

def posicao_para_str(posicao):
    return f"({posicao[0]}, {posicao[1]})"


# Funções de alto nível

def obter_posicoes_adjacentes(posicao):
    posicoes_adjacentes = []

    if eh_posicao([posicao[0], posicao[1] - 1]):
        posicoes_adjacentes.append([posicao[0], posicao[1] - 1])

    if eh_posicao([posicao[0] + 1, posicao[1]]):
        posicoes_adjacentes.append([posicao[0] + 1, posicao[1]])

    if eh_posicao([posicao[0], posicao[1] + 1]):
        posicoes_adjacentes.append([posicao[0], posicao[1] + 1])

    if eh_posicao([posicao[0] - 1, posicao[1]]):
        posicoes_adjacentes.append([posicao[0] - 1, posicao[1]])

    return tuple(posicoes_adjacentes)


def ordenar_posicoes(posicoes):
    posicoes = list(posicoes)
    posicoes.sort(key=lambda x: (x[1], x[0]))
    posicoes = tuple(posicoes)

    return posicoes


# TAD Animal
# Presa (espécie, idade, frequência de reprodução)
# Predador (espécie, idade, frequência de reprodução, fome, frequência de alimentação)
# Construtor

def cria_animal(s, r, a):
    if not (isinstance(s, str) and s and isinstance(r, int) and r > 0 and isinstance(a, int) and a >= 0):
        raise ValueError('cria_animal: argumentos invalidos')

    if a == 0:
        animal = [s, 0, r]
    else:
        animal = [s, 0, r, 0, a]

    return animal


def cria_copia_animal(animal):
    if not eh_animal(animal):
        raise ValueError('cria_copia_animal: argumento invalido')

    copia_animal = list(animal)

    return copia_animal


# Seletores

def obter_especie(animal):
    return animal[0]


def obter_freq_reproducao(animal):
    return animal[2]


def obter_freq_alimentacao(animal):
    if len(animal) == 5:
        return animal[4]
    return 0


def obter_idade(animal):
    return animal[1]


def obter_fome(animal):
    if len(animal) == 5:
        return animal[3]
    return 0


# Modificadores

def aumenta_idade(animal):
    animal[1] += 1

    return animal


def reset_idade(animal):
    animal[1] = 0

    return animal


def aumenta_fome(animal):
    if eh_predador(animal):
        animal[3] += 1

    return animal


def reset_fome(animal):
    if eh_predador(animal):
        animal[3] = 0

    return animal


# Reconhecedor

def eh_animal(animal):
    def requisitos_comuns(animal_aux):
        if isinstance(animal_aux, list) and isinstance(animal_aux[0], str) and \
                animal_aux[0] and isinstance(animal_aux[1], int) and animal_aux[1] >= 0 and \
                isinstance(animal_aux[2], int) and animal_aux[2] > 0:
            return True
        return False

    def requisitos_presa(animal_aux):
        if requisitos_comuns(animal_aux) and len(animal_aux) == 3:
            return True
        return False

    def requisitos_predador(animal_aux):
        if requisitos_comuns(animal_aux) and isinstance(animal_aux[3], int) and \
                animal_aux[3] >= 0 and isinstance(animal_aux[4], int) and animal_aux[4] > 0 and len(animal_aux) == 5:
            return True
        return False

    if requisitos_presa(animal) or requisitos_predador(animal):
        return True
    return False


def eh_predador(animal):
    if eh_animal(animal) and len(animal) == 5:
        return True
    return False


def eh_presa(animal):
    if eh_animal(animal) and len(animal) == 3:
        return True
    return False


# Teste

def animais_iguais(a1, a2):
    return eh_animal(a1) and eh_animal(a2) and a1 == a2


# Transformadores

def animal_para_char(animal):
    if eh_predador(animal):
        return str((animal[0])[0]).upper()
    return str((animal[0])[0])


def animal_para_str(animal):
    if eh_predador(animal):
        return str(animal[0]) + f" [{animal[1]}/{animal[2]};{animal[3]}/{animal[4]}]"
    return str(animal[0]) + f" [{animal[1]}/{animal[2]}]"


# Funções de alto nível

def eh_animal_fertil(animal):
    if animal[1] >= animal[2]:
        return True
    return False


def eh_animal_faminto(animal):
    if eh_predador(animal) and animal[3] >= animal[4]:
        return True
    return False


def reproduz_animal(animal):
    reset_idade(animal)
    novo_animal = cria_copia_animal(animal)

    if eh_predador(novo_animal):
        reset_fome(novo_animal)
    return novo_animal


# TAD Prado
# Construtor

def cria_prado(d, r, a, p):
    if not (eh_posicao(d) and isinstance(r, tuple) and (not r or all(eh_posicao(rochedo) for rochedo in r)) and
            all((0 < pos[0] < d[0] and 0 < pos[1] < d[1]) for pos in r) and isinstance(a, tuple) and
            all(eh_animal(animal) for animal in a) and isinstance(p, tuple) and len(p) == len(a) and
            all(eh_posicao(pos) for pos in p) and all((0 < pos[0] < d[0] and 0 < pos[1] < d[1]) for pos in p)
            and all(pos not in r for pos in p)):
        raise ValueError('cria_prado: argumentos invalidos')

    prado = {}

    def primeira_ultima_linhas():
        prado[0] = '+'

        for x1 in range(1, d[0]):
            prado[x1] = '-'

        prado[d[0]] = '+'
        indice_aux = (2 * d[0]) + 1

        for y1 in range(1, d[1]):
            prado[(d[0] + 1) * y1] = '|'
            prado[indice_aux] = '|'
            indice_aux += d[0] + 1

        prado[(d[0] + 1) * d[1]] = '+'

        for x1 in range(1, d[0]):
            prado[(d[0] + 1) * d[1] + x1] = '-'

        prado[(d[0] + 1) * d[1] + d[0]] = '+'

        return prado

    prado = primeira_ultima_linhas()

    for y in range(1, d[1]):
        for x in range(1, d[0]):
            prado[(d[0] + 1) * y + x] = '.'

    for rochedo in r:
        prado[rochedo[1] * (d[0] + 1) + rochedo[0]] = '@'

    cont = 0

    for animal in a:
        prado[(p[cont])[1] * (d[0] + 1) + (p[cont])[0]] = animal
        cont += 1

    prado = {k: v for k, v in sorted(prado.items())}

    return prado


def cria_copia_prado(prado):
    if not eh_prado(prado):
        raise ValueError('cria_copia_prado: argumento invalido')

    copia_prado = dict(prado)

    return copia_prado


# Seletores

def obter_tamanho_x(prado):
    cantos = [item for item in list(prado.items()) if item[1] == '+']
    return cantos[1][0] + 1


def obter_tamanho_y(prado):
    cantos = [item for item in list(prado.items()) if item[1] == '+']
    return cantos[2][0] // obter_tamanho_x(prado) + 1


def obter_numero_predadores(prado):
    numero_predadores = [item for item in list(prado.values()) if len(item) == 5]

    return len(numero_predadores)


def obter_numero_presas(prado):
    numero_presas = [item for item in list(prado.values()) if len(item) == 3]

    return len(numero_presas)


def obter_posicao_animais(prado):
    posicao_animais = tuple([obter_posicao(prado, key) for key in list(prado.keys()) if
                             isinstance(prado[key], list)])
    return posicao_animais


def obter_animal(prado, posicao):
    return prado[obter_valor_numerico(prado, posicao)]


# Modificadores

def eliminar_animal(prado, posicao):
    prado[obter_valor_numerico(prado, posicao)] = '.'

    return prado


def mover_animal(prado, posicao1, posicao2):
    animal = obter_animal(prado, posicao1)
    prado[obter_valor_numerico(prado, posicao1)] = '.'

    return inserir_animal(prado, animal, posicao2)


def inserir_animal(prado, animal, posicao):
    prado[obter_valor_numerico(prado, posicao)] = animal

    return prado


# Reconhecedores

def eh_prado(prado):

    nx = obter_tamanho_x(prado)
    ny = obter_tamanho_y(prado)

    def eh_prado_aux(p):
        indice_aux = (2 * (nx - 1)) + 1

        for y1 in range(1, ny - 1):
            if p[nx * y1] != '|' or p[indice_aux] != '|':
                return False
            indice_aux += nx
        return True

    if prado[0] == '+' and all(prado[cont] == '-' for cont in range(1, nx - 1)) and prado[nx - 1] == '+' and \
            prado[nx * (ny - 1)] == '+' and all(prado[nx * (ny - 1) + cont] == '-' for cont in range(1, nx - 1)) and \
            prado[nx * (ny - 1) + nx - 1] == '+' and eh_prado_aux(prado):
                    return True

    return False


def eh_posicao_animal(prado, posicao):
    if posicao in obter_posicao_animais(prado):
        return True
    return False


def eh_posicao_obstaculo(prado, posicao):
    if prado[obter_valor_numerico(prado, posicao)] in ['@', '+', '-', '|']:
        return True
    return False


def eh_posicao_livre(prado, posicao):
    if prado[obter_valor_numerico(prado, posicao)] == '.':
        return True
    return False


# Teste

def prados_iguais(prado1, prado2):
    return eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2


# Transformador

def prado_para_str(prado):
    nx = obter_tamanho_x(prado)
    ny = obter_tamanho_y(prado)
    cadeia_caracteres = f"+{'-' * (nx - 2)}+\n"

    for y in range(1, ny - 1):
        cadeia_caracteres += '|'
        for x in range(1, nx - 1):
            if not eh_animal(prado[nx * y + x]):
                cadeia_caracteres += prado[nx * y + x]
            else:
                cadeia_caracteres += animal_para_char(prado[nx * y + x])

        cadeia_caracteres += '|\n'

    cadeia_caracteres += f"+{'-' * (nx - 2)}+"

    return cadeia_caracteres


# Funções de alto nível

def obter_valor_numerico(prado, posicao):
    nx = obter_tamanho_x(prado)

    return nx * posicao[1] + posicao[0]


def obter_posicao(prado, valor_numerico):
    nx = obter_tamanho_x(prado)

    return cria_posicao(valor_numerico % nx, valor_numerico // nx)


def obter_movimento(prado, posicao):
    animal = obter_animal(prado, posicao)
    posicoes_adjacentes = [adj for adj in obter_posicoes_adjacentes(posicao) if
                           obter_valor_numerico(prado, adj) in list(prado.keys()) and
                           eh_posicao_livre(prado, adj)]

    if eh_predador(animal):
        presas = [adj for adj in obter_posicoes_adjacentes(posicao) if
                  obter_valor_numerico(prado, adj) in list(prado.keys()) and
                  eh_presa(obter_animal(prado, adj))]
        if len(presas) >= 1:
            return presas[0]

    p = len(posicoes_adjacentes)
    n = obter_valor_numerico(prado, posicao)

    if p >= 1:
        return posicoes_adjacentes[n % p]
    return posicao


# Funções adicionais

def geracao(prado):
    ja_movimentado = []

    for key, value in prado.items():
        if eh_animal(value) and key not in ja_movimentado:
            if eh_predador(value):
                value = aumenta_fome(value)

            value = aumenta_idade(value)
            posicao_inicial = obter_posicao(prado, key)
            nova_posicao = obter_movimento(prado, posicao_inicial)

            if eh_presa(obter_animal(prado, nova_posicao)) and nova_posicao != posicao_inicial:
                value = reset_fome(value)

            nova_key = obter_valor_numerico(prado, nova_posicao)
            ja_movimentado.append(nova_key)

            if eh_animal_fertil(value) and nova_posicao != posicao_inicial:
                value = reset_idade(value)
                prado = mover_animal(prado, posicao_inicial, nova_posicao)
                prado = inserir_animal(prado, reproduz_animal(value), posicao_inicial)
            else:
                prado = mover_animal(prado, posicao_inicial, nova_posicao)

            if eh_animal_faminto(prado[nova_key]):
                prado = eliminar_animal(prado, nova_posicao)

    return prado


def simula_ecossistema(f, num_geracoes, verboso):
    ficheiro = open(f, 'r')
    num_animais = len(ficheiro.readlines()) - 2

    ficheiro.seek(0)
    d = list(eval(ficheiro.readline()))
    temp_r = eval(ficheiro.readline())
    r = []

    for posicao in temp_r:
        r.append(list(posicao))

    r = tuple(r)
    a = []
    temp_p = ()
    p = []

    for cont in range(0, num_animais):
        copia_p = tuple(temp_p)

        if cont != num_animais - 1:
            line = eval((ficheiro.readline())[:-1])
        else:
            line = eval(((ficheiro.readline())[:-1]) + ')')

        animal = cria_animal(line[0], line[1], line[2])
        a.append(animal)
        temp_p = copia_p + (line[3],)

    a = tuple(a)

    for posicao in temp_p:
        p.append(list(posicao))

    p = tuple(p)
    print(d)
    print(r)
    print(a)
    print(p)
    prado = cria_prado(d, r, a, p)

    print(f'Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. 0)')
    print(prado_para_str(prado))

    for cont in range(1, num_geracoes + 1):
        num_predadores_anterior = obter_numero_predadores(prado)
        num_presas_anterior = obter_numero_presas(prado)
        prado = geracao(prado)

        if (verboso and (obter_numero_predadores(prado) != num_predadores_anterior or
                         obter_numero_presas(prado) != num_presas_anterior)) or (not verboso and cont == num_geracoes):
            print(f'Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {cont})')
            print(prado_para_str(prado))

    return tuple((obter_numero_predadores(prado), obter_numero_presas(prado)))
