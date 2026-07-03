import pandas as pd

def carregar_dados(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
    except Exception as e:
        raise ValueError(f"Não foi possível carregar os dados: {e}")

    if df.empty:
        raise ValueError("O arquivo carregado está vazio.")

    return df

def calcular_media_aluno(nota_math, nota_reading, nota_writing):
  notas = [nota_math, nota_reading, nota_writing]

  for nota in notas:
    if not (0 <= nota <= 100):
      raise ValueError(f'Nota inválida: {nota}. Deve estar entre 0 e 100.')

    return sum(notas)/len(notas)

def classificar_aprovacao(media, nota_minima = 60):
  if not(0 <= media <= 100):
    raise ValueError(f'Média inválida: {media}')
  
  return "Aprovado" if media >= nota_minima else "Reprovado"
