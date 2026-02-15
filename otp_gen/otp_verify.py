"""
OTP verification functionality.
"""
from datetime import datetime
from otp_gen.otp_service import otp_storage


def verify_otp(email, otp):
    """
    Verify an OTP code for a given email address.
    
    Args:
        email (str): The email address to verify
        otp (str): The OTP code to verify
        
    Returns:
        bool: True if the OTP is valid, False otherwise
    """
    if email not in otp_storage:
        print(f"[OTP VERIFY] No OTP found for {email}")
        return False
    
    stored_data = otp_storage[email]
    stored_otp = stored_data['otp']
    expires_at = stored_data['expires_at']
    
    # Check if OTP has expired
    if datetime.now() > expires_at:
        print(f"[OTP VERIFY] OTP for {email} has expired")
        del otp_storage[email]
        return False
    
    # Check if OTP matches
    if stored_otp == otp:
        print(f"[OTP VERIFY] OTP verified successfully for {email}")
        del otp_storage[email]  # Remove OTP after successful verification
        return True
    else:
        print(f"[OTP VERIFY] Invalid OTP for {email}")
        return False
