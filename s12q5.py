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


# Realiza o preço médio do arquivo de acordo com o mês e o ano informado.
def dados(empresa):
    mes = int(input())
    ano = int(input())
    print(f'Dias de {mes}/{ano} que houve queda no preço da ação:')
    ordenado = sorted(empresa, key=itemgetter('ano', 'mes', 'dia'))
    for i in ordenado:
        if i['mes'] == mes:
            if i['ano'] == ano:
                if i['abertura'] > i['fechamento']:
                    d = i['dia']
                    v = round(i['abertura'] - i['fechamento'], 2)
                    print(f"('{i['dia']:02d}/{i['mes']:02d}/{i['ano']}', {i['abertura']}, {i['fechamento']}, {v})")


def main():
    # Carregar os dados da empresa a partir do arquivo csv
    nome_arquivo = str(input()).strip()
    arquivo = carregar(nome_arquivo)

    dados(arquivo)
    



if __name__ == '__main__':
    main()