from supabase import create_client, Client
import datetime

# ====> INSIRA AQUI SUA URL DO SUPABASE
SUPABASE_URL = "https://drfclkhcuewmxbryuyhp.supabase.co"

# ====> INSIRA AQUI SUA CHAVE SECRETA (SERVICE_ROLE KEY)
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyZmNsa2hjdWV3bXhicnl1eWhwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTg0NzQxNCwiZXhwIjoyMDYxNDIzNDE0fQ.D9jjbElP_ZxYinqlbKA1jcwY9D0g9y9n4MqTl_YUELo"

# Conexão com Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Dados de exemplo
data = {
    "sigrc": 12345,
    "endereco": "Rua Exemplo",
    "numeral": 100,
    "bairro": "Centro",
    "distrito": "Distrito Central",
    "risco": 2,
    "motivo": "Manutenção Preventiva",
    "data": "2025-04-28"  # formato ISO: yyyy-mm-dd
}

# Validação básica
if not isinstance(data["sigrc"], int) or not isinstance(data["numeral"], int) or not isinstance(data["risco"], int):
    print("❌ ERRO: sigrc, numeral e risco devem ser inteiros.")
else:
    try:
        response = supabase.table("tabela_unica").insert([data]).execute()

        if response.data:
            print("\n✅ Dados inseridos com sucesso!\n")
            print("📦 Retorno Supabase:")
            print(response.data)
        else:
            print("⚠️ Nenhum dado retornado, mas pode ter sido inserido.")
            print("🔍 Verifique sua tabela manualmente.")

    except Exception as e:
        print("\n❌ ERRO AO INSERIR DADOS NO SUPABASE:")
        print(str(e))
