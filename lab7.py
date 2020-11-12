lab 7

def new_contact_store():
    return {}   # Returns an empty dictionary to store information in
  
def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
    key = "{first_name} {last_name}"
    contacts[key]["First Name:"] = first_name
    contacts[key]["Last Name:"] = last_name
    contacts[key]["Email:"] = email
    contacts[key]["Phone Number:"] = phone_number
    contacts[key]["Birthday:"] = birthday    # Stores associated values to their respective indexes
    
    return contacts
  
  
def has_contact(contacts, first_name, last_name):
    key = "{first_name} {last_name}"
    contact_exists = False
    if key in contacts:   # Checks if the given name has values in the dictionary
      contact_exists = True
    
    return contact_exists
      
    
def get_contact_string(contacts, first_name, last_name):
    key = "{first_name} {last_name}"
    return contacts[key]    # Returns the list of values associated with the given name
  
  
def remove_contact(contacts, first_name, last_name):
    key = "{first_name} {last_name}"
    del contacts[key]   # Deletes the desired key location in the dictionary
    return contacts
    
    
def update_contact_first_name(contacts, first_name, last_name, new_field_value):
    key = "{first_name} {last_name}"
    contacts[key]["First Name:"] = new_field_value
    return contacts
    
    
def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    key = "{first_name} {last_name}"
    contacts[key]["Last Name:"] = new_field_value
    return contacts
    
    
def update_contact_email(contacts, first_name, last_name, new_field_value):
    key = "{first_name} {last_name}"
    contacts[key]["Email:"] = new_field_value
    return contacts
    
    
def update_contact_phone_number(contacts, first_name, last_name, new_field_value):
    key = "{first_name} {last_name}"
    contacts[key]["Phone Number:"] = new_field_value
    return contacts
    
    
def update_contact_birthday(contacts, first_name, last_name, new_field_value):
    key = "{first_name} {last_name}"
    contacts[key]["Birthday:"] = new_field_value
    return contacts
    
    

# Contact layout as follows: ['John', 'Smith','jsmith@gmail.com', '928-111-111', 'Nov. 10th']
