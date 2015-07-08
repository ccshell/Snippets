from __future__ import with_statement
import gdb
class SavePrefixCommand(gdb.Command):
    "Prefix command for saving things."

    def __init__(self):
        super(SavePrefixCommand, self).__init__(
                "save",
                gdb.COMMAND_DATA,
                gdb.COMPLETE_NONE, True)

SavePrefixCommand()

class SaveBreakpointsCommand(gdb.Command):
    """Save the current breakpoints to a file.

This command takes a single argument,a file name.
The breakpoints can be restored using the 'source' commmand."""

    def __init__(self):
        gdb.Command.__init__(self,
                "save breakpoints",
                gdb.COMMAND_DATA,
                gdb.COMPLETE_FILENAME)

    def invoke(self, arg, from_tty):
        with open(arg, 'w') as myfile:
            for breakpoint in gdb.breakpoints():
                try:
                    print >> myfile, "break", breakpoint.location,
                    if breakpoint.thread is not None:
                        print >> myfile, " thread", breakpoint.thread,
                    if breakpoint.condition is not None:
                        print >> myfile, " if", breakpoint.condition,
                    print >> myfile
                    if not breakpoint.enabled:
                        print >> myfile, "disable break" , breakpoint.number
                    if breakpoint.commands is not None:
                        print >> myfile, "commands"
                        print >> myfile, breakpoint.commands,
                        print >> myfile, "end"
                    print >> myfile
                except RuntimeError as e:
                    print "a"

SaveBreakpointsCommand()

