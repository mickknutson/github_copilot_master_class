## GitHub Copilot CLI

A CLI experience for letting GitHub Copilot help you on the command line.

NOTE: GitHub Copilot CLI is in **technical preview**.
Expect rough corners and poorly supported platforms.
To get access to GitHub Copilot CLI, [sign up on the waitlist](https://githubnext.com/projects/copilot-cli/).

GitHub Copilot CLI translates natural language into shell commands, with modes for different domains.
After installation, you can use the following three command:

- `??`: Translate natural language to arbitrary shell commands
- `git?`: Translate natural language to Git commands
- `gh?`: Translate natural language to GitHub CLI commands

GitHub Copilot CLI will also try to break down and explain piece by piece what the suggested command will do.

To use GitHub Copilot CLI, you must have access to [GitHub Copilot](https://github.com/features/copilot/).

## Supported platforms

GitHub Copilot CLI should basically work broadly across platforms, terminals and shells, but has a bias towards zsh on Linux.
It may therefore suggest you commands that do not work on your platform or your terminal.
If this happens, consider using the `revise` option to tell GitHub Copilot CLI what platform you're on.

The alias commands are only tested to work on zsh and bash.

We appreciate any and all input on how well GitHub Copilot CLI works on your platform, and how we can improve it.

### Minimum Node Version

GitHub Copilot CLI requires Node.js 16.0.0 or later. When using versions of Node.js prior to 16.0.0, you may encounter errors such as the following.

```bash
usr/local/lib/node_modules/@githubnext/github-copilot-cli/dist/index.js:27
...
SyntaxError: Unexpected token '.'
    at wrapSafe (internal/modules/cjs/loader.js:915:16)
    at Module._compile (internal/modules/cjs/loader.js:963:27)
```

## Installation and setup

Install GitHub Copilot CLI globally on your machine using `npm`:

```bash
$ npm install -g @githubnext/github-copilot-cli
```

This adds the command `github-copilot-cli` to your `PATH`.
To authenticate with GitHub, run the following command:

```bash
$ github-copilot-cli auth
```

and follow the on-screen instructions.
Once authenticated, the token will be stored on your machine and used for future requests, so this command only rarely needs to be run.

## Upgrading

To upgrade GitHub Copilot CLI, run the following command:

```bash
$ npm install -g @githubnext/github-copilot-cli
```

### Setup alias convenience commands

You can run GitHub Copilot CLI directly using `github-copilot-cli`, but we recommend you install the `??`, `git?`, and `gh?` commands in your shell.
These are not only more convenient to type, but also [provide added features](#whats-the-point-of-the-eval-and-alias-stuff).
To install them, run the following command:

```bash
  eval "$(github-copilot-cli alias -- "$0")"
```

These will add the commands to your shell, but only for the current session.
To make them available in all future sessions, you should add the above command on a line by itself to the bottom of your `.zshrc` or `.bashrc` or equivalent.

## Usage instructions and tips

<img width="600" src="https://githubnext.com/assets/projects/copilot-cli/what-the-shell.svg">

All three modes of GitHub Copilot CLI work in the same way:
you write a natural language query to declare what you want, and GitHub Copilot CLI will try to construct a command or sequence of commands to do it.
If you're happy with the suggested command, just ask GitHub Copilot CLI to run it for you.

### Explanations

GitHub Copilot CLI will also explain piece-by-piece what the suggested command does.
This is important when you're learning new commands or flags: the shell is very powerful, and you may inadvertently do irreversible changes you did not intend.
Always be sure you understand what a suggested command does before running it.
Like all AI systems, GitHub Copilot CLI is not perfect, and may make mistakes.

### Revisions

If the command is not quite what you wanted, you can revise your query and ask GitHub Copilot CLI to suggest a new command.
This workflow can be used for different purposes:

- GitHub Copilot CLI misunderstood your initial query, and a revision can put it back on track, e.g. `only files in current folder`.

- The suggestion applies to a different platform than yours. Use a revision to state your platform requirements, e.g. `on fish shell`.

- Start with a simple query, and iteratively make it more complex, e.g. building a multi-pipe command or several statements, like in the video showns above.
  This tends to work better than writing all the details in the first query.

- GitHub Copilot CLI may suggest placeholder names in the initial suggestion. You can use revise to replace them by the actual names you want to use, e.g. `on branch feature/origami-swans`.

### Gotchas in the shell

Since you write your query directly in the shell, there's a number of gotchas to be aware of.

Many symbols have a special meaning in the shell and will be interpreted _before_ they are handed to GitHub Copilot CLI.
The safest way is to avoid these symbols in queries altogether.
If you do particularly need them, most of them can be escaped by prefixing them with a backslash `\`, or by enclosing the entire query in single-quotes `' ... '`.

For instance:

- Quotes `'` or `"`, question marks `?`, or exclamation marks `!` in your query will usually cause a shell syntax error, or cause the shell to expect a second line of your query.
  In the latter case, press Ctrl-C to cancel the current shell statement, and write your query again without the offending symbol.

- Parentheses, braces and brackets `( ) [ ] { }` will likewise usually cause a shell syntax error, or cause the shell to expect a second line of your query.

- Asterisks `*` will be expanded to match file and folder names. This may cause sensitive file name information to appear in the query.

- A pipe `|` will be interpreted as the shell pipe and interpret anything after it as a separate command. This will almost surely fail since GitHub Copilot CLI is an interactive application.

- Be careful never to prepend a shell variable name with `$`: this causes the shell to expand the variable before GitHub Copilot CLI sees it, potentially sending sensitive information in the query.

### More example videos

### `git?`

<img width="600" src="https://githubnext.com/assets/projects/copilot-cli/git.svg">

### `gh?`

<img width="600" src="https://githubnext.com/assets/projects/copilot-cli/gh.svg">

## Privacy and telemetry

When using GitHub Copilot CLI, we will form a query and send it to the GitHub Copilot AI.
We are also gathering telemetry about the usage of the app.

We are very aware that the shell is a sensitive place with access to a lot of private information.
Rest assured that GitHub Copilot CLI sends only a minimal amount of information from your shell in its query and in gathered telemetry.

### What we never gather

We are **never** harvesting and sending any of the following:

- File and folder names you did not write in the query.
- Contents of any files on your system.
- Git repo, branch or status information
- The value of any environment variables set in your shell.
- The command history of your shell.
- Any shell command output, also not for the command you ask GitHub Copilot CLI to run.

## What's the point of the `eval` and alias stuff?

You may wonder about the somewhat round-about installation instructions for the convenience commands `??`, `git?`, and `gh?`.

The technical reason that these commands must be installed using `eval` is that they are not executables themselves, but rather "shell functions" that wrap `github-copilot-cli`.
This enables the commands to more tightly integrate with the current shell session, and provides two key features that you do not get if you run `github-copilot-cli` directly:

1. When you accept a suggested command, this gets run in the current shell session.
   This means your commands will use the same shell state - such as environment variables - as you would get by typing the command yourself.
   This sidesteps many potential points of confusion.
   In fact, when you do run `github-copilot-cli` directly, we wish to avoid exactly this confusion and therefore simply print the command and ask you to copy/paste it into your shell yourself, rather than opening a subshell.

2. When you accept a suggested command, we not only run it but also add it to your shell's command history.
   This means that if you wish to run it again or edit it, you can just use up-arrow or Ctrl-R to recall it.
