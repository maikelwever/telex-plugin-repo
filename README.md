# Central Package Repository for telegram-pybot

# Submit a package

Clone the repository.

Edit pkglist.txt and add a unique simple package name, and a http/s url to the location of the repository folder.

E.g.
```
whiskey https://raw.githubusercontent.com/xlopo/tg-pybot-whiskey/master/repository
dice    https://raw.githubusercontent.com/datamachine/telegram-pybot-dice/master/repository
weather https://raw.githubusercontent.com/datamachine/telegram-pybot-weather/master/repository
my-plugin	https://raw.githubusercontent.com/exmaple/telegram-pybot-example/master/repository
```

Make a pull request.

repo.json is generated automatically using the latest data in your repository/repo.json file.
 
# Package Name Requirements

The package name in pkglist.txt is a simplified name of your package for use in the package manager.

You package name must match the following requirements

* Must contain only unicode word characters, dashes '-', and underscores '_'
* Must nott begin with a - or an underscore
* Must be all lower case
* Must be unique to the repo
* Must be at least two characters in length

For illustration purposes, this is roughly equivalent to the python 3.4 regex:

```
 "^\w[\w\-_]+"
```

