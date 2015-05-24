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

You package name must contain only the following characters:

* unicode word charcater
* lowercase
* dash "-"
* underscore "_"

This is equivalent to the python 3.4 regex u"[\w-]"

