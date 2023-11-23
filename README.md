# Splan
Terminal planner application for college students, with a TUI interface. Built using Textual py.
the name is Splan because my name is sean and this is a planner

## New terminal
- Nice ascii art showcasing the current date and time

- New terminal shows all classes. (short overview of all classes and when/where)
    - Office hours today will be shown in daily section
    - Homeworks due today will be shown in daily section
    - Upcoming homeworks will be shown in upcoming secion
    - Upcoming Exams will be shown in upcoming secion

- Daily todo's (todos that you make 'today')
    - todo's associated with a class
        - overdue todo's
        - upcoming todos
    - todo's not associated with a class (internship, call family)
        - overdue todo's
        - upcoming todos
        - leetcode, reocurring + certain times per week)

- Todo items have to be physically checked off or else they will become overdue.
### Delete later
- homeworks and exams will be like a todo item without a need to check them off, they will also have some kind of associated data like a link or a filepath. it should be easy to get this associated data
- Homeworks and exams
    - Select class from dropdown
    - Homework name
    - Due date, M, D, Y 
    - Time due? no
    - infoDump - store info about the homework here. easy way to open this file with vim and edit it for each todo. Make it a markdown file
    - add a way to put a grade in eventually
    - if they dont get checked off how do they go away. 

## Commands
    - `splan` to get the startup screen
    - `splan class` to get a list of classes with all associated office hours and todos from now until the future
    - `splan class --archive` to get a list of all assocated past todos
    - `splan class --all` to get a list of all todos and homeworks ever
    - `splan class {className}` to get a list of all assocated past todos
    - `splan class {className} --archive` to get a list of all assocated past todos
    - `splan class {className} --all` to get a list of all todos and homeworks ever
    - Run the `splan OH` command to see all office hours for that week and what classes they are associated with
    - Run `splan class --list` to see all class names locations, and times only
## Adding new items
- `splan class add`
- `splan OH add`
- `splan homework add`





