ToDo List
=========

-   [ ] Multi-character short codes, so you can say `command -d1`, `command -fex`, etct.

-   [ ] Separate CmdLine into its own repository

-   [ ] \@CmdLine with no args doesn't have the one-char flag, only the
    function-name -- flag

-   [ ] \@CmdLine print the name or docstring of its command when it runs.

-   [ ] Figure out how to install "betools" command-line command for both
    windows and mac using pip install (a useful piece of research in itself)

-   [ ] Command just spews out a framework code file

-   [ ] Option **run()** argument: default command if no flags are used

-   [ ] More complete docs and tests

-   [ ] Support for cleaning/creating/cloning/populating a target directory (one
    that is rebuilt from scratch)

-   [ ] timestamp-based and/or comparison-based dependency management (tells you
    if something needs to be rebuilt). Seems like there might already exist a
    library to do this.

-   [ ] BuildDirectory class. You give it a name, and it makes sure that dir exists.
        You can cd to the BuildDirectory (maybe it's a Path object?). You can "sweep()"
        all the files out of the BuildDirectory, and "remove()" it.

-   [ ] DirectEdit context manager. Modify a file as if it's a text object. Writes and
        Closed the file automatically. Requires some overloading or inherit from an io object.


