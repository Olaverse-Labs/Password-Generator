from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import secrets
import string

app = FastAPI()

german_umlauts = 'äöüÄÖÜß'

@app.get("/generate-password")
def generate_password(
    length: int = Query(
        10, ge=4, le=32,
        description="Length of each password (min 4, max 32)."
    ),
    spchar: int = Query(
        2, ge=0,
        description="Number of special characters to include in each password."
    ),
    numbers: int = Query(
        2, ge=0,
        description="Number of digits to include in each password."
    ),
    umlauts: bool = Query(
        True,
        description="If true, include German umlauts (ä, ö, ü, Ä, Ö, Ü, ß) in the password."
    ),
    quantity: int = Query(
        10, ge=1, le=10,
        description="Number of passwords to generate (max 10 per call)."
    ),
    use_uppercase: bool = Query(
        True,
        description="If true, include uppercase letters in the base character set."
    ),
    use_digits: bool = Query(
        True,
        description="If true, include digits in the base character set (in addition to the required count)."
    ),
    use_symbols: bool = Query(
        True,
        description="If true, include special characters in the base character set (in addition to the required count)."
    )
):
    if spchar + numbers > length:
        return JSONResponse({"error": "Sum of spchar and numbers cannot exceed total length."}, status_code=400)
    if spchar > 0 and not use_symbols:
        return JSONResponse({"error": "Cannot require special characters (spchar > 0) when use_symbols is False."}, status_code=400)
    if numbers > 0 and not use_digits:
        return JSONResponse({"error": "Cannot require digits (numbers > 0) when use_digits is False."}, status_code=400)

    base_chars = list(string.ascii_lowercase)
    if use_uppercase:
        base_chars += list(string.ascii_uppercase)
    if umlauts:
        base_chars += list(german_umlauts)
    if use_digits:
        base_chars += list(string.digits)
    if use_symbols:
        base_chars += list(string.punctuation)
    # Remove duplicates
    base_chars = list(set(base_chars))
    if not base_chars:
        return JSONResponse({"error": "No character sets selected."}, status_code=400)

    special_chars = list(string.punctuation)
    digit_chars = list(string.digits)

    passwords = []
    for _ in range(quantity):
        pwd = []
        # Add required special characters
        if spchar > 0:
            pwd += [secrets.choice(special_chars) for _ in range(spchar)]
        # Add required digits
        if numbers > 0:
            pwd += [secrets.choice(digit_chars) for _ in range(numbers)]
        # Fill the rest with base chars
        remaining = length - spchar - numbers
        pwd += [secrets.choice(base_chars) for _ in range(remaining)]
        # Shuffle to randomize order
        secrets.SystemRandom().shuffle(pwd)
        passwords.append(''.join(pwd))
    return {"passwords": passwords} 