
def main():
    filename = input("File name: ")
    filename = filename.strip().lower()

    check_file(filename)


def get_extension(file):
    return file.split(".")[-1]


def check_file(file):
    if get_extension(file) == "gif" or get_extension(file) == "png":
        print(f"image/{get_extension(file)}")
    elif get_extension(file) == "jpg" or get_extension(file) == "jpeg":
        print("image/jpeg")
    elif get_extension(file) == "pdf" or get_extension(file) == "zip":
        print(f"application/{get_extension(file)}")
    elif get_extension(file) == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")


main()