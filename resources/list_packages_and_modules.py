import pkgutil
import os

def list_packages_and_modules(directory, depth=0):
    for importer, package_name, _ in pkgutil.iter_modules([directory]):
        print("|   " * depth + "|-- " + package_name)
        full_path = os.path.join(directory, package_name)
        if os.path.isdir(full_path):
            list_packages_and_modules(full_path, depth+1)

if __name__ == "__main__":
    directory_path = "."
    print(directory_path)
    list_packages_and_modules(directory_path)
