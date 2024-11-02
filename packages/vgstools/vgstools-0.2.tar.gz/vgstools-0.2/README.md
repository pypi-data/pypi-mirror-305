# A Collection of tools from my first year!

This package just serves as a collection of tools which I may or may not need in the future.

It includes 
- ``load_words`` to sort wordlists into a list for easy list/string handling.
- ``decrypt_words()`` to decrypt a wordlist encoded in a caesar cipher (look in KPR-Prosjekt on my profile for context) 
- ``validate_password`` a password strength checker and 
- ``decrypt()`` which is the same as ``decrypt_words()`` and takes in a string.

# Download
Make sure to upgrade pip to the newest version before you download!
````shell
pip install vgstools
````
To access the package
````python3
// Import only functions
>>> from tools import decipher
>>> decipher("rah")

// Import tools on it's own
>>> import tools
>>> tools.validate_password("password")
````


# License
This package uses the MIT License.
