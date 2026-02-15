"""
User lookup functionality to retrieve email addresses for users.
"""
import json
import os


def get_email_for_user(name):
    """
    Lookup email address for a given user name.
    
    Args:
        name (str): The name of the user to lookup
        
    Returns:
        str or None: The email address if found, None otherwise
    """
    contacts_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'contacts.json')
    
    if not os.path.exists(contacts_file):
        print(f"Warning: {contacts_file} not found")
        return None
    
    try:
        with open(contacts_file, 'r') as f:
            data = json.load(f)
        
        names = data.get('names', [])
        emails = data.get('emails', [])
        
        if name in names:
            index = names.index(name)
            if index < len(emails):
                return emails[index]
        
        return None
    except Exception as e:
        print(f"Error reading contacts: {e}")
        return None
