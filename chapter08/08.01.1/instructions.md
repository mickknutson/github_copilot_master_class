
# How to Install and Use the GitHub CLI

## Step 1: Download the GitHub CLI

- **For Windows:** Visit the GitHub CLI release page at `https://github.com/cli/cli/releases` and download the latest `.msi` installer for Windows.
- **For macOS:** You can install the GitHub CLI using Homebrew with the command `brew install gh`.
- **For Linux:** Depending on your distribution, you can use one of the package managers. For example, on Ubuntu/Debian, you can use `sudo apt install gh`.

## Step 2: Install the GitHub CLI

- **Windows:** Run the downloaded `.msi` file and follow the installation prompts.
- **macOS/Linux:** If you're using Homebrew or a package manager, the installation command provided above will also handle the installation process.

## Step 3: Authenticate with GitHub

- Open your terminal or command prompt.
- Type `gh auth login` and press Enter.
- Follow the on-screen instructions to authenticate. You'll have the option to authenticate via a web browser or by entering a token directly.

## Step 4: Basic GitHub CLI Commands

- **Clone a repository:** `gh repo clone <repository>`
- **Create an issue:** `gh issue create`
- **View open issues:** `gh issue list`
- **Create a pull request:** `gh pr create`
- **Check out a pull request locally:** `gh pr checkout <number>`

## Step 5: Explore Advanced Features

The GitHub CLI offers a wide range of commands that allow you to interact with issues, pull requests, repositories, and more, right from your terminal. Use `gh help` to discover more commands and how to use them effectively.

## Getting Help

For more detailed information about a specific command, use `gh help <command>`. For example, `gh help pr` will provide detailed information about pull request commands.

## Conclusion

The GitHub CLI is a powerful tool that simplifies GitHub workflows directly from your terminal. By following the steps above, you should now have the GitHub CLI installed and be familiar with some basic commands to get started. As you become more comfortable, explore the CLI's advanced features to fully leverage its capabilities.


---
# Reference Manual
> See [Official GitHub CLI manual](https://cli.github.com/manual/)
>
> See [GitHub CLI Extensions](https://github.com/topics/gh-extension)
>
> * [Github Extension: Branch Management](https://github.com/joaom00/gh-b)


--- 
# Notes


---

#### [../back](../README.md)
