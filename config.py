import logging

# Extract secrets
secrets = {}
with open("secrets.txt") as f:
    for line in f:
        try:
            pair = line.split("=")
            secrets[pair[0]] = pair[1]
        except Exception as e:
            logging.critical(f"Incorrect formatting of secrets: {e}")

