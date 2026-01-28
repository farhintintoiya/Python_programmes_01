

def b2mb_kb_gb(bytes) :

    KB = bytes / 1024
    MB = bytes / (1024 * 1024)
    GB = bytes / (1024 * 1024 * 1024)

    print(f"The {bytes} bytes are {KB} in Kilobytes.")
    print(f"The {bytes} bytes are {MB} in Megabytes.")
    print(f"The {bytes} bytes are {GB} in Gigabytes.")

bytes = int(input("Enter the bytes : "))

b2mb_kb_gb(bytes)

