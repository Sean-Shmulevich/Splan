from textual import events

from textual.app import App, ComposeResult
from textual.widgets import RichLog
from textual import on
from textual.app import App, ComposeResult
from textual.validation import Function, Number, ValidationResult, Validator
from textual.widgets import Input, Label, Pretty, Static, Checkbox, Select
from textual.containers import VerticalScroll
import json
import os

from term_bg import query_terminal, parse_rgb_value

# this file will open a text input box that asks
# class name, class time, checkbox for days of the week, location

# make a generic checkbox function and a generic text input function
# store the state of the checkbox in an array in this format ["M", "W", "F""] where the array 
# store the state of the text input in an array in this format ["inputName": "currentInput"]
# whenever the submit button is pressed all of these states should be captured 

# Ai notebook

class InputClass(App):
    """App to display key events."""
    bg_rgb = ""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.checkboxes = {}
        self.times = {}
        self.inputs = {}

    # def __init__(self):
    #     color_response = query_terminal("\033]11;?\033\\")
    #     bg_rgb = parse_rgb_value(color_response)

    # send escape secuence through the os to make the
    # bg of the app the same as the bg of the terminal
    color_response = query_terminal("\033]11;?\033\\")
    bg_rgb = parse_rgb_value(color_response)

    CSS = """
    Input.-valid {
        border: tall $success 60%;
    }
    Select {
        width: 40%; 
    }
    Input.-valid:focus {
        border: tall $success;
    }
    Input {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    Screen {
        align: center top;
    }

    VerticalScroll {
        background: $boost;
        padding: 2;
        layout: horizontal;
        height: auto
    }

    Screen {
        background: """+bg_rgb+""";\n}"""


    def compose(self) -> ComposeResult:
        # Storing references to checkboxes
        hour_options = [(str(hour), hour) for hour in range(24)]
        minute_options = [(str(minute), minute) for minute in range(60)]

        # Storing references to inputs
        class_name_input = Input(placeholder="CS 0401", id="class_name_input")
        self.inputs["class_name"] = class_name_input
        yield Label("Class name")
        yield class_name_input

        class_location_input = Input(placeholder="5625 Sennot Square", id="class_location_input")
        self.inputs["class_location"] = class_location_input

        yield Label("Class location")
        yield class_location_input

        yield Label("Days of the week")
        with VerticalScroll():
            for day in ["M", "T", "W", "Th", "F", "S", "Su"]:
                checkbox = Checkbox(day, id=day)
                self.checkboxes[day] = checkbox
                yield checkbox


        yield Label("Start time")
        with VerticalScroll():
            yield Label("Hour")
            startTime = Select(hour_options)
            self.times["eventStart_start"] = startTime
            yield startTime
            yield Label("Minute")
            endTime = Select(minute_options)
            self.times["eventStart_end"] = endTime
            yield endTime

        yield Label("End time")
        with VerticalScroll():
            yield Label("Hour")
            startTime = Select(hour_options)
            self.times["eventEnd_start"] = startTime
            yield startTime
            yield Label("Minute")
            endTime = Select(minute_options)
            self.times["eventEnd_end"] = endTime
            yield endTime




    def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            # Capture the states of checkboxes and inputs
            # print(self.checkboxes)


            checkbox_states = {name: checkbox.value for name, checkbox in self.checkboxes.items()}
            input_values = {name: input.value for name, input in self.inputs.items()}
            event_times = {name: times.value for name, times in self.times.items()}

            s_start = self.times.get("eventStart_start").value
            s_end = self.times.get("eventStart_end").value
            e_start = self.times.get("eventEnd_start").value
            e_end = self.times.get("eventEnd_end").value
            timesEmpty = s_start == Select.BLANK or s_end == Select.BLANK or e_start == Select.BLANK or e_end == Select.BLANK


            class_name = self.inputs["class_name"].value
            class_name_exists = False
            if os.path.exists('classes.txt'):
                with open('classes.txt', 'r') as file:
                    for line in file:
                        if class_name == line.strip():
                            class_name_exists = True
                            break

            #check if class name already exists

            if(not class_name_exists and (class_name != "") and (self.inputs["class_location"].value != "") and (not timesEmpty)):
                data_to_save = {
                    "checkbox_states": checkbox_states,
                    "input_values": input_values,
                    "times": event_times
                }

                # You can process these states as needed here
                # print("Checkbox States:", checkbox_states)
                # print("Input Values:", input_values)
                with open('classes.txt', 'a') as file:
                    file.write(class_name)
                    file.write("\n")  # Add a newline for separation between entries
                with open('app_data.txt', 'a') as file:
                    json.dump(data_to_save, file)
                    file.write("\n")  # Add a newline for separation between entries
                self.exit("hello")



if __name__ == "__main__":
    app = InputClass()
    hello = app.run()
    print(hello) 

