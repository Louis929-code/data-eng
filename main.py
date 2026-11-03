from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

print("=== Mon premier projet Data Engineer ===")
print(f"API_KEY chargée: {os.getenv('API_KEY')}")
print(f"Pandas version: {pd.__version__}")
# Crée un petit DataFrame comme un vrai Data Engineer
df = pd.DataFrame({
    "nom": ["Alice", "Bob"],
    "age": [25, 30]
})
print("\nMon premier DataFrame:")
print(df)