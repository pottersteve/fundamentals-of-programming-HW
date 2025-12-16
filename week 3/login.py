#department = "CS"
#is_banned = False
#ignore_checks = True

allow_login = False

if department == "CS" and not is_banned or ignore_checks:
    allow_login = True

print(allow_login)