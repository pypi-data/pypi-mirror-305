from ..minicrm_api import MiniCrmClient

client = MiniCrmClient(76354, "fGD6Tj5aEwFc0WzdJ3QCerPSBxpuOHXo")

address = client.get_address("84")
print(address)
