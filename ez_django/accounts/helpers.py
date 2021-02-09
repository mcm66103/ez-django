import secrets

def generate_confirmation_number(): 
    return secrets.token_hex(16)