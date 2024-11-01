import subprocess

# Command to execute
command = "ls"

# Execute the command
result = subprocess.run(command, capture_output=True, text=True)

# Get stdout
stdout = result.stdout


def size_of_drive(safe_drive_name):
    result = subprocess.run(
        "blockdev --getsize64 /dev/sda", capture_output=True, shell=True
    )
    return int(result.stdout)
