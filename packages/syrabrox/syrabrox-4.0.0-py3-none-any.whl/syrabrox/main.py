import os
import traceback
def errorlaw(exception, intents, logFile="Error_Logs.txt"):
    error_details = []
    if '1' in intents: 
        error_details.append(f"Error Type: {type(exception).__name__}")
    if '2' in intents: 
        error_details.append(f"Error Message: {str(exception)}")
    if '3' in intents:  
        error_details.append(f"File Name: {os.path.basename(__file__)}")
    if '4' in intents:
        error_details.append(f"Full Path: {os.path.abspath(__file__)}")
    if '5' in intents:
        tb = traceback.extract_tb(exception.__traceback__)[-1]
        filename, lineno, funcname, text = tb
        error_details.append(f"Line Number: {lineno}")
    if '6' in intents:
        error_details.append(f"Traceback: {traceback.format_exc()}")
    log_entry = "\n".join(error_details)
    if '7' in intents: 
        with open(logFile, "w") as log_file:
            log_file.write(log_entry + "\n" + "="*50 + "\n")
    if '8' in intents:
        print(log_entry)
    if '9' in intents:
        return log_entry