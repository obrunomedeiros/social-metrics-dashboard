from config.settings import Settings
from src.adapters.simulate.mock_generator import extrair_dados as extrair_mock
# Futuramente: from src.adapters.api_real import extrair_dados as extrair_api

def extrair_dados_redes_sociais():
    """
    Roteador de extração: decide entre mock ou API real baseado no perfis.json.
    """
    if Settings.USAR_MOCK():
        print("-> Modo de Execução: Usando Simulador Local (Mock via Config)")
        return extrair_mock()
    else:
        print("-> Modo de Execução: Conectando às APIs Reais")
        # return extrair_api()
        raise NotImplementedError("APIs reais ainda não foram implementadas.")