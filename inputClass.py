from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog
from textual import on
from textual.app import App, ComposeResult
from textual.validation import Function, Number, ValidationResult, Validator
from textual.widgets import Input, Label, Pretty, Static, Checkbox, Select
from textual.containers import VerticalScroll
import json

from term_bg import query_terminal, parse_rgb_value

# this file will open a text input box that asks
# class name, class time, checkbox for days of the week, location

# make a generic checkbox function and a generic text input function
# store the state of the checkbox in an array in this format ["M", "W", "F""] where the array 
# store the state of the text input in an array in this format ["inputName": "currentInput"]
# whenever the submit button is pressed all of these states should be captured 

# Ai notebook

class InputApp(App):
    """App to display key events."""
    bg_rgb = ""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.checkboxes = {}
        self.class_time = {}
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
            yield Select(hour_options)
            yield Label("Minute")
            yield Select(minute_options)

        yield Label("End time")
        with VerticalScroll():
            yield Label("Hour")
            yield Select(hour_options)
            yield Label("Minute")
            yield Select(minute_options)



    def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            # Capture the states of checkboxes and inputs
            # print(self.checkboxes)

            checkbox_states = {name: checkbox.value for name, checkbox in self.checkboxes.items()}
            input_values = {name: input.value for name, input in self.inputs.items()}

            data_to_save = {
                "checkbox_states": checkbox_states,
                "input_values": input_values
            }

            # You can process these states as needed here
            # print("Checkbox States:", checkbox_states)
            # print("Input Values:", input_values)
            with open('app_data.txt', 'a') as file:
                json.dump(data_to_save, file)
                file.write("\n")  # Add a newline for separation between entries

            self.exit()

def run_app():
    app = InputApp()
    app.run()

if __name__ == "__main__":
    app = InputApp()
    app.run()

