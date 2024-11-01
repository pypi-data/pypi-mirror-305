# SyraBroX - Libarys
## ErrorLaw
The `errorlaw` function logs error details based on specified intents. It can log messages to a file, print them to the console, or return the details as a string.

### Function Signature
```python
def errorlaw(exception, intents, filename="Error_Logs.txt"):
```
## Parameters
#### exception (Exception): 
- The exception object to retrieve error details from.
#### intents (str): 
- A string of numbers, each specifying an action to include in the output.
#### filename (str, optional): 
- Log file name if intent '7' is set (default: "Error_Logs.txt").
## Intents
Each character in intents represents a type of error information to include:

- '1': Error type (type(exception).__name__)
- '2': Error message (again)
- '3': File name where the exception occurred
- '4': Full path of the script
- '5': Line number where the error occurred
- '6': Full traceback
- '7': Append log to file (filename)
- '8': Print log to console
- '9': Return log as a string
## Returns
Returns the log as a string if intent '9' is set, otherwise None.
## Example Usage
```python
try:
    1 / 0
except Exception as e:
    errorlaw(e, "123456789", "file_name.txt (optional)")
```
This captures various error details, saves to a file, prints, and returns the log entry.

## Requirements
Ensure __os__ and __traceback__ libraries are imported.

<details>
<summary>License</summary>
Copyright 2024 SyraBroX

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</details>