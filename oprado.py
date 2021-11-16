# TAD posicao
# Construtor

def cria_posicao(x, y):
    """
    Recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente
    :param x: (int) coordenada x
    :param y: (int) coordenada y
    :return posicao: (posicao) posição
    """
    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        raise ValueError('cria_posicao: argumentos invalidos')

    posicao = [x, y]

    return posicao


def cria_copia_posicao(posicao):
    """
    Recebe uma posição e devolve uma cópia da mesma
    :param posicao: (posicao) posição a ser copiada
    :return copia_posicao: (posicao) cópia da posição
    """
    if not eh_posicao(posicao):
        raise ValueError('cria_copia_posicao: argumento invalido')

    copia_posicao = list(posicao)

    return copia_posicao


# Seletores

def obter_pos_x(posicao):
    """
    Obtém a coordenada x de uma posição
    :param posicao: (posicao) posição
    :return: (int) coordenada x da posição dada como argumento
    """
    return posicao[0]


def obter_pos_y(posicao):
    """
    Obtém a coordenada y de uma posição
    :param posicao: (posicao) posição
    :return: (int) coordenada y da posição dada como argumento
    """
    return posicao[1]


# Reconhecedor

def eh_posicao(posicao):
    """
    Verifica se o argumento é um TAD posição
    :param posicao: (list) argumento a ser verificado
    :return: (bool) True se for um TAD posição, False se não.
    """
    if not (isinstance(posicao, list) and all(isinstance(axis, int) for axis in posicao) and
            len(posicao) == 2 and posicao[0] >= 0 and posicao[1] >= 0):
        return False
    return True


# Teste

def posicoes_iguais(pos1, pos2):
    """
    Verifica se duas posições são iguais
    :param pos1: (posicao) primeira posição
    :param pos2: (posicao) segunda posição
    :return: (bool) True se forem posições iguais, False se não
    """
    return eh_posicao(pos1) and eh_posicao(pos2) and pos1 == pos2


# Transformador

def posicao_para_str(posicao):
    """
    Recebe uma posição e devolve a mesma em forma de string
    :param posicao: (posicao) posição
    :return: (str) posição em forma de string
    """
    return f"({obter_pos_x(posicao)}, {obter_pos_y(posicao)})"


# Funções de alto nível

def obter_posicoes_adjacentes(posicao):
    """
    Obtém as posições adjacentes à posição dada como argumento
    :param posicao: (posicao) posição
    :return: (tuple) posições adjacentes à posição dada como argumento
    """
    posicoes_adjacentes = []

    if eh_posicao([obter_pos_x(posicao), obter_pos_y(posicao) - 1]):
        posicoes_adjacentes.append(cria_posicao(obter_pos_x(posicao), obter_pos_y(posicao) - 1))

    if eh_posicao([obter_pos_x(posicao) + 1, obter_pos_y(posicao)]):
        posicoes_adjacentes.append(cria_posicao(obter_pos_x(posicao) + 1, obter_pos_y(posicao)))

    if eh_posicao([obter_pos_x(posicao), obter_pos_y(posicao) + 1]):
        posicoes_adjacentes.append(cria_posicao(obter_pos_x(posicao), obter_pos_y(posicao) + 1))

    if eh_posicao([obter_pos_x(posicao) - 1, obter_pos_y(posicao)]):
        posicoes_adjacentes.append(cria_posicao(obter_pos_x(posicao) - 1, obter_pos_y(posicao)))

    return tuple(posicoes_adjacentes)


def ordenar_posicoes(posicoes):
    """
    Ordena as posições dadas de acordo com o enunciado
    :param posicoes: (tuple) posições a serem ordenadas
    :return: (tuple) posições ordenadas
    """
    posicoes = sorted(posicoes, key=lambda x: (obter_pos_y(x), obter_pos_x(x)))
    return posicoes


# TAD Animal
# Presa (espécie, idade, frequência de reprodução)
# Predador (espécie, idade, frequência de reprodução, fome, frequência de alimentação)
# Construtor

def cria_animal(s, r, a):
    """
    Recebe a espécie, frequência de reprodução e frequência de alimentação de um animal e devolve o animal
    :param s: (str) espécie
    :param r: (int) frequência de reprodução
    :param a: (int) frequência de alimentação
    :return: (animal) animal
    """
    if not (isinstance(s, str) and s and isinstance(r, int) and r > 0 and isinstance(a, int) and a >= 0):
        raise ValueError('cria_animal: argumentos invalidos')

    if a == 0:
        animal = [s, 0, r]
    else:
        animal = [s, 0, r, 0, a]

    return animal


