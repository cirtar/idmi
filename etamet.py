def my_function(callback_on_step_end=None):
    # Perform some steps or iterations
    for step in range(10):
        # Do something
        # Call the callback function at the end of each step
        if callback_on_step_end is not None:
            callback_on_step_end(step)
