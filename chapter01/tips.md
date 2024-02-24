# Tips and Resources
Copilot tips and resources


## Useful Official GitHub Copilot Links


> [Official Github Copilot Documentation](https://docs.github.com/en/copilot)

> [Getting Started with Copilot Editor Extensions](https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot)

> [Getting Started with Copilot Chat Editor Extensions](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide)


## Copilot Help
In Copilot and Copilot Chat, using the `/help` slash prompt can give a wealth of useful information and start a useful dialog.

## Useful Copilot Techniques

#### Open a source file, write a comment description of what you want, type `<ENTER>`, and a suggestion should appear on the following line.
- If you like the suggestion, hit `<TAB>` on the keyboard to accept.
- If the suggestion is unacceptable and you want to type something else, type `<ESC>` on the keyboard to decline the suggestion. Then, you may continue typing.
- If no suggestion appears, or the suggestion disappears, and you want it back, then hit `<ALT> + \` on the keyboard; if there is a suggestion, it will appear.
- When there are multiple suggestions, to view them, type `<ALT>+]` or `<ALT>+[` to cycle left and right through them. Also, you can mouse over the suggestion to see more.
- If you want to view multiple suggestions in a new editor tab, type `<CTRL> + <ENTER>` to open a new tab and review the generated suggestions.

#### Copilot Reference
- Open files are used as `context` for Copilot in other open files.
- Only open files are used for context reference.
- File in the project IDE, but not opened, are not used for referencing inline suggestions, fixes or other language specific interaction with Copilot.
- You can prefix your prompt with `@workspace` scope agents to give copilot directives to reference the current workspace.
- Scopes/Agents will not work in comment oriented suggestions and prompting.

## Useful Copilot Chat Techniques
- To open a chat session to discuss a code snippet, highlight the code in the editor and type `<CTRL>+i` on Windows and Linux and `<CMD>+i` on macOS.
- If you do not understand some lines of code, highlight them, right-click, and select Copilot -> Explain This from the context menu.
- If you want to fix some lines of code, highlight them, right-click, and choose Copilot -> Fix This from the context menu.
- To get help within Copilot Chat, open the chat panel, type in /help, and then hit `<ENTER>`. A good summary of available Copilot Chat commands will appear.
- `/help` is useful to get helpful information
- `@<SOME SCOPE>` handles your prompts within a scope; there are three scopes: `@workspace`, `@vscode`, and `@terminal`
    - `@workspace` is for creating new projects and managing existing projects.
        - `/explain` is useful for a detailed description of a section of code.
        - `/tests` Generate unit tests for the selected code.
        - `/fix` Propose a fix for the problems in the selected code.
        - `/new` Scaffold code for a new workspace.
        - `/newNotebook` Create a new Jupyter Notebook.
    - `@vscode` is for editor configuration and managing extensions.
    - `@terminal` is for running commands in the terminal.



## Prompts and Suggestions
### Q: What data does Copilot send in the prompts to the GitHub Copilot servers?
A: Copilot sends the code and comments that you are editing and the relevant surrounding context. Surrounding context includes the current file and other files opened in the editor.

### Q: What data is retained by GitHub?
A: GitHub deletes prompt data after making the suggestion, and GitHub does not store the suggestion after making it. GitHub stores user interaction data for 24 months. GitHub uses this data to improve the Copilot service, not the training AI model. GitHub trains the generative AI model with public source code, not code from private repositories.

---

# Other tricks and prompts in Copilot

## Select an error message on the terminal:
- Select error message such as `HERE`, and ask copilot to `explain this`.
- You can then tell copilot `but its not working`.


```text
/fix
```


---

# Other tricks and prompts in Copilot Chat

## The upper right of code snippets, you can:
- Copy
- Insert at Curser (^Enter)
- Select the three elipses to either:
    - Insert into New File
    - Insert into Terminal


---

> See: [Copilot Tip's](./qa.md)


---

#### [./back](./README.md)
