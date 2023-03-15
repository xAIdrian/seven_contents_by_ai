# UTILITY
import os
import json

def open_url(url):
    '''
        Function to Open URL.
        Used to open the authorization link
    '''
    import webbrowser
    print(url)
    webbrowser.open(url)

def parse_redirect_uri(redirect_response):
    '''
        Parse redirect response into components.
        Extract the authorized token from the redirect uri.
    '''
    from urllib.parse import urlparse, parse_qs
 
    url = urlparse(redirect_response)
    url = parse_qs(url.query)
    return url['code'][0]

def save_token(filename,data):
    '''
        Write token to credentials file.
    '''
    data = json.dumps(data, indent = 4) 
    with open(filename, 'w') as f: 
        f.write(data)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print("Deletion Failed: The file does not exist")  

def get_title_subquery( text ):
	return text[0:32]        