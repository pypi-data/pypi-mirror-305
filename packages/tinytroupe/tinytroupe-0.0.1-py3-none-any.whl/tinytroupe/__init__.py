import warnings

message =\
"""
You are NOT importing the actual TinyTroupe library! Don't use `pip install`! This is just a PyPI placeholder for now. We do hope to make it available on PyPI in the future, which is why this
placeholder exists.

TO ACTUALLY INSTALL the TinyTroupe library, please do it directly from the GitHub repository according to the instructions given there: 

       https://github.com/microsoft/tinytroupe

If you do that, the GitHub version will override this PyPI placeholder, since it has a higher version number.
"""

print("!!! WARNING !!!")
print(message)
print("!!! WARNING !!!")