def cria_copia_animal(animal):
    """
    Recebe um animal e devolve uma cópia do mesmo
    :param animal: (animal) animal a ser copiado
    :return: (animal) cópia do animal
    """
    if not eh_animal(animal):
        raise ValueError('cria_copia_animal: argumento invalido')

    copia_animal = list(animal)

    return copia_animal


# Seletores

def obter_especie(animal):
    """
    Obtém a espécie de um animal
    :param animal: (animal) animal
    :return: (str) espécie
    """
    return animal[0]


def obter_freq_reproducao(animal):
    """
    Obtém a frequência de reprodução de um animal
    :param animal: (animal) animal
    :return: (int) frequência de reprodução
    """
    return animal[2]


def obter_freq_alimentacao(animal):
    """
    Obtém a frequência de alimentação de um animal
    :param animal: (animal) animal
    :return: (int) frequência de alimentação
    """
    if len(animal) == 5:
        return animal[4]
    return 0


def obter_idade(animal):
    """
    Obtém a idade de um animal
    :param animal: (animal) animal
    :return: (int) idade
    """
    return animal[1]


def obter_fome(animal):
    """
    Obtém a fome de um animal
    :param animal: (animal) animal
    :return: (int) fome
    """
    if len(animal) == 5:
        return animal[3]
    return 0


# Modificadores

def aumenta_idade(animal):
    """
    Aumenta a idade de um animal
    :param animal: (animal) animal
    :return: (animal) animal
    """
    animal[1] += 1

    return animal


def reset_idade(animal):
    """
    Modifica a idade de um animal para 0
    :param animal: (animal) animal
    :return: (animal) animal
    """
    animal[1] = 0

    return animal


def aumenta_fome(animal):
    """
    Aumenta a fome de um animal
    :param animal: (animal) animal
    :return: (animal) animal
    """
    if eh_predador(animal):
        animal[3] += 1

    return animal


def reset_fome(animal):
    """
    Modifica a fome de um animal para 0
    :param animal: (animal) animal
    :return: (animal) animal
    """
    if eh_predador(animal):
        animal[3] = 0

    return animal


# Reconhecedor
# Se se verificarem os requisitos comuns e um dos requisitos de presa ou predador, é um TAD animal

def eh_animal(animal):
    """
    Verifica se o argumento é um TAD animal
    :param animal: (universal) argumento a ser verificado
    :return: (bool) True se for um TAD animal, False se não
    """
    def requisitos_comuns(animal_aux):
        """
        Verifica os requisitos comuns a todos os animais
        :param animal_aux: (universal) argumento a ser verificado
        :return: (bool) True se se verificarem os requisitos comuns a todos os animais, False se não
        """
        if isinstance(animal_aux, list) and isinstance(animal_aux[0], str) and \
                animal_aux[0] and isinstance(animal_aux[1], int) and animal_aux[1] >= 0 and \
                isinstance(animal_aux[2], int) and animal_aux[2] > 0:
            return True
        return False

    def requisitos_presa(animal_aux):
        """
        Verifica os requisitos comuns a presas
        :param animal_aux: (universal) argumento a ser verificado
        :return: True se se verificarem os requisitos comuns a presas, False se não
        """
        if requisitos_comuns(animal_aux) and len(animal_aux) == 3:
            return True
        return False

    def requisitos_predador(animal_aux):
        """
        Verifica os requisitos comuns a predadores
        :param animal_aux: (universal) argumento a ser verificado
        :return: True se se verificarem os requisitos comuns a predadores, False se não
        """
        if requisitos_comuns(animal_aux) and isinstance(animal_aux[3], int) and \
                animal_aux[3] >= 0 and isinstance(animal_aux[4], int) and animal_aux[4] > 0 and animal[3] <= animal[4] \
                and len(animal_aux) == 5:
            return True
        return False

    if requisitos_presa(animal) or requisitos_predador(animal):
        return True
    return False


def eh_predador(animal):
    """
    Verifica se o argumento é um TAD animal do tipo predador
    :param animal: (universal) argumento a ser verificado
    :return: (bool) True se for um predador, False se não
    """
    if eh_animal(animal) and len(animal) == 5:
        return True
    return False


def eh_presa(animal):
    """
    Verifica se o argumento é um TAD animal do tipo presa
    :param animal: (universal) argumento a ser verificado
    :return: (bool) True se for uma presa, False se não
    """
    if eh_animal(animal) and len(animal) == 3:
        return True
    return False


# Teste

