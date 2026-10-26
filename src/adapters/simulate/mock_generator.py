import pandas as pd
from datetime import datetime
import random
from config.settings import Settings

def extrair_dados():
    """Gera dados simulados realistas mantendo o mock isolado da configuração oficial."""
    perfis = Settings.obter_perfis()
    registros = []
    data_hoje = datetime.now().date()
    
    # Bases de seguidores estáticas mantidas exclusivamente no escopo do simulador
    bases_simuladas = {
        1: 15200, # Instagram
        2: 8400,  # LinkedIn
        3: 9640   # Tiktok
    }
    
    for perfil in perfis:
        if not perfil.get("ativo", True):
            continue
            
        perfil_id = perfil["perfil_id"]
        base_atual = bases_simuladas.get(perfil_id, 10000)
        
        seguidores_ganhos = random.randint(5, 45)
        seguidores_totais = base_atual + seguidores_ganhos
        alcance = random.randint(1200, 4500)
        impressoes = alcance + random.randint(500, 1500)
        engajamento = int(alcance * random.uniform(0.04, 0.12))
        
        registros.append({
            "perfil_id": perfil_id,
            "data": data_hoje,
            "seguidores": seguidores_totais,
            "seguidores_ganhos": seguidores_ganhos,
            "alcance": alcance,
            "impressoes": impressoes,
            "engajamento": engajamento,
            "curtidas": int(engajamento * 0.70),
            "comentarios": int(engajamento * 0.20),
            "compartilhamentos": int(engajamento * 0.10),
            "cliques": random.randint(30, 150)
        })
        
    print("-> [SIMULAÇÃO] Dados gerados com sucesso via adaptador mock isolado.")
    return pd.DataFrame(registros)