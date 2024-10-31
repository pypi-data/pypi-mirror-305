"""
Session-State interface module

Create class containing the whole sess_i interface. The class contains two subclasses:
    * Object space: contains the logic for handling tool calculation layer and communication with the widget spaces
    * Widget space(s): contains the logic for handling data persistency throughout page switching in the GUI
The main class when initialized will automatically generate an object space. Widget spaces will be generated with a
specific command. This is because while there is only one object space, there can be multiple widget spaces (one for
each page).

The user will start by initializing the sess_i object, passing in as argument the streamlit session state for the
current user. Internally, a widget space is initialized with the current page. This creates an entry in the Global
Widget Space that will hold the different widget keys and associate a page id to them.

On page load:
    1) If first pass: Initialize session, create page widget space and Global Space in session_state. Put the widget
    space object into the Global Space. Initialize widget defaults from user kwargs.
    Create object space, add to session state and create objects container inside the Space.
    On leave: add widget values inside widgets container. Update Object in session state from object space.
    2) Else: Initialize session. Initialize widget values from Widget Space stored values.
"""


class SessI:

    def __init__(self, session_state, page=None):
        """
        Initialise session interface object
        :param session_state: The state of the current session.
        :param page: The id of the page. If not provided, it defaults to the
                     name of the current file.
        """
        self.session_state = session_state
        self.page = page if page is not None else __file__.split("\\")[-1][:-3]
        self.object_space = ObjectSpace(self.session_state)
        self.widget_space = WidgetSpace.initialize_session(
            self.session_state, self.page
        )

    def __repr__(self):
        return f"Page = {self.page}\n" \
               f"Registered Objects = {self.object_space.objects}\n" \
               f"Widgets = {self.widget_space.widgets}"

    def set_widget_defaults(self, mapping=None, **kwargs):
        """
        Sets the default values for the designated widgets.

        :param mapping: A dictionary containing the default values for the widgets.
        :param kwargs: The default values for the widgets as keyword arguments.
        """
        self.widget_space.set_widget_defaults(mapping, **kwargs)

    def register_widgets(self, mapping=None, **kwargs):
        """
        Registers widgets in the widget space of the current page.

        :param mapping: A dictionary containing the widgets to be registered.
                        If not provided, it defaults to None.
        :param kwargs: The widgets to be registered as keyword arguments.
        """
        self.widget_space.register_widgets(mapping, **kwargs)

    def register_object(self, obj, key):
        """
        Registers an object in the object space.

        :param obj: The object to be registered.
        :param key: The key associated with the object.
        """
        self.object_space[key] = obj

    def get_object(self, key):
        """
        Retrieves an object from the object space.

        :param key: The key of the object.
        :return: The object associated with the key if it exists, None otherwise.
        """
        return self.object_space[key]

    def get_widget(self, key, page=None):
        """
        Retrieves the value of a widget from the widget space of a designated
        page. If the page is not provided, it defaults to the current page.

        :param key: The key of the widget.
        :param page: The id of the page. If not provided, it defaults to the current page.
        :return: The value of the widget if it exists, None otherwise.
        """
        widget_space = self.session_state["Global_Widget_Space"].get(
            page, self.widget_space
        )
        return widget_space[key]


# Object Space
class ObjectSpace:
    """
    The ObjectSpace class is a container for objects and their data. It
    provides methods to register objects with specific keys, retrieve
    objects by their keys, and update the values of objects. The state of
    the session is stored in the session_state attribute, and the objects
    are stored in the objects attribute, which is a dictionary.
    """

    def __init__(self, session_state):
        """
        Constructs all the necessary attributes for the ObjectSpace object.

        :param session_state: The state of the session.
        """
        self.session_state = session_state
        self.objects = self.session_state.setdefault("Object_Space", {})

    def __repr__(self):
        """
        Returns a string representation of the ObjectSpace object.

        :return: A string representation of the stored objects.
        """
        return f"Stored objects:\n{self.objects}"

    def __getitem__(self, item):
        """
        Returns the object associated with the key.

        :param item: The key of the object.
        :return: The object associated with the key.
        """
        return self.objects.get(item)

    def __setitem__(self, key, value):
        """
        Sets the value of the object associated with the key and updates the session state.

        :param key: The key of the object.
        :param value: The value of the object.
        """
        self.objects[key] = value
        self.session_state["Object_Space"] = self.objects


# Widget Space
class WidgetSpace:
    """
    Every widget space must contain two base parameters:
        * The id of the page it communicates with
        * A container with the widgets and their state metadata (key & value)
    """

    def __init__(self, session_state, page):

        self.page = page
        self.session_state = session_state
        if "Global_Widget_Space" not in session_state.keys():
            self.session_state["Global_Widget_Space"] = {page: self}
        self.widgets = {key: value for key, value in session_state.items() if str(self.page) in key}

    def __repr__(self):
        return f"WidgetSpace.widgets({self.widgets})"

    def __getitem__(self, item):
        return self.widgets.get(item)

    @classmethod
    def initialize_session(cls, session_state, page=None):
        """
        Initialize widget space and add it to the Global Space.

        This method initializes a widget space for a given page and adds it
        to the Global Space in the session state. If the page is not
        provided, it defaults to the name of the current file. If the Global
        Space does not exist, it is created. If the widget space for the
        given page does not exist in the Global Space, it is created.

        :param session_state: The state of the current session.
        :param page: The id of the page. If not provided, it defaults
                     to the name of the current file.
        :return: The widget space for the given page.
        """

        # if page is None:
        #     page = __file__.split("\\")[-1][:-3]
        # if "Global_Widget_Space" not in session_state.keys():
        #     space = WidgetSpace(session_state, page)
        #     session_state["Global_Widget_Space"] = {page: space}
        #     return st.session_state["Global_Widget_Space"][page]
        # else:
        #     if page not in session_state["Global_Widget_Space"].keys():
        #         session_state["Global_Widget_Space"].update({page: WidgetSpace(session_state, page)})
        #     return st.session_state["Global_Widget_Space"][page]

        # Refactored: to test
        page = page or __file__.split("\\")[-1][:-3]
        global_space = session_state.get("Global_Widget_Space", {})

        if page not in global_space:
            global_space[page] = WidgetSpace(session_state, page)

        session_state["Global_Widget_Space"] = global_space
        return session_state["Global_Widget_Space"][page]

    def set_widget_defaults(self, mapping=None, **kwargs):
        """
        Add default values to widgets in the widget space. If the widget space is empty, initialize it.
        :param mapping: Widget defaults as key-value pairs. Default is None.
        :param kwargs: Widget defaults as keyword arguments.
        """
        updates = mapping or {key: value for key, value in kwargs.items()}
        if not self.widgets:
            self.widgets = updates
        else:
            self.widgets.update(updates)

    def register_widgets(self, mapping=None, **kwargs):
        """
        This method is used to register widgets in the widget space. It
        updates the widgets dictionary with the provided mapping and keyword
        arguments. If the widget space for the current page does not exist,
        it raises a KeyError.

        :param mapping: A dictionary containing widget mappings. Default is None.
        :param kwargs: Keyword arguments for adding to the mapping of widgets.
        :raises KeyError: If the widget space for the current page does not
                          exist in the Global_Widget_Space.
        """
        widget_space = self.session_state["Global_Widget_Space"].get(self.page)
        if widget_space is None:
            raise KeyError(f"Widget space for page '{self.page}' doesn't exist.")
        self.widgets.update(mapping or {}, **kwargs)


if __name__ == "__main__":
    pass
