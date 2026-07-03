import pandas as pd

def carregar_dados(caminho_arquivo):
  try:
    df = pd.read_csv(caminho_arquivo)
  except Exception as e:
    raise ValueError(f'Não foi possível carregar os dados: {e}')

  if df.empty:
    raise ValueError('O arquivo carregado está vazio')
  
  return df
