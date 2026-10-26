# 📊 Social Metrics Dashboard — Pipeline ETL & Business Intelligence

Um projeto completo de **Engenharia de Dados e BI** desenvolvido para coletar, transformar, armazenar e visualizar métricas de redes sociais de forma automatizada e escalável.

---

## 🚀 Arquitetura e Tecnologias
O projeto foi construído seguindo boas práticas de desenvolvimento e arquitetura orientada a configuração:
* **Linguagem:** Python 3.10+
* **Manipulação de Dados:** Pandas
* **Banco de Dados & Armazenamento:** PostgreSQL (hospedado no **Supabase**)
* **Modelagem:** Camada relacional com tabelas de Dimensão (`dim_perfis`) e Fato (`fato_metricas`), unificadas via **SQL Views**.
* **Visualização de Dados (BI):** Google Looker Studio.

---

## ⚙️ Estrutura do Pipeline
1. **Ingetão / Simulação:** Extração de dados diários de redes sociais (Instagram, TikTok e LinkedIn) através de adaptadores isolados.
2. **Transformação:** Limpeza, tratamento de tipos e consolidação utilizando Pandas.
3. **Carga (Load):** Persistência automatizada no Supabase via operações de *Upsert* utilizando SQLAlchemy.
4. **Camada Analítica:** View SQL otimizada (`vw_dashboard_metricas`) para consumo direto pela ferramenta de BI.

---

## 📈 Visualização do Dashboard (Looker Studio)
O painel executivo consolida os principais indicadores de performance (KPIs), séries temporais e análises de engajamento multiplataforma.

👉 **[Acesse o Dashboard Público aqui](https://datastudio.google.com/s/sQg4iSb-o_c)**

### Principais Blocos do Painel:
* **Filtros Globais:** Seleção de período dinâmico e filtro por plataforma.
* **Cartões de KPI:** Seguidores totais, seguidores ganhos, alcance, impressões e engajamento.
* **Série Temporal:** Evolução diária do crescimento de seguidores por rede social.
* **Análise de Interações:** Gráficos comparativos de curtidas, comentários e compartilhamentos.
* **Visão Granular:** Tabela detalhada de performance por perfil e gráfico de distribuição de alcance.

---

## 🛠️ Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/social-metrics-dashboard.git](https://github.com/SEU-USUARIO/social-metrics-dashboard.git)
   cd social-metrics-dashboard