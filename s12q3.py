from operator import itemgetter


def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()  # Descarta a primeira linha (cabeçalho do arquivo)
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'

def media_volume(empresa):
    soma = cont = 0
    mes = int(input())
    ano = int(input())
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes'), reverse=True)
    for i in ordenado:
        if i['mes'] == mes:
            if i['ano'] == ano:
                soma += i['volume']
                cont += 1
    media = soma/cont
    return f'O volume médio em {mes}/{ano} foi {media:.0f}'


def main():
    # Carregar os dados da empresa a partir do arquivo csv
    nome_arquivo = str(input()).strip()
    arquivo = carregar(nome_arquivo)
 
    # Qual o maior volume diário negociado e em que data ocorreu.
    mv = media_volume(arquivo)
    print(mv)

if __name__ == '__main__':
    main()