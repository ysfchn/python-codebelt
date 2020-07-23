# Progress Bar
Prints a progress bar in console for your tasks.<br>_by [@ysfchn](https://github.com/ysfchn)_

## Input
### progress `int`
Current progress value in units, needs to be smaller than total value. 
### total `int`
Total progress value in units, needs to be greater than progress value. 
### size `int`
Length of the progress bar. Default is 40 characters long.
### filled `str`
Character that will be used for filled side of progress bar. Default is "█"
### empty `str`
Character that will be used for empty side of progress bar. Default is "░"

## Output
Generates a progress bar as `str`.

## Usage
```py
progress = progress_bar(50, 100)
print(progress)

# Output:
# ████████████████████░░░░░░░░░░░░░░░░░░░░ %50 - 50 / 100
```