def animais_iguais(a1, a2):
    """
    Verifica se dois animais são iguais
    :param a1: (animal) primeiro animal
    :param a2: (animal) segundo animal
    :return: (bool9 True se forem iguais, False se não
    """
    return eh_animal(a1) and eh_animal(a2) and a1 == a2


# Transformadores

def animal_para_char(animal):
    """
    Recebe um animal e devolve o mesmo na forma de um caracter
    :param animal: (animal) animal
    :return: (str) animal na forma de caracter
    """
    if eh_predador(animal):
        return obter_especie(animal)[0].upper()
    return obter_especie(animal)[0].lower()


def animal_para_str(animal):
    """
    Recebe um animal e devolve o mesmo na forma de uma string
    :param animal: (animal) animal
    :return: (str) animal na forma de string
    """
    if eh_predador(animal):
        return obter_especie(animal) + f" [{obter_idade(animal)}/{obter_freq_reproducao(animal)};" \
                                       f"{obter_fome(animal)}/{obter_freq_alimentacao(animal)}]"
    return obter_especie(animal) + f" [{obter_idade(animal)}/{obter_freq_reproducao(animal)}]"


# Funções de alto nível

def eh_animal_fertil(animal):
    """
    Verifica se um animal é fértil
    :param animal: (animal) animal
    :return: (bool) True se for fértil, False se não
    """
    if obter_idade(animal) >= obter_freq_reproducao(animal):
        return True
    return False


def eh_animal_faminto(animal):
    """
    Verifica se um animal está faminto
    :param animal: (animal) animal
    :return: (bool) True se estiver faminto, False se não
    """
    if eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal):
        return True
    return False


def reproduz_animal(animal):
    """
    Recebe um animal e devolve um novo animal, semelhante ao primeiro mas com idade (e fome, se for predador) igual a zero
    :param animal: (animal) animal
    :return: (animal) novo animal
    """
    reset_idade(animal)
    novo_animal = cria_copia_animal(animal)

    if eh_predador(novo_animal):
        reset_fome(novo_animal)
    return novo_animal


# TAD Prado
# Construtor

def cria_prado(d, r, a, p):
    """
    Recebe o canto inferior direito, a posição dos rochedos, os animais, e as posições dos animais de um prado e devolve o prado
    :param d: (posicao) canto inferior direito do prado
    :param r: (tuple) tuplo com as posições dos rochedos do prado
    :param a: (tuple) tuplo com os animais do prado
    :param p: (tuple) tuplo com as posições dos animais do prado
    :return: (prado) prado
    """
    if not (eh_posicao(d) and isinstance(r, tuple) and (not r or all(eh_posicao(rochedo) for rochedo in r)) and
            all((0 < pos[0] < d[0] and 0 < pos[1] < d[1]) for pos in r) and isinstance(a, tuple) and
            all(eh_animal(animal) for animal in a) and isinstance(p, tuple) and len(p) == len(a) and
            all(eh_posicao(pos) for pos in p) and all((0 < pos[0] < d[0] and 0 < pos[1] < d[1]) for pos in p)
            and all(pos not in r for pos in p)):
        raise ValueError('cria_prado: argumentos invalidos')

    prado = {}

    def primeira_ultima_linhas():
        """
        Cria as primeira e última linhas do prado
        :return: (prado) prado
        """
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
    """
    Recebe um prado e devolve uma cópia do mesmo
    :param prado: (prado) prado a ser copiado
    :return: (prado) cópia do prado
    """
    if not eh_prado(prado):
        raise ValueError('cria_copia_prado: argumento invalido')

    copia_prado = dict(prado)

    return copia_prado


# Seletores

def obter_tamanho_x(prado):
    """
    Obtém a dimensão Nx do prado
    :param prado: (prado) prado
    :return: (int) dimensão Nx do prado
    """
    cantos = [item for item in list(prado.items()) if item[1] == '+']
    return cantos[1][0] + 1


def obter_tamanho_y(prado):
    """
    Obtém a dimensão Ny do prado
    :param prado: (prado) prado
    :return: (int) dimensão Ny do prado
    """
    cantos = [item for item in list(prado.items()) if item[1] == '+']
    return cantos[2][0] // obter_tamanho_x(prado) + 1


def obter_numero_predadores(prado):
    """
    Obtém o número de predadores do prado
    :param prado: (prado) prado
    :return: (int) número de predadores do prado
    """
    numero_predadores = [item for item in list(prado.values()) if len(item) == 5]

    return len(numero_predadores)


def obter_numero_presas(prado):
    """
    Obtém o número de presas do prado
    :param prado: (prado) prado
    :return: (int) número de presas do prado
    """
    numero_presas = [item for item in list(prado.values()) if len(item) == 3]

    return len(numero_presas)


def obter_posicao_animais(prado):
    """
    Obtém as posições dos animais do prado
    :param prado: (prado) prado
    :return: (tuple) tuplo com as posições dos animais do prado
    """
    posicao_animais = tuple([obter_posicao(prado, key) for key in list(prado.keys()) if
                             isinstance(prado[key], list)])
    return posicao_animais


def obter_posicao_rochedos(prado):
    """
    Obtém as posições dos rochedos do prado
    :param prado: (prado) prado
    :return: (tuple) tuplo com as posições dos rochedos do prado
    """
    posicao_rochedos = tuple([obter_posicao(prado, key) for key in list(prado.keys()) if prado[key] == '@'])
    return posicao_rochedos


def obter_animal(prado, posicao):
    """
    Obtém o animal que se encontra na posição do prado dada como argumento
    :param prado: (prado) prado
    :param posicao: (posicao) posicao
    :return: (animal) animal que se encontra na posição dada como argumento
    """
    return prado[obter_valor_numerico(prado, posicao)]


# Modificadores

def eliminar_animal(prado, posicao):
    """
    Remove do prado o animal que se encontra na posição dada como argumento
    :param prado: (prado) prado
    :param posicao: (posicao) posicao
    :return: (prado) prado atualizado
    """
    prado[obter_valor_numerico(prado, posicao)] = '.'

    return prado


def mover_animal(prado, posicao1, posicao2):
    """
    Move um animal de uma posicao do prado para outra
    :param prado: (prado) prado
    :param posicao1: (posicao) posição inicial
    :param posicao2: (posicao) posição final
    :return: (prado) prado atualizado
    """
    animal = obter_animal(prado, posicao1)
    prado[obter_valor_numerico(prado, posicao1)] = '.'

    return inserir_animal(prado, animal, posicao2)


def inserir_animal(prado, animal, posicao):
    """
    Insere o animal dado como argumento na posição do prado dada como argumento
    :param prado: (prado) prado
    :param animal: (animal) animal
    :param posicao: (posicao) posição
    :return: (prado) prado atualizado
    """
    prado[obter_valor_numerico(prado, posicao)] = animal

    return prado


# Reconhecedores

def eh_prado(prado):
    """
    Verifica se  argumento é um TAD prado
    :param prado: (universal) argumento a ser verificado
    :return: (bool) True se for um TAD prado, False se não
    """
    d = cria_posicao(obter_tamanho_x(prado), obter_tamanho_y(prado))
    r = obter_posicao_rochedos(prado)
    p = obter_posicao_animais(prado)
    a = tuple(obter_animal(prado, pos) for pos in p)

    try:
        cria_prado(d, r, a, p)
    except ValueError:
        return False
    return True


def eh_posicao_animal(prado, posicao):
    """
    Verifica se um animal se encontra na posição dada como argumento
    :param prado: (prado) prado
    :param posicao: (posicao) posição
    :return: (bool) True se for a posição de um animal, False se não
    """
    if posicao in obter_posicao_animais(prado):
        return True
    return False


def eh_posicao_obstaculo(prado, posicao):
    """
    Verifica se um obstáculo se encontra na posição dada como argumento
    :param prado: (prado) prado
    :param posicao: (posicao) posição
    :return: (bool) True se for a posição de um obstáculo, False se não
    """
    if obter_animal(prado, posicao) in ['@', '+', '-', '|']:
        return True
    return False


def eh_posicao_livre(prado, posicao):
    """
    Verifica se a posição dada como argumento está livre
    :param prado: (prado) prado
    :param posicao: (posicao) posição
    :return: (bool) True se for uma posição livre, False se não
    """
    if obter_animal(prado, posicao) == '.':
        return True
    return False


# Teste

def prados_iguais(prado1, prado2):
    """
    Verifica se dois prados são iguais
    :param prado1: (prado) primeiro prado
    :param prado2: (prado) segundo prado
    :return: (bool) True se forem prados iguais, False se não
    """
    return eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2


# Transformador

def prado_para_str(prado):
    """
    Recebe um prado e devolve o mesmo na forma de string
    :param prado: (prado) prado
    :return: (string) prado em forma de string
    """
    cadeia_caracteres = ''

    for cont in range(0, len(prado)):
        if eh_animal(obter_animal(prado, obter_posicao(prado, cont))):
            cadeia_caracteres += animal_para_char(obter_animal(prado, obter_posicao(prado, cont)))
        else:
            cadeia_caracteres += obter_animal(prado, obter_posicao(prado, cont))
        if len(prado) - 1 > cont > 0 and (cont + 1) % obter_tamanho_x(prado) == 0:
            cadeia_caracteres += '\n'

    return cadeia_caracteres


