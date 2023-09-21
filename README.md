# Password-manager
This is a simple Password Manager application built using Python and the tkinter library. The application allows users to generate random passwords, store them along with website details, and retrieve stored passwords when needed.

# Getting Started

# Prerequisites
1) Python (3.x recommended)
2) tkinter library (usually included with Python)

# Installation 

1. Clone the repository to your local machine: https://github.com/Hemang648/password-manager.git
2. Navigate to the project directory: cd password-manager
3. Run the application: python password_manager.py

# Usage 
## Generating Passwords
* Click the "Generate Password" button to create a random password.
* You can customize the length and complexity of the generated password by modifying the code in the 'gen()' function.

## Storing Passwords
* Enter the website name, email/username, and password
* Click the "Add" button to save the details.
* The data is stored in a JSON file named "data.json".

## Retrieving Passwords
* Enter the website name and click the "Search" button to retrieve saved details
* If the website details are found, the email/username and password will be displayed.
* If no details are found for the given website, an error message will be displayed.

## Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository and create a pull request. If you encounter any issues or have questions, please open an issue on GitHub.
