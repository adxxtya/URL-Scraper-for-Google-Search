# How to Run the Code
> First Install all the dependencies
```
pip install selenium
pip install csv
```
> For Windows
```
python shopify.py
```
> For Linux (Ubuntu)
```
python3 shopify.py
```

# How The Code Works

Basically we are storing the top search queries based on the Indian Search Data in the search_queries variable. 

In the Main Logic of the code we are mapping over the search_queries variable to search for every single value and then using a while loop to iterate over all of the pages in the google search

# The Drivers

The project currently have the geckdriver executable in the drivers folder.

Geckodriver in this repo is meant to be for linux environment and it shall run flawlessly in Ubuntu distros.

For windows, one will need to install the geckodriver which is supported by the windows os.

