from supabase import create_client, Client

# ====> INSIRA AQUI SUA URL DO SUPABASE
SUPABASE_URL = "https://drfclkhcuewmxbryuyhp.supabase.co"

# ====> INSIRA AQUI SUA CHAVE SECRETA (SERVICE_ROLE KEY)
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyZmNsa2hjdWV3bXhicnl1eWhwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTg0NzQxNCwiZXhwIjoyMDYxNDIzNDE0fQ.D9jjbElP_ZxYinqlbKA1jcwY9D0g9y9n4MqTl_YUELo"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Exemplo de dados para inserção automática
data = {
    "sigrc": 12345,
    "endereco": "Rua Exemplo",
    "numeral": 100,
    "bairro": "Centro",
    "distrito": "Distrito Central",
    "risco": 2,
    "motivo": "Manutenção Preventiva",
    "data": "2025-04-28"
}

try:
    response = supabase.table("tabela_unica").insert([data]).execute()
    print("✅ Dados inseridos com sucesso:", response.data)

except Exception as e:
    print("❌ Erro ao inserir dados:", e)
