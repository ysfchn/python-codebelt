# Python Codebelt
#
# Progress Bar
# Yusuf Cihan (@ysfchn)
#
# Prints a progress bar in console for your tasks.
# Example result:
# █████░░░░░ %50 - 5 / 10
#
# Inputs (5):
# progress : int -- Current progress value in units, needs to be smaller than total value. 
# total : int    -- Total progress value in units, needs to be greater than progress value. 
# size : int     -- Length of the progress bar. Default is 40 characters long.
# filled : str   -- Character that will be used for filled side of progress bar. Default is "█"
# empty : str    -- Character that will be used for empty side of progress bar. Default is "░"

def progress_bar(progress : int, total : int, size : int = 40, filled : str = "█", empty : str = "░", showpercent : bool = True):
    # Create a empty progress bar.
    bar = empty * size
    # Calculate the percent.
    percent = (progress / total) * 100
    # Build the progress bar.
    bar = bar.replace(empty, filled, int(percent / (100 / size)))
    # If showpercent is True, display the percent value too.
    if showpercent:
        bar = "{0}   %{1} - {2} / {3}".format(bar, percent, progress, total)
    return bar