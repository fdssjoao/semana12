from operator import itemgetter


def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()  # Descarta a primeira linha (cabeçalho do arquivo)
        for linha in f.readlines():
            data, abertura,_ ,_ , _, _ = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
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


def maior_preco(empresa):
    ordenado = sorted(empresa, key=itemgetter('abertura'))
    return ordenado[-1]['abertura'], formatar_data(ordenado[-1])


def main():
    # Carregar os dados da empresa a partir do arquivo csv
    nome = str(input())
    arquivo = carregar(nome)

    maior, data = maior_preco(arquivo)
    print(f'O maior preço na abertura foi {maior:.2f} em {data}')
    
    

if __name__ == '__main__':
    main()