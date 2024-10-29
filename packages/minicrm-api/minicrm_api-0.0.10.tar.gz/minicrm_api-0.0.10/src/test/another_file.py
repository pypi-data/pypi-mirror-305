from ..minicrm_api import MiniCrmClient
from datetime import datetime, timedelta

client = MiniCrmClient(76354, "fGD6Tj5aEwFc0WzdJ3QCerPSBxpuOHXo")

data = client.get_adatlap_details(172)
address = client.get_address(data["ContactId"])
print(address)
