"""Regressões do perfil pessoal de vagas iOS."""

import pytest

from core.job import Job
from core.perfis import PERFIL_IOS, PERFIL_IOS_INTL


def _vaga(titulo, local, modalidade):
    return Job(
        titulo=titulo,
        empresa="Empresa Teste",
        local=local,
        link=f"https://exemplo.com/{abs(hash((titulo, local, modalidade)))}",
        site="Teste",
        modalidade=modalidade,
    )


@pytest.mark.parametrize("cidade", ["Manaus", "Recife", "Rio de Janeiro"])
@pytest.mark.parametrize("modalidade", ["Presencial", "Híbrido"])
def test_ios_aceita_presencial_e_hibrido_nas_cidades_prioritarias(cidade, modalidade):
    assert _vaga("iOS Developer Pleno", cidade, modalidade).combina_com(PERFIL_IOS.regras)


@pytest.mark.parametrize("local", [
    "Remoto",
    "Remote - Brazil",
    "Remoto (São Paulo, SP)",
    "Home Office",
])
def test_ios_aceita_remoto_em_todo_o_brasil(local):
    assert _vaga("Swift Developer", local, "Remoto").combina_com(PERFIL_IOS.regras)


@pytest.mark.parametrize("local", ["São Paulo - SP", "Belo Horizonte - MG", "Salvador - BA"])
def test_ios_rejeita_presencial_fora_das_cidades_prioritarias(local):
    assert not _vaga("iOS Developer", local, "Presencial").combina_com(PERFIL_IOS.regras)


@pytest.mark.parametrize("titulo", [
    "iOS Developer",
    "Desenvolvedor Swift",
    "Mobile Engineer",
    "Software Engineer - SwiftUI",
])
def test_ios_reconhece_titulos_e_stack(titulo):
    assert _vaga(titulo, "Manaus - AM", "Híbrido").combina_com(PERFIL_IOS.regras)


def test_ios_rejeita_vaga_sem_relacao_com_mobile():
    assert not _vaga("Backend Developer - Python", "Manaus - AM", "Presencial").combina_com(PERFIL_IOS.regras)


@pytest.mark.parametrize("local", ["Remote - Portugal", "Remote - Spain", "Remote - LATAM"])
def test_ios_internacional_prioriza_mercados_aceitos(local):
    assert _vaga("iOS Developer", local, "Remoto").combina_com(PERFIL_IOS_INTL.regras)


def test_ios_internacional_rejeita_presencial():
    assert not _vaga("iOS Developer", "Lisboa, Portugal", "Presencial").combina_com(PERFIL_IOS_INTL.regras)

