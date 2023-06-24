import subprocess
import sys
import platform

def install_python():
    if platform.system() != "Windows":
        print("Python installation is currently supported only on Windows.")
        return

    try:
        import sysconfig
    except ImportError:
        print("Python installation requires internet access.")
        return

    python_version = "3.11.2"
    python_url = f"https://www.python.org/ftp/python/{python_version}/python-{python_version}-embed-amd64.zip"

    subprocess.check_call(["powershell.exe", "-Command", f"(New-Object System.Net.WebClient).DownloadFile('{python_url}', 'python.zip')"])
    subprocess.check_call(["powershell.exe", "-Command", "Expand-Archive -Path python.zip -DestinationPath ."])

    python_path = sysconfig.get_paths()["purelib"]
    subprocess.check_call(["powershell.exe", "-Command", f"Copy-Item -Path 'python-{python_version}-embed-amd64/*' -Destination '{python_path}' -Recurse -Force"])
    subprocess.check_call(["powershell.exe", "-Command", "Remove-Item -Path 'python.zip', 'python-*' -Force"])

    print("Python installed successfully.")

def install_dependencies():
    dependencies = [
        "tk",
        "matplotlib",
        "pandas",
        "numpy",
        "scikit-learn"
        
    ]

    for dependency in dependencies:
        subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])

    print("Dependencies installed successfully.")

# Install Python if not already installed
try:
    import sysconfig
except ImportError:
    install_python()

# Install dependencies using pip
install_dependencies()

