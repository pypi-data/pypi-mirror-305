import random
import hashlib

def random_hex_digit():
    """Helper to generate a random hexadecimal digit."""
    return f"{random.randint(0, 15):x}"

def random_decimal_digit():
    """Generate a random decimal digit."""
    return str(random.randint(0, 9))

def generate_uuid1():
    """Generate a UUID with version 1, ensuring the correct UUID structure."""
    part1 = ''.join([random_hex_digit() for _ in range(8)])
    part2 = ''.join([random_hex_digit() for _ in range(4)])
    part3 = '1' + ''.join([random_hex_digit() for _ in range(3)])  # Version 1 identifier
    part4 = ''.join([random_hex_digit() for _ in range(4)])
    part5 = ''.join([random_hex_digit() for _ in range(12)])
    return f"{part1}-{part2}-{part3}-{part4}-{part5}"

def generate_uuid4():
    """Generate a UUID with version 4, ensuring the correct UUID structure."""
    part1 = ''.join([random_hex_digit() for _ in range(8)])
    part2 = ''.join([random_hex_digit() for _ in range(4)])
    part3 = '4' + ''.join([random_hex_digit() for _ in range(3)])  # Version 4 identifier
    part4 = ''.join([random_hex_digit() for _ in range(4)])
    part5 = ''.join([random_hex_digit() for _ in range(12)])
    return f"{part1}-{part2}-{part3}-{part4}-{part5}"

def generate_uuid7():
    """Generate a UUID with version 7, ensuring the correct UUID structure."""
    part1 = ''.join([random_hex_digit() for _ in range(8)])
    part2 = ''.join([random_hex_digit() for _ in range(4)])
    part3 = '7' + ''.join([random_hex_digit() for _ in range(3)])  # Version 7 identifier
    part4 = ''.join([random_hex_digit() for _ in range(4)])
    part5 = ''.join([random_hex_digit() for _ in range(12)])
    return f"{part1}-{part2}-{part3}-{part4}-{part5}"

def generate_nil_uuid():
    """Generate a nil UUID."""
    return '00000000-0000-0000-0000-000000000000'

def generate_guid():
    """Generate a UUID with version 4, ensuring the correct UUID structure."""
    part1 = ''.join([random_hex_digit() for _ in range(8)])
    part2 = ''.join([random_hex_digit() for _ in range(4)])
    part3 = ''.join([random_hex_digit() for _ in range(4)])
    part4 = ''.join([random_hex_digit() for _ in range(4)])
    part5 = ''.join([random_hex_digit() for _ in range(12)])
    return f"{part1}-{part2}-{part3}-{part4}-{part5}"

def generate_multiple_uuids(version, count):
    """Generate multiple UUIDs for a specified version."""
    if count < 2 or count > 50:
        raise ValueError("Count must be between 2 and 50.")
    generator = {
        1: generate_uuid1,
        4: generate_uuid4,
        7: generate_uuid7,
    }.get(version)

    if not generator:
        raise ValueError("Unsupported version.")
    return [generator() for _ in range(count)]

def generate_uuid_for_email(email):
    """Generate a consistent UUID-like string based on an email."""
    if not isinstance(email, str) or not email:
        raise ValueError("Please provide a valid email address.")
    return email_to_uuid(email)

def email_to_uuid(email):
    """Convert an email to a UUID-like format using hashing."""
    email_hash = hashlib.md5(email.encode()).hexdigest()
    return f"{email_hash[:8]}-{email_hash[8:12]}-4{email_hash[12:15]}-{email_hash[15:19]}-{email_hash[19:32]}"

def generate_custom_uuid(pattern: str, segment_length: int, static_prefix: str = ""):
    """
    Generate a custom UUID-like string based on a user-defined pattern and segment length.

    :param pattern: A string defining the pattern (e.g., 'xxxx-xxxx-xxxx').
                    Use 'x' for random hex digits and 'd' for random decimal digits.
    :param segment_length: The length of each segment defined by the user.
    :param static_prefix: A static string to prepend to the generated UUID.
    :return: A custom UUID-like string.
    """
    result = []

    # Split the pattern by the separator '-'
    segments = pattern.split('-')

    for segment in segments:
        segment_result = ""
        for char in segment:
            if char == 'x':
                segment_result += random_hex_digit()
            elif char == 'd':
                segment_result += random_decimal_digit()
            else:
                segment_result += char  # Static characters stay the same

        # Ensure the segment matches the desired segment length
        if len(segment_result) < segment_length:
            segment_result += ''.join(random_hex_digit() for _ in range(segment_length - len(segment_result)))

        result.append(segment_result[:segment_length])  # Trim to segment length

    return f"{static_prefix}-{'-'.join(result)}" if static_prefix else '-'.join(result)

