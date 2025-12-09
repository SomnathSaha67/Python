with open("log.txt", "w") as file:
    file.write("This log file has been overwritten using write mode 'w'.\n")
    file.write("All previous content has been deleted.\n")
    file.write("New log entries can be added from this point onward.\n")
    file.write("End of log.\n")
