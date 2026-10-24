from src.config import Config
from src.extract import extrair_dados_instagram
from src.transform import transformar_metricas
from src.load import salvar_metricas_upsert

def main():
    print("=== Iniciando Pipeline de Métricas de Redes Sociais ===")
    
    # 1. Validação de segurança das credenciais
    Config.validate()
    
    try:
        # 2. Extract: Coleta os dados brutos da API
        df_raw = extrair_dados_instagram()
        
        # 3. Transform: Limpa, trata nulos e padroniza os dados
        df_clean = transformar_metricas(df_raw)
        
        # 4. Load: Salva de forma idempotente (Upsert) no Supabase
        salvar_metricas_upsert(df_clean)
        
        print("=== Pipeline executado com sucesso! ===")
    except Exception as e:
        print(f"[ERRO NO PIPELINE]: {e}")
        exit(1)

if __name__ == "__main__":
    main()