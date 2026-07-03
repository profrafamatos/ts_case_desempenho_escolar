import pytest
from unittest.mock import patch
import pandas as pd
import kagglehub
import os
from sistema import carregar_dados, calcular_media_aluno, classificar_aprovacao

CAMINHO_DATASET = kagglehub.dataset_download("spscientist/students-performance-in-exams")
CAMINHO_CSV_VALIDO = os.path.join(CAMINHO_DATASET, "StudentsPerformance.csv")

# ---------- Fixture ----------
@pytest.fixture
def aluno_exemplo():
    """Simula as notas de um aluno para reaproveitar em vários testes."""
    return {"math": 70, "reading": 80, "writing": 90}


# ---------- Testes de carregar_dados (Aula 2) ----------
def test_carregar_dados_retorna_dataframe():
    df = carregar_dados(CAMINHO_CSV_VALIDO)
    assert isinstance(df, pd.DataFrame)

def test_carregar_dados_caminho_invalido_gera_erro():
    with pytest.raises(ValueError):
        carregar_dados("caminho/que/nao/existe.csv")


# ---------- Testes de calcular_media_aluno (Aula 3) ----------
def test_calcular_media_aluno_com_fixture(aluno_exemplo):
    media = calcular_media_aluno(
        aluno_exemplo["math"], aluno_exemplo["reading"], aluno_exemplo["writing"]
    )
    assert media == 80.0

def test_calcular_media_aluno_nota_invalida_gera_erro():
    with pytest.raises(ValueError):
        calcular_media_aluno(150, 80, 90)

def test_calcular_media_aluno_nota_negativa_gera_erro():
    with pytest.raises(ValueError):
        calcular_media_aluno(-10, 80, 90)


# ---------- Testes de classificar_aprovacao (Aula 3) ----------
def test_classificar_aprovacao_aprovado():
    assert classificar_aprovacao(75) == "Aprovado"

def test_classificar_aprovacao_reprovado():
    assert classificar_aprovacao(45) == "Reprovado"

def test_classificar_aprovacao_no_limite():
    assert classificar_aprovacao(60) == "Aprovado"  # valor de fronteira


# ---------- Exemplo de MOCK ----------
def test_carregar_dados_usa_mock_sem_acessar_internet():
    """
    Mostra como usar mock para simular a leitura do CSV,
    sem depender de internet, do Kaggle ou do GitHub estarem no ar.
    """
    dados_falsos = pd.DataFrame({
        "math score": [70],
        "reading score": [80],
        "writing score": [90],
    })

    with patch("pandas.read_csv", return_value=dados_falsos):
        df = carregar_dados("qualquer_caminho.csv")
        assert len(df) == 1
        assert df["math score"].iloc[0] == 70
