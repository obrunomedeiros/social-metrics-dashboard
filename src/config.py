import os

class Config:
    """
    Cofre de credenciais seguro baseado em Variáveis de Ambiente do Sistema.
    """
    DATABASE_URL = os.getenv("DATABASE_URL")

    @classmethod
    def validate(cls):
        """Valida se a string de conexão do banco está presente no cofre."""
        if not cls.DATABASE_URL:
            raise ValueError(
                "[ERRO DE SEGURANÇA] A variável 'DATABASE_URL' não foi encontrada no ambiente. "
                "Execute 'source load_env.sh' antes de rodar o pipeline."
            )
        print("-> [COFRE] String de conexão do PostgreSQL validada com sucesso!")