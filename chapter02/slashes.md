# Chapter 02.03: Slash Commands
Slash Commands


## Useful Copilot Chat Slash Commands
- `@<SOME SCOPE>` handles your prompts within a scope; there are three scopes: `@workspace`, `@vscode`, and `@terminal`
    - `@workspace` is for creating new projects and managing existing projects.
        - `/explain` is useful for a detailed description of a section of code.
        - `/tests` Generate unit tests for the selected code.
        - `/fix` Propose a fix for the problems in the selected code.
        - `/new` Scaffold code for a new workspace.
        - `/createWorkspace` Create a new workspace.
        - `/newNotebook` Create a new Jupyter Notebook.
        - `/doc` Create documentation.
    - `@vscode` is for editor configuration and managing extensions.
    - `@terminal` is for running commands in the terminal.



## Slash Commands for common tasks[*](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices//#13-slash-commands-for-common-tasks)

[Slash commands](https://github.blog/changelog/2024-01-30-code-faster-and-better-with-github-copilots-new-features-in-visual-studio/#slash-commands) are awesome, and there are quite a few of them. We have commands to help you explain code, fix code, create a new notebook, write tests, and many more. They are just shortcuts to common prompts that we’ve found to be particularly helpful in day-to-day development from our own internal usage.

<table><tbody><tr><td><strong>Command</strong></td><td><strong>Description</strong></td><td><strong>Usage</strong></td></tr><tr><td>/explain</td><td>Get code explanations</td><td>Open file with code or highlight code you want explained and type:<p><code>/explain what is the fetchPrediction method?</code></p></td></tr><tr><td>/fix</td><td>Receive a proposed fix for the problems in the selected code</td><td>Highlight problematic code and type:<p><code>/fix propose a fix for the problems in fetchAirports route</code></p></td></tr><tr><td>/tests</td><td>Generate unit tests for selected code</td><td>Open file with code or highlight code you want tests for and type:<p><code>/tests</code></p></td></tr><tr><td>/help</td><td>Get help on using Copilot Chat</td><td>Type:<p><code>/help what can you do?</code></p></td></tr><tr><td>/clear</td><td>Clear current conversation</td><td>Type:<p><code>/clear</code></p></td></tr><tr><td>/doc</td><td>Add a documentation comment</td><td>Highlight code and type:<p><code>/doc</code></p><p>You can also press CMD+I in your editor and type <code>/doc/</code> inline</p></td></tr><tr><td>/generate</td><td>Generate code to answer your question</td><td>Type:<p><code>/generate code that validates a phone number</code></p></td></tr><tr><td>/optimize</td><td>Analyze and improve running time of the selected code</td><td>Highlight code and type:<p><code>/optimize fetchPrediction method</code></p></td></tr><tr><td>/clear</td><td>Clear current chat</td><td>Type:<p><code>/clear</code></p></td></tr><tr><td>/new</td><td>Scaffold code for a new workspace</td><td>Type:<p><code>/new create a new django app</code></p></td></tr><tr><td>/simplify</td><td>Simplify the selected code</td><td>Highlight code and type:<p><code>/simplify</code></p></td></tr><tr><td>/feedback</td><td>Provide feedback to the team</td><td>Type:<p><code>/feedback</code></p></td></tr></tbody></table>

See

---
# [GitHub Copilot Slash Commands Tutorial](./slash-tutorial.md)


# Excercises

 1. [Explain Exercises](./02.03.1/instructions.md)



---

#### [./back](./README.md)
