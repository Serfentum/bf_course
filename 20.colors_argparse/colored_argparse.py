import sys
import argparse


class ColoredArgParser(argparse.ArgumentParser):
    """
    Subclass of ArgumentParser
    Enable  colored text printing
            capital letters in help sections

    First number - color, second - mode
    Look here for information http://jafrog.com/2013/11/23/colors-in-terminal.html
    # Colors
    30 - black
    31 - red
    32 - green
    33 - yellow
    34 - blue
    35 - magenta
    36 - cyan
    37 - white
    # Modes
    1 - bold
    3 - italics
    4 - underline
    """
    color_dict = {'usage': '33;1', 'help': '35;1', 'error': '31;1', 'version': '36;1'}


    def format_help(self):
        # Usage doesn`t add to help text automatically, it is printed separately lower
        formatter = self._get_formatter()
        formatter.add_text(self.description)
        # positionals, optionals and user-defined groups
        for action_group in self._action_groups:
            formatter.start_section(action_group.title[0].upper() + action_group.title[1:])
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()
        # epilog
        formatter.add_text(self.epilog)
        # determine help from format above
        return formatter.format_help()

    def print_usage(self, file=None):
        if file is None:
            file = sys.stdout
        self._print_message(self.format_usage()[0].upper() +
                            self.format_usage()[1:],
                            file, self.color_dict['usage'])

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        self._print_message(self.format_usage()[0].upper() +
                            self.format_usage()[1:],
                            file, self.color_dict['usage'])
        file.write('\n')
        self._print_message(self.format_help()[0].upper() +
                            self.format_help()[1:],
                            file, self.color_dict['help'])

    def _print_message(self, message, file=None, color=None):
        if message:
            if file is None:
                file = sys.stderr
            # Print messages in bold, colored text if color is given
            if color is None:
                file.write(message)
            else:
                # \x1b[ is an escape character, m for command terminating, \x1b[0m for "endtag"
                file.write('\x1b[{col}m{stdout}\x1b[0m\n'.format(col=color, stdout=message.strip()))

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, sys.stderr, self.color_dict['error'])
        sys.exit(status)

    def error(self, message):
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(2, 'Error: {0[prog]}\n{0[message]}\n'.format(args))



