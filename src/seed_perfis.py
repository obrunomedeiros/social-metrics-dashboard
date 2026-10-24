import os
import pandas as pd
from sqlalchemy import create_engine, text
from src.config import Config

def popular_perfis():
    """
    Insere os perfis reais das redes sociais na tabela dim_perfis do Supabase.
    """
    print("=== Populando Tabela de Dimensão de Perfis (dim_perfis) ===")
    
    # 1. Conecta ao banco de dados utilizando a configuração centralizada
    db_url = Config.DATABASE_URL
    if not db_url:
        raise ValueError("A variável DATABASE_URL não foi encontrada no ambiente.")
    
    engine = create_engine(db_url)
    
    # 2. Defina aqui os seus perfis reais das redes sociais
    # Substitua pelos dados reais das suas marcas e IDs oficiais
    perfis_para_cadastrar = [
        {
            "plataforma": "instagram",
            "nome_perfil": "@sua_marca_oficial",
            "brand_id": "marca_principal"
        },
        {
            "plataforma": "linkedin",
            "nome_perfil": "Sua Empresa S.A.",
            "brand_id": "marca_principal"
        },
        {
            "plataforma": "tiktok",
            "nome_perfil": "@sua_marca_tiktok",
            "brand_id": "marca_principal"
        }
    ]
    
    df_perfis = pd.DataFrame(perfis_para_cadastrar)
    
    print(f"-> Inserindo {len(df_perfis)} perfis no Supabase...")
    
    # 3. Query com verificação para evitar duplicatas caso o script rode mais de uma vez
    query_upsert = text("""
        INSERT INTO dim_perfis (plataforma, nome_perfil, brand_id)
        VALUES (:plataforma, :nome_perfil, :brand_id)
        ON CONFLICT DO NOTHING;
    """)
    
    registros = df_perfis.to_dict(orient="records")
    
    with engine.begin() as conn:
        for row in registros:
            conn.execute(query_upsert, row)
            
    print("-> Tabela dim_perfis populada com sucesso!")

if __name__ == "__main__":
    popular_perfis()