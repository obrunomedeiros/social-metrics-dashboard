import json
import os

class Settings:
    """
    Centraliza a leitura das configurações do projeto a partir do arquivo settings.json.
    """
    _config_cache = None

    @classmethod
    def _carregar_json(cls):
        if cls._config_cache is None:
            # Caminho absoluto para a pasta config/settings.json
            caminho_config = os.path.join(os.path.dirname(__file__), "settings.json")
            
            if not os.path.exists(caminho_config):
                raise FileNotFoundError(f"Arquivo de configuração não encontrado em: {caminho_config}")
                
            with open(caminho_config, "r", encoding="utf-8") as f:
                cls._config_cache = json.load(f)
                
        return cls._config_cache

    @classmethod
    def USAR_MOCK(cls) -> bool:
        """Retorna se o sistema deve usar dados simulados (True) ou APIs reais (False)."""
        return cls._carregar_json().get("use_mock", True)

    @classmethod
    def obter_perfis(cls) -> list:
        """Retorna a lista completa de perfis configurados."""
        return cls._carregar_json().get("perfis", [])