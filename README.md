# SE-assignment2 - GitHub Project
# Project Description
This project is a comprehensive demonstration of GitHub version control techniques, including repository setup, branching, merging, resolving conflicts, and collaboration using pull requests. It also covers best practices for documentation and issue tracking. The program prompts the user for input and returns a greeting message. It serves as a foundational project for understanding distributed version control systems.
# Installation Instructions
Follow these steps to set up the project on your local machine:
# Step 1: Prerequisites
Ensure you have the following installed:
•	Git (Download Git)
# Step 2: Clone the Repository
Open a terminal or Git Bash and run:
 git clone https://github.com/your-username/SE-assignment2.git
This will download the repository to the local machine.
# Step 3: Navigate to the Project Directory
Move into the cloned project folder:
cd SE-assignment2
# Step 4: Check Out the Main Branch
Ensure you are on the latest version of main:
git checkout main
git pull origin main

# Step 5: Verify Git Configuration 
Ensure your Git configuration is set up correctly:
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Usage Examples
# Example 1: Running the Program

User Input:
Enter your name: Alice
Output:
Hello, Alice!

# Example 2: Handling Empty Input

User Input:
Enter your name:   
Output:
Name cannot be empty. Please try again.
Enter your name: Bob
Hello, Bob!

# Example 3: Checking Git Status
To check the status of your repository:
git status

# Example 4: Committing Changes
To commit and push changes:
git add .
git commit -m "Updated hello.py with improved input validation"
git push origin main

# Advanced Git Commands

# Branch Management
•	Create a new branch: 
•	git checkout -b new-feature
•	Switch branches: 
•	git checkout main
•	Delete a local branch: 
•	git branch -d old-feature

# Rebasing
•	Rebase feature branch onto main: 
•	git checkout feature-branch
•	git rebase main

# Troubleshooting Guide
# Issue & Solution
Git is not recognized:	Ensure Git is installed and added to system PATH
Merge conflicts occur:	Manually resolve conflicts and commit changes

# Future Improvements
•	Implement additional features such as saving user input.
•	Add multi-language support for greetings.

# Best Practices Followed
*•Version Control: Git-based workflow using feature branches and pull requests.
•	Collaboration: Issues and PR reviews ensure quality contributions.
•	Documentation: Proper README and commit messages for maintainability.
•	Error Handling: Basic input validation prevents invalid inputs.
•	Modularity: Code structure is clean and easily extensible.
•	Security: Avoids hardcoding sensitive data.

# Contributors
•	Name: Jafin Khan



