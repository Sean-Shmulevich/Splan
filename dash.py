# Create todo list item
# weekly task, will work similar to a class and office hours
# Create class. first to edit screen then to create.
    # See all of the classes added, be able to delete them
    # See office hours, attached to a class or seperate?

# Need to add a calendar system for todo list items and homeworks/tests
# Create a homework
    # Attached to a class

# rocurring todolist item.
# class and office hours weekly reocurring event both have a time, weekly task does not have a time (leetcode)

# todolist item either reocurring or not.
    # reocurring item is like a class or office hours but not attached to a class and does not have a time

    # todo today, quick task. carry over to the next day if not completed, still attached to an exact day 
    # non reocurring item is like an email to send or an job application to finish, should be attached to an exact day, carried over if not completed
    # if task is not completed by the due date, it should be moved to the next day until it is marked completed
    # upcoming tasks should be shown if they are tasks within

# reocurring item has a time, non reocurring does not have a time
# homework, associated with a certain exact day/month no time
# exams, same as homework

# the only difference between todo list items and homework is that todo list items dont carry over if they are not completed

#todo - optional to associate them with a class, have task details with links to resources, easily append info or edit these files.
#todo needs to check off
    #today
    #nonreocurring homework
    #reocurring
#class
#office hours

# Dash starts with just buttons
# See all todo items in the next 7 days, be able to check them off (and delete them?)
    # Create todo item, today, non reocurring, reocurring. all items carry over if not checked off
        # for all options ask is associated with a class
            # is exam, homework, email, application, project, misc
            # if project add pathsomehow
        #if not associated with a class dont associate it put it in a misc todo's
# Class + office hours
# see list of classes with office hours underneath them, a button to remove the class and the office hours associated
    # button to add a class
    # button to add office hours

#then dash should have some useful info # calendar with daily events todos, and classes/office hours., can configure what is on this screen from textual.app import App, ComposeResult from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Label
from term_bg import query_terminal, parse_rgb_value
from textual.containers import Container
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from inputClass import InputClass
from officehours import InputOH

class ButtonsApp(App):
    color_response = query_terminal("\033]11;?\033\\")
    bg_rgb = parse_rgb_value(color_response)

    CSS= """
    Button {
        width: 50%;
    }

    VerticalScroll {
    }

    Label {
        width: 50%;
        background: """+bg_rgb+""";\n
        text-align: center;
        padding: 1;
    }
    Container {
        layout: horizontal;
        align: center top;
    }

    Horizontal {
        align: center top;
        height: 10%;
    }
    #label_container {
        height: 10%;
    }
    Screen {
        background: """+bg_rgb+""";\n}"""

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Container(
                Button.error("Manage Todos and Homework"),
                Button.success("Manage Classes"),
            ),
        )

        # todo, load in todo list items from a file, determine which are in the next 7 days
        # make it a scrollable vertical list within the container
        # load in todo's and allow them to be checked off
        # load in classes and just show them along with a short preview of the details

        # make an input form for office hours
        with Container(id="label_container"):
            yield Label("Todo list items")
            yield Label("Classes")
        with Container():
            with VerticalScroll():
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
            with VerticalScroll():
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")
                yield Label("CS1520")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.label)


if __name__ == "__main__":
    app = ButtonsApp()
    buttonPressed = app.run()
    if(str(buttonPressed) == "Manage Todos and Homework"):
        app = InputClass()
        app.run()
    else:
        app = InputOH()
        app.run()
