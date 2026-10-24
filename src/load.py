import os
import pandas as pd
from sqlalchemy import create_engine, text
from src.config import Config

def get_db_engine():
    """Cria e retorna a engine de conexão com o PostgreSQL do Supabase."""
    db_url = Config.DATABASE_URL
    if not db_url:
        raise ValueError("A variável DATABASE_URL não foi encontrada no ambiente.")
    
    engine = create_engine(db_url)
    return engine

def salvar_metricas_upsert(df_metricas):
    """
    Insere ou atualiza (Upsert) as métricas diárias no Supabase PostgreSQL.
    """
    engine = get_db_engine()
    
    print(f"-> Salvando {len(df_metricas)} registros no Supabase (PostgreSQL)...")
    
    registros = df_metricas.to_dict(orient="records")
    
    query_upsert = text("""
        INSERT INTO fato_metricas (
            perfil_id, data, seguidores, seguidores_ganhos, 
            alcance, impressoes, engajamento, curtidas, 
            comentarios, compartilhamentos, cliques
        ) VALUES (
            :perfil_id, :data, :seguidores, :seguidores_ganhos, 
            :alcance, :impressoes, :engajamento, :curtidas, 
            :comentarios, :compartilhamentos, :cliques
        )
        ON CONFLICT (perfil_id, data) 
        DO UPDATE SET 
            seguidores = EXCLUDED.seguidores,
            seguidores_ganhos = EXCLUDED.seguidores_ganhos,
            alcance = EXCLUDED.alcance,
            impressoes = EXCLUDED.impressoes,
            engajamento = EXCLUDED.engajamento,
            curtidas = EXCLUDED.curtidas,
            comentarios = EXCLUDED.comentarios,
            compartilhamentos = EXCLUDED.compartilhamentos,
            cliques = EXCLUDED.cliques,
            atualizado_em = CURRENT_TIMESTAMP;
    """)
    
    with engine.begin() as conn:
        for row in registros:
            conn.execute(query_upsert, row)
            
    print("-> Carga e consolidação diária concluídas com sucesso no Supabase!")