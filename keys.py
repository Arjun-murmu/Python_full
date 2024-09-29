#Q1
def email_list(domains):
	emails = []
	for domains,users in domains.items():
	  for user in users:
	    emails.append(f"{user}@{domains}")
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#Q2
def groups_per_user(group_dictionary):
    user_groups = {}
    
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Create the entry for the user if it doesn't exist
            if user not in user_groups:
                user_groups[user] = []
            # Add the group to the user's list of groups
            user_groups[user].append(group)

    return user_groups

# Example usage
print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))
# Output : {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