# Funções de alto nível

def obter_valor_numerico(prado, posicao):
    """
    Obtém o valor numérico de uma posição do prado
    :param prado: (prado) prado
    :param posicao: (posicao) posição
    :return: (int) valor numérico da posição
    """
    return obter_tamanho_x(prado) * obter_pos_y(posicao) + obter_pos_x(posicao)


def obter_posicao(prado, valor_numerico):
    """
    Obtém a posição do prado a partir de um valor numérico
    :param prado: (prado) prado
    :param valor_numerico: (int) valor numérico
    :return: (posicao) posição
    """
    return cria_posicao(valor_numerico % obter_tamanho_x(prado), valor_numerico // obter_tamanho_x(prado))


def obter_movimento(prado, posicao):
    """
    Obtém o movimento seguinte a partir de uma posição do prado
    :param prado: (prado) prado
    :param posicao: (posicao) posição
    :return: (posicao) posição após o movimento
    """
    if eh_predador(obter_animal(prado, posicao)):
        presas = [adj for adj in obter_posicoes_adjacentes(posicao) if eh_presa(obter_animal(prado, adj))]
        if len(presas) >= 1:
            return presas[0]

    posicoes_adjacentes = [adj for adj in obter_posicoes_adjacentes(posicao) if eh_posicao_livre(prado, adj)]

    if len(posicoes_adjacentes) >= 1:
        return posicoes_adjacentes[obter_valor_numerico(prado, posicao) % len(posicoes_adjacentes)]
    return posicao


# Funções adicionais

def geracao(prado):
    """
    Simula uma geração do prado
    :param prado: (prado) prado
    :return: (prado) prado após uma geração
    """
    ja_movimentado = []

    for cont in range(0, len(prado)):
        if eh_animal(obter_animal(prado, obter_posicao(prado, cont))) and cont not in ja_movimentado:
            if eh_predador(obter_animal(prado, obter_posicao(prado, cont))):
                aumenta_fome(obter_animal(prado, obter_posicao(prado, cont)))

            aumenta_idade(obter_animal(prado, obter_posicao(prado, cont)))
            posicao_inicial = obter_posicao(prado, cont)
            nova_posicao = obter_movimento(prado, posicao_inicial)

            if eh_presa(obter_animal(prado, nova_posicao)) and nova_posicao != posicao_inicial:
                reset_fome(obter_animal(prado, obter_posicao(prado, cont)))

            novo_val_num = obter_valor_numerico(prado, nova_posicao)
            ja_movimentado.append(novo_val_num)

            if eh_animal_fertil(obter_animal(prado, obter_posicao(prado, cont))) and nova_posicao != posicao_inicial:
                reset_idade(obter_animal(prado, obter_posicao(prado, cont)))
                mover_animal(prado, posicao_inicial, nova_posicao)
                inserir_animal(prado, reproduz_animal(obter_animal(prado, nova_posicao)), posicao_inicial)
            else:
                prado = mover_animal(prado, posicao_inicial, nova_posicao)

            if eh_animal_faminto(obter_animal(prado, obter_posicao(prado, novo_val_num))):
                prado = eliminar_animal(prado, nova_posicao)

    return prado


def simula_ecossistema(f, num_geracoes, verboso):
    """
    Simula o ecossistema de um prado
    :param f: (str) nome do ficheiro de configuração da simulação
    :param num_geracoes: (int) número de gerações a ser simulado
    :param verboso: (bool) True para o modo verboso, False para o modo quiet
    :return: (tuple) tuplo com o número de predadores e presas do prado
    """
    ficheiro = open(f, 'r')

    linha1 = eval(ficheiro.readline())
    d = cria_posicao(obter_pos_x(linha1), obter_pos_y(linha1))

    linha2 = eval(ficheiro.readline())
    r = tuple(cria_posicao(obter_pos_x(rochedo), obter_pos_y(rochedo)) for rochedo in linha2)

    animais = ficheiro.readlines()
    for cont in range(0, len(animais)):
        if cont != len(animais) - 1:
            animais[cont] = eval((animais[cont])[:-1])
        else:
            animais[cont] = eval((animais[cont]))

    a = tuple(cria_animal(animal[0], animal[1], animal[2]) for animal in animais)

    posicoes = (animal[3] for animal in animais)
    p = tuple(cria_posicao(obter_pos_x(posicao), obter_pos_y(posicao)) for posicao in posicoes)

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