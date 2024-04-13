import pkgutil
import os

def is_importable(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def list_resolvable_packages_and_modules(directory, prefix='', indent=0):
    for importer, package_name, _ in pkgutil.iter_modules([directory]):
        full_path = os.path.join(directory, package_name)
        if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, '__init__.py')):
            if is_importable(prefix + package_name):
                print('  ' * indent + package_name + ' (package)')
                list_resolvable_packages_and_modules(full_path, prefix + package_name + '.', indent + 1)
        elif os.path.isfile(full_path + '.py'):
            if is_importable(prefix + package_name):
                print('  ' * indent + prefix + package_name + ' (module)')

if __name__ == "__main__":
    project_directory = "."
    print("Resolvable local packages and modules:")
    list_resolvable_packages_and_modules(project_directory)
