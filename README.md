# pytest-and-matplotlib-cryptobot_api

API cryptobot. This project contains cryptobot tha operates under api requisitions to do trading operations. All the necessary support documentation to develop this project is placed here. Requests library is used. It creates one .json file for each request so we can share data between different requests. The .json file is excluded after each test execution. 

# Pre-requirements:

| Requirement                     | Version        | Note                                                            |
| :------------------------------ |:---------------| :-------------------------------------------------------------- |
| Python                          | 3.12.5         | -                                                               |
| Visual Studio Code              | 1.89.1         | -                                                               |
| Python extension                | 2024.14.1      | -                                                               | 
| Pytest                          | 8.4.1          | -                                                               |
| matplotlib                      | 3.10.5         | -                                                               |
| requests                        | 2.32.4         | -                                                               |
| pytest-html                     | 4.1.1          | -                                                               |
          
# Installation:

- See [python page](https://www.python.org/downloads/) and download the latest Python stable version. Start the installation and check the checkboxes below: 
  - :white_check_mark: Use admin privileges when installing py.exe 
  - :white_check_mark: Add python.exe to PATH
and keep all the other preferenced options as they are.
- See [Visual Studio Code page](https://code.visualstudio.com/) and install the latest VSC stable version. Keep all the prefereced options as they are until you reach the possibility to check the checkboxes below: 
  - :white_check_mark: Add "Open with code" action to Windows Explorer file context menu. 
  - :white_check_mark: Add "Open with code" action to Windows Explorer directory context menu.
Check then both to add both options in context menu.
- Look for Python in the extensions marketplace and install the one from Microsoft.
- Open windows prompt as admin and execute ```pip install pytest``` to install Pytest.
- Open windows prompt as admin and execute ```pip install matplotlib``` to install matplotlib library.
- Open windows prompt as admin and execute ```pip install requests``` to install Requests library.
- Open windows prompt as admin and execute ```pip install pytest-html``` to install pytest-html plugin.

# Execute requisition:

- Execute ```pytest ./tests -v --html=./reports/report.html``` to run tests in verbose mode and generate a report inside reports folder.
- Execute ```pytest .\tests\api\cryptobot_api_test.py -v --html=./reports/report.html``` to run tests inside cryptobot_api_test.py file in verbose mode and generate a report inside reports folder.

# Support:

- [General API Information](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-api-information)
- [https://developers.coindesk.com/documentation/data-api/introduction](https://developers.coindesk.com/documentation/data-api/introduction)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Python – Call function from another file](https://www.geeksforgeeks.org/python-call-function-from-another-file/)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/latest/)
- [How to get the localStorage with Python and Selenium WebDriver](https://stackoverflow.com/a/46361890/10519428)
- [Python Requests Library Complete Tutorial - Rest API Testing](https://www.youtube.com/watch?v=LP8NlUYHQGg)
- [Python Accessing Nested JSON Data [duplicate]](https://stackoverflow.com/a/23306717/10519428)
- [Session Objects](https://requests.readthedocs.io/en/latest/user/advanced/#session-objects)
- [Write JSON data to a file in Python](https://sentry.io/answers/write-json-data-to-a-file-in-python/)
- [Read JSON file using Python](https://www.geeksforgeeks.org/read-json-file-using-python/)
- [Python | os.remove() method](https://www.geeksforgeeks.org/python-os-remove-method/)
- [Python String strip() Method](https://www.w3schools.com/python/ref_string_strip.asp)
- [Matplotlib 3.10.5 documentation - Home](https://matplotlib.org/stable/gallery/scales/index.html)
- [Matplotlib](https://pypi.org/project/matplotlib/)
- [ChatGPT](https://openai.com/chatgpt/)

# Tips:

- Although this is no sw test project, Pytest is used. Lets see how it behaves. 
- Trust ChatGPT.
