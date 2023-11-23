import re
import os 
import termios
import tty

def query_terminal(sequence):
    with open('/dev/tty', 'wb+', buffering=0) as tty_file:
        fd = tty_file.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Switch to non-canonical mode
            tty.setraw(fd)

            tty_file.write(sequence.encode())
            tty_file.flush()

            # Read the initial bytes (often control characters)
            tty_file.read(2)

            # Read enough bytes to get the response
            response = tty_file.read(21)
        finally:
            # Restore the terminal to its original settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return response.decode()


def convert_color(hex_value):
    # Convert from four-digit hex to two-digit hex
    val = int(hex_value, 16)  # Convert to integer
    scaled_val = int((val / 65535) * 255)  # Scale the value
    return format(scaled_val, '02x')  # Convert back to hex


def parse_rgb_value(input_string):
    # Regular expression pattern to match the rgb value
    pattern = r'rgb:([0-9a-fA-F]{4})/([0-9a-fA-F]{4})/([0-9a-fA-F]{4})'
    match = re.search(pattern, input_string)
    if match:
        # Extract and convert each RGB component
        red, green, blue = match.groups()
        return f"#{convert_color(red)}{convert_color(green)}{convert_color(blue)}"
    else:
        return None
