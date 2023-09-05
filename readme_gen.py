import os

def write():
    # reading a file named base.txt
    with open("base.txt", "r") as f:
        content = f.read()
    # writing the content of base.txt to README.md
    with open("README.md", "w") as f:
        f.write(content)
    
    # new line x 2
        f.write("\n")
        f.write("\n")

    # recursively read all files in source directory
    for root, dirs, files in os.walk("source"):
        for file in files:
            # reading a file named file
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
            # appending the content of file to README.md
            with open("README.md", "a") as f:
                f.write(f"## {file[:-4]}\n")
                for i in content.split("\n"):
                    if i == "":
                        continue
                    f.write(f"- {i}\n")
                # f.write(f"- {content}")
            # new line x 1
                f.write("\n")
    
    # reading a file named footer.txt
    with open("footer.txt", "r") as f:
        content = f.read()
    # appending the content of footer.txt to README.md
    with open("README.md", "a") as f:
        f.write(content)

if __name__ == "__main__":
    write()