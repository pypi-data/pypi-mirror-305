# Sess_I

[![PyPI version](https://badge.fury.io/py/sess-i.svg)](https://badge.fury.io/py/sess-i)

## What is Sess_I?
**A helper package for handling multi-page apps built using [Streamlit](https://streamlit.io/)**

Sess_I offers a simple and intuitive way of handling data persistency and widget states in multi-page apps.

The code is open-source, and available under a GPLv3 license. 

## Installation

```sh
pip install sess_i
```

## Tutorial

The main interface for interacting with the Sess_I package is through the Session State Interface (SSI). 

### Initialize the session interface

Start by importing the associated  class and initializing a SSI instance:

```sh
# HOME PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state=st.session_state
    page="home"
)
```

The SessI class takes 2 arguments:
    
* A session state argument, which is just the current streamlit session state (for more information, 
      check [here](https://docs.streamlit.io/library/advanced-features/session-state)). 
* A page argument, which is a string containing the current page name

You can now start building your app. 

### Handling widgets

With Sess_I, widget current values are handled by the SessI class. As such, when  initializing a widget, there are two 
key points to keep in mind:

* Widget keys are essential, as they are used to ensure state persistence between the different pages. The key 
  nomenclature is "[key id]_[page name]"
* When getting the value from a widget or when setting the widget's value, the current widget value can be accessed 
  through the SessI class.

The following is an example of a text widget being initialized with the SSI:

```sh
# HOME PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state = st.session_state
    page="home"
)

text_1 = st.text_input(
    label = "Tutorial",
    key = "text_1_home",
    value = session.widget_space["text_1_home"]
)
```

As shown above, the widget can be called from the session's widget space using the widget key. But here, as the widget 
space does not yet have information on the widget's value, it will return a *None* value. This can be problematic in 
most cases, and as such it is important to set widget defaults beforehand:

```sh
import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state = st.session state
    page = "home"
)

widget_default_values = {
    text_1_home : "Hello World"
}

session.set_widget_defaults(widget_default_values)

text_1=st.text_input(
    label="Tutorial",
    key="text_1_home",
    value=session.widget_space["text_1_home"]
)
```

> **_NOTE:_**  The note content.When setting widget default values, registering widgets or registering objects, SessI supports passing in mappings
(dictionaries) or keyword arguments.

When your page is done, the next step is to register the widget's and their values for future use. This is what makes 
it possible to keep widget states when switching between pages:

```sh
# HOME PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state=st.session_state
    page="home"
)

widget_default_values = {
    "text_1_home" : "Hello World"
}

session.set_widget_defaults(widget_default_values)

text_1 = st.text_input(
    label="Tutorial",
    key="text_1_home",
    value=session.widget_space["text_1_home"]
)
  
session.register_widgets(
    text_1_home = "text_1"
)
```

### Handling objects

As with widgets, the first thing to do is to initialize a SSI instance:

```sh
# HOME PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state = st.session_state
    page = "Home"
)

```

Here as an example we will create a quick dataclass to store some example data:

```sh
  
@dataclass
class Something:
    foo: str
    bar: dict
    
example = Something(
    foo="Hello World",
    bar={}
)

```

The next step is to register the object into the object space. For this, we use the register_object that has two 
arguments:

* The object itself
* A key that contains the page name using the same convention as for widgets

```sh
# HOME PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state=st.session_state
    page="Home"
)
  
@dataclass
class Something:
    foo: str
    bar: dict
    
example = Something(
    foo="Hello World",
    bar={}
)

session.register_object(
    obj=example,
    key="example_home"
)

```

The object (and previously created widgets) can now be referenced from another page using the appropriate methods.

### Getting objects and widgets from another page

Let us now add a second page that will be called "About". We can instantiate a SessI object to get back information 
from the first page, and also add new widgets using the interface:

```sh
# ABOUT PAGE

import streamlit as st
from sess_i.base.main import SessI

session = SessI(
    session_state=st.session_state,
    page="About"
)
  
st.write(f"This was the text from the home page:\n{session.widget_space['text_1_home']}")

session.set_widget_defaults(
    text_2_About="Welcome to the about page"
)

text_2 = st.text_intput(
    label="example_2",
    key="text_2_About",
    value=session.widget_space["text_2_About"]
)
  
session.register_widgets(
    {"text_2_About": text_2}
)
```

And finally to access objects from the object space is as simple as accessing widgets through the get_object method of 
the SessI object or by using the object_space getter:

```sh

example = session.get_object(
    key = "example_home"
)

# OR

example = session.object_space["example_home"]

```
