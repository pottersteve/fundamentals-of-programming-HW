import requests


def fetch_posts(userInput):
    url = f"https://api.tvmaze.com/search/shows?q={userInput}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    
def RemoveHTMLTags(text):
    result = ""
    inside_tag = False

    for ch in text:
        if ch == '<':
            inside_tag = True
            continue
        if ch == '>':
            inside_tag = False
            continue

        if not inside_tag:
            result += ch

    return result

def main():
    userInput = input("Enter show name: ").lower()
    posts = fetch_posts(userInput)
    if posts == []:
        print("No shows found.")
        return
    
    show = posts[0]["show"]

    name = show["name"]
    premiered = show["premiered"]
    summary = show["summary"]

    summary = RemoveHTMLTags(summary)

    print(f"Name: {name}")
    print(f"Premiered: {premiered}")
    print(f"Summary: {summary}")

if __name__ == "__main__":
    main()