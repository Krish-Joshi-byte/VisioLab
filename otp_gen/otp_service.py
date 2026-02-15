"""
OTP generation and email sending service.
"""
import secrets
import string
from datetime import datetime, timedelta


# In-memory storage for OTPs (in production, use a database)
otp_storage = {}


def generate_otp(length=6):
    """
    Generate a cryptographically secure random OTP code.
    
    Args:
        length (int): Length of the OTP code
        
    Returns:
        str: The generated OTP code
    """
    return ''.join(secrets.choice(string.digits) for _ in range(length))


def generate_and_send_otp(email):
    """
    Generate an OTP and send it to the specified email address.
    
    Args:
        email (str): The email address to send the OTP to
        
    Returns:
        str: The generated OTP code
    """
    otp = generate_otp()
    
    # Store OTP with expiration time (5 minutes)
    otp_storage[email] = {
        'otp': otp,
        'expires_at': datetime.now() + timedelta(minutes=5)
    }
    
    # In a real implementation, this would send an email
    # For now, just print it
    print(f"[OTP SERVICE] Generated OTP for {email}: {otp}")
    print(f"[OTP SERVICE] (In production, this would be sent via email)")
    
    return otp
