import requests
import csv
from datetime import datetime, timedelta

# List of package names
packages = [
    'numpy',
    'pandas',
    'matplotlib',
    'requests',
    'beautifulsoup4',
    'scikit-learn',
    'tensorflow',
    'flask',
    'django',
    'scipy',
    'pillow',
    'opencv-python',
    'seaborn',
    'sqlalchemy',
    'plotly',
    'nltk',
    'jupyter',
    'pygame',
    'sympy',
    'pytorch',
    'pyqt5',
    'networkx',
    'tweepy',
    'flask-restful',
    'pyyaml',
    'openpyxl',
    'pyinstaller',
    'flask-login',
    'django-rest-framework',
    'wtforms',
    'pytest',
    'pyodbc',
    'docopt',
    'pytest-cov',
    'pytz',
    'boto3',
    'pyglet',
    'paramiko',
    'bokeh',
    'django-crispy-forms',
    'pyjwt',
    'python-dateutil',
    'pycrypto',
    'scrapy',
    'tqdm',
    'pyserial',
    'sphinx',
    'flask-wtf',
    'opencv-python-headless',
    'plotly-geo'
]

# Create a CSV file
csv_file = open("package_data.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Package Name", "Release Date", "Python Version", "Downloads (Last Month)"])

# Retrieve data for each package
for package in packages:
    # Make a request to the PyPI API
    api_url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(api_url)
    data = response.json()

    # Get the latest release information
    releases = data["releases"]
    latest_release = releases[max(releases)]
    release_date = latest_release[0]["upload_time"]
    python_version = latest_release[0]["python_version"]
    downloads_last_month = data["info"]["downloads"]["last_month"]

    # Write the data to the CSV file
    csv_writer.writerow([package, release_date, python_version, downloads_last_month])

# Close the CSV file
csv_file.close()

print("CSV file created successfully!") 