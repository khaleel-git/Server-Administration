import psutil

# Get a list of all running processes
processes = psutil.process_iter()

# Initialize a list to store the PIDs of PHP processes
php_pids = []

# Loop through each process and check if it is a PHP process
for process in processes:
    try:
        # Get the process information as a named tuple
        process_info = process.as_dict(attrs=['pid', 'name'])

        # Check if the process name contains "php"
        if 'php' in process_info['name']:
            php_pids.append(process_info['pid'])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # If there is an error getting the process information, skip it
        continue

# Initialize a variable to store the total memory usage in bytes
total_memory_usage = 0

# Loop through each PHP PID and get the memory usage in bytes
for pid in php_pids:
    try:
        # Get the process memory information as a named tuple
        memory_info = psutil.Process(pid).memory_info()

        # Add the memory usage to the total
        total_memory_usage += memory_info.rss
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # If there is an error getting the process memory information, skip it
        continue

# Convert the total memory usage to MB and print it
print(f"Total PHP memory usage: {total_memory_usage / (1024 * 1024):.2f} MB")
