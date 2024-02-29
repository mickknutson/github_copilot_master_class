# GitHub Copilot CLI Extension Tutorial

GitHub Copilot is an AI pair programmer that helps you write code faster and with less work. The `gh-copilot` CLI extension brings the power of GitHub Copilot directly to your terminal, allowing you to generate code, comments, and even entire functions quickly through the command line interface.

## Prerequisites

Before installing the `gh-copilot` CLI extension, you must have the following:
- GitHub CLI (`gh`) installed on your machine. If you don't have GitHub CLI installed, visit [GitHub CLI documentation](https://cli.github.com/manual/installation) for installation instructions.
- An active GitHub account.
- GitHub Copilot subscription or GitHub Copilot trial activated for your GitHub account. Visit [GitHub Copilot](https://copilot.github.com/) for more information.

## Installation

1. **Open your terminal.**

2. **Install the `gh-copilot` extension** by running the following command:

    ```bash
    gh extension install github/gh-copilot
    ```

This command downloads and installs the `gh-copilot` extension directly from GitHub.


1. **Setting aliases**:
   Command line aliases can be created in `.aliases` or `.zshrc` file:

    ```bash
    # Github and Copilot
    alias copilot='gh copilot'
    alias gcs='gh copilot suggest'
    alias gce='gh copilot explain'
    ```

This command downloads and installs the `gh-copilot` extension directly from GitHub.


---
# Usage

After installing the `gh-copilot` extension, you can start using it to generate code snippets, entire functions, or other code constructs directly from your command line.


## Suggestions

- **Suggestions**

    Ask copilot for suggested for a command in natural language.

    ```bash
    gh copilot suggest -t git "Undo the most recent local commits"
    ```

- **Suggestion Result:**
    ```
    Suggestion:
        git reset --hard HEAD~1
        
        ? Select an option  [Use arrows to move, type to filter]
        > Copy command to clipboard
        Explain command
        Revise command
        Rate response
        Exit
  ```

This command asks GitHub Copilot suggest can target `shell`, `gh`, `git`.


- **More Suggestion Examples:**
    ```
    Examples:

    - Guided experience
    $ gh copilot suggest

    - Git use cases
    $ gh copilot suggest -t git "Undo the most recent local commits" 
    $ gh copilot suggest -t git "Clean up local branches" 
    $ gh copilot suggest -t git "Setup LFS for images" 

    - Working with the GitHub CLI in the terminal
    $ gh copilot suggest -t gh "Create pull request"
    $ gh copilot suggest -t gh "List pull requests waiting for my review"
    $ gh copilot suggest -t gh "Summarize work I have done in issues and pull requests for promotion"

    - General use cases
    $ gh copilot suggest -t shell "Kill processes holding onto deleted files"
    $ gh copilot suggest -t shell "Test whether there are SSL/TLS issues with github.com"
    $ gh copilot suggest -t shell "Convert SVG to PNG and resize"
    $ gh copilot suggest -t shell "Convert MOV to animated PNG"
    ```



### Explaination

- **Explaination:** Explain a given input command in natural language.

    ```bash
    gh copilot explain 'git log --oneline --graph --decorate --all'
    ```

- **Explaination Result:**
    ```
    Explanation:                       
    • git log shows the commit history of the repository.
    • --oneline shows each commit on a single line with a condensed format.
    • --graph displays an ASCII art representation of the commit history graph.
    • --decorate adds additional information to the commit output, such as branch and tag names.
    • --all shows commits from all branches, not just the current branch.  
  ```



- **More Explaination Examples**
    ```
    Examples:

    # View disk usage, sorted by size
    $ gh copilot explain 'du -sh | sort -h'

    # View git repository history as text graphical representation
    $ gh copilot explain 'git log --oneline --graph --decorate --all'

    # Remove binary objects larger than 50 megabytes from git history
    $ gh copilot explain 'bfg --strip-blobs-bigger-than 50M'
    ```



### Start a Copilot session

  ```sh
  gh copilot
  ```

  This command initiates a Copilot session in your terminal. You can start typing your comments or questions, and Copilot will provide suggestions or answers based on the context.


### Options

The `gh-copilot` CLI offers several options to customize the code generation process, including specifying the programming language, the number of suggestions, and more. For a full list of options, run:

```bash
gh copilot --help
```





--- 
# Notes
> 

---

#### [../back](../README.md)
