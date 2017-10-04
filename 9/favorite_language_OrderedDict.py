from collections import OrderedDict


favorite_languages = OrderedDict()
favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "C"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

print(type(favorite_languages))
print(favorite_languages)
print(favorite_languages.items())

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())