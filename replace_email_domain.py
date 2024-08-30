#Replace Email domain
# Example usage:
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("user@gmail.com", "gmail.com", "example.com"))

#Output : user@example.com

#Example 
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
  
print(replace_domain("arjun@gmail.com","gmail.com","dog,com"))

#Output : arjun@dog,com

