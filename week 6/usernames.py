def extract_usernames(emails):
    usernames = []

    for email in emails:
        email = email.strip().lower()
        email_split = email.split("@")
        username = email_split[0]
        if username not in usernames:
            usernames.append(username)

    usernames.sort()
    
    return usernames