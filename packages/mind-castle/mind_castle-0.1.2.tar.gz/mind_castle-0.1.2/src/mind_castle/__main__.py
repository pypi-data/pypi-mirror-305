from mind_castle import stores
from mind_castle.secret_store_base import SecretStoreBase

print("\nMind-Castle - Shhhhh")
print("====================")
print("Available secret stores:\n")

for store in SecretStoreBase.__subclasses__():
    print(f"{store.store_type.ljust(30)}- Required env vars: {store.required_config}")