# Splan
Terminal planner application for college students, with a TUI interface. Built using Textual py.

## New terminal
- Nice ascii art showcasing the current date and time
- When you open a new terminal you will see, A list of classes you have on that day and information associated with those classes, (location, time, etc)
- Underneath classes you will see office hours for that specific day
- If the class is today, you will see associated todo's for that class underneath the information for the class. (or just seperate)
- If the class is not today but there are still associated todo's for that class, they will be shown in a list of todo's below the class list
- If the todo is not associated with a class you will see a list of these todo's underneath the todo's associated with a class
- (note: there is no point in showing todos, only if they are associated with a class that you have on that exact day. You should show all the classes you have today, under that all of the tasks associated with all class even if its not on that day)

## Classes
- Add classes and associated office hours.
- Every time you open your terminal you will see which classes you have for that day.
- Run the `class` command to see all of your classes
- Run the `class --all` command to see all of your classes all associated info as well as todo's attached to classes
- Run the `OH` command to see all office hours for that week and what classes they are associated with
- Run `class {className}` to see class information and all associated todos for that class
- Run `class --list` to see all class names

