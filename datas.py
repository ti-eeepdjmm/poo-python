from datetime import datetime

def data_atual():
    data_atual = datetime.now()
    data_texto = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    return data_texto