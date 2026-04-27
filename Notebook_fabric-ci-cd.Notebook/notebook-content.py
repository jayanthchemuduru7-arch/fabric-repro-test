# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c41c07e7-2c15-434f-ad3a-a64b8564d628",
# META       "default_lakehouse_name": "lakehouse1",
# META       "default_lakehouse_workspace_id": "04c06837-7694-4a23-b791-74ef2d0c3721",
# META       "known_lakehouses": [
# META         {
# META           "id": "c41c07e7-2c15-434f-ad3a-a64b8564d628"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Attempt to retrieve a secret from Key Vault using mssparkutils
secret = mssparkutils.credentials.getSecret(
    "https://newnewnew.vault.azure.net/",
    "AISECRET"
)
print(secret)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
