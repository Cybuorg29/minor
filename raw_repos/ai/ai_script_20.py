def get_module_lines(module):
    """
    Returns the number of lines of code in a given module,
    using the inspect module.
    """
    import inspect
    sourcelines = inspect.getsourcelines(module)
    line_count = len(sourcelines[0])
    return line_count