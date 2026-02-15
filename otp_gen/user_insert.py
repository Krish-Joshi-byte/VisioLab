"""
User insertion functionality to add new users to the contacts database.
"""
import json
import os


def insert_user(name, email):
    """
    Insert a new user into the contacts database.
    
    Args:
        name (str): The name of the user
        email (str): The email address of the user
        
    Returns:
        bool: True if successful, False otherwise
    """
    contacts_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'contacts.json')
    
    try:
        # Load existing contacts
        if os.path.exists(contacts_file):
            with open(contacts_file, 'r') as f:
                data = json.load(f)
        else:
            data = {'names': [], 'emails': []}
        
        # Check if user already exists
        if name in data.get('names', []):
            print(f"User {name} already exists, updating email")
            index = data['names'].index(name)
            data['emails'][index] = email
        else:
            # Add new user
            data.setdefault('names', []).append(name)
            data.setdefault('emails', []).append(email)
        
        # Save updated contacts
        with open(contacts_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Successfully added/updated user: {name} -> {email}")
        return True
        
    except Exception as e:
        print(f"Error inserting user: {e}")
        return False
