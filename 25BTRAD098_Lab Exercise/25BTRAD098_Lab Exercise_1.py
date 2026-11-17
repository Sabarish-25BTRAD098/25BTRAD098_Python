#Lab Exercise 1: Installing Python, VS Code / PyCharm, and Jupyter Notebook
'''Windows
Step 1: Download the Python Installer via Chrome
1. Open Google Chrome.
2. Navigate to the official website: python.org/downloads.
3. Click the yellow "Download Python" button to download the latest installer .exe file.
4. Once downloaded, click the file directly from Chrome's download bar (top right) or press Ctrl + J
and click "Show in folder" to locate the file in your Downloads folder.
Step 2: Run the Installer
1. Double-click the downloaded file (e.g., python-3.x.x-amd64.exe).
2. Crucial Step: At the bottom of the installation window, check the box that says "Add python.exe to
PATH".(Skipping this step will make it difficult to run Python from the Command Prompt).
3. Check "Install launcher for all users".
4. Click "Install Now".
Step 3: Verify the Installation
1. Press Win + R, type cmd, and press Enter to open the Command Prompt.
2. Type the following command and hit Enter:
“python --version”
3. If installed correctly, it will display your installed version (e.g., Python 3.12.x).
Setting up Visual Studio Code
1. Install VS Code
• Windows: Download the User Setup installer (.exe) from code.visualstudio.com. Run the file and
accept the defaults.
• macOS: Download the .zip/.dmg installer. Drag Visual Studio Code.app into your Applications
folder.
• Linux: Download the .deb (Debian/Ubuntu) or .rpm (Fedora/RHEL) package and install it via your
package manager (sudo apt install ./*.deb).
2. Terminal Setup (code .)
To open any project folder directly from your command line:
• Mac: Open VS Code → Press Cmd+Shift+P to open the Command Palette → Type Shell
Command: Install 'code' command in PATH \rightarrow Press Enter.
• Windows/Linux: The installer configures this automatically. Open your terminal, navigate to a
folder, and run code .
3. Essential First Customizations
• Install Extensions: Click the Extensions icon on the left sidebar (Ctrl+Shift+X or Cmd+Shift+X).
Recommended starting extensions:
• Language Support: Install Python, C/C++, Prettier (Formatter), or ESLint depending on your
stack.
• Git / Source Control: Built-in, but tools like GitLens add line-by-line history.
• Turn on Auto Save: Go to File → Auto Save.

• Set Up AI Assistance (Optional): Click the Copilot icon in the bottom status bar or press
Ctrl+Alt+I (Cmd+Alt+I on Mac) to enable GitHub Copilot or sign in with your provider.
4. Open Your First Project
Go to File → Open Folder (Ctrl+K Ctrl+O or Cmd+K Cmd+O), select your project directory, and
create a new file (Ctrl+N) to start coding.
Visual Studio'''

#Lab Exercise 2: Write and Execute a Basic Python Program 

#Code:
print("Hello, World!")
print("Welcome to Python Programming.")

#Lab Exercise 3: Programs Using Variables, Operators, and Input/Output
#Code:
# Input/Output and Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Basic Arithmetic Operators
next_year_age = age + 1
double_age = age * 2
# Output using formatted string (f-string)
print(f"\nHello, {name}!")
print(f"You are currently {age} years old.")
print(f"Next year, you will be {next_year_age} years old.")
print(f"Twice your age is {double_age}.")

#Lab Exercise 4: Simple Calculator and Area Calculation Programs
#Part A: Simple Calculator
#Code:
# Simple Calculator
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Performing calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
# Displaying results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
