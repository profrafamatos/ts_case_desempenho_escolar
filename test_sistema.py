import pytest
import pandas as pd
import kagglehub
import os
from sistema import carregar_dados

CAMINHO_DATASET = kagglehub.dataset_download("spscientist/students-performance-in-exams")
CAMINHO_CSV_VALIDO = os.path.join(CAMINHO_DATASET, "StudentsPerformance.csv")

def test_carregar_dados_retorna_dataframe():
    df = carregar_dados(CAMINHO_CSV_VALIDO)
    assert isinstance(df, pd.DataFrame)

def test_carregar_dados_nao_esta_vazio():
    df = carregar_dados(CAMINHO_CSV_VALIDO)
    assert len(df) > 0

def test_carregar_dados_colunas_esperadas():
    df = carregar_dados(CAMINHO_CSV_VALIDO)
    colunas_esperadas = {"math score", "reading score", "writing score"}
    assert colunas_esperadas.issubset(set(df.columns))

def test_carregar_dados_caminho_invalido_gera_erro():
    with pytest.raises(ValueError):
        carregar_dados("caminho/que/nao/existe.csv")
