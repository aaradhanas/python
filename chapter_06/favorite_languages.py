fav_languages = {
    'vde': 'python',
    'gopi': 'java',
    'sudha': 'ruby',
    'preethi': 'perl',
    }


#Iterate over the object as key,value pairs
for name,language in fav_languages.items():
    print("The favorite language of "+name.title()+" is "+ language.title())