def log(severity, text):
    logs = open("info.log", "a")
    logs.write(f"{severity}: {text}\n")
    logs.close()