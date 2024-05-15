from datetime import datetime

def formatar_data(data_str):
    # Converte a string de data para um objeto datetime
    data = datetime.strptime(data_str, '%d/%m/%Y')
    # Formata a data como uma string no formato YYYY-MM-DD
    return data.strftime('%Y-%m-%d')