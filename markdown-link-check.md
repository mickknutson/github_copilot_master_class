# markdown-link-check

## Original Prompt
```t
@workspace scan all my Markdown files and verify all the links are valid
```

## Copitlot Anser:

To verify all the links in your Markdown files, you can use a tool like markdown-link-check. Here's how you can use it:

Install markdown-link-check globally using npm:

```t
npm install -g markdown-link-check
```

Run `markdown-link-check` on each Markdown file. You can use the find command to `find` all Markdown files and run `markdown-link-check` on each file:

```t
find . -name \*.md -exec markdown-link-check {} \;
```

This command will find all Markdown files in the current directory and its subdirectories and run `markdown-link-check` on each file. `markdown-link-check` will check all the links in each file and print a report of all broken links.

Please note that `markdown-link-check` can only check HTTP/HTTPS links. It cannot check links to local files or anchors within the same document. If you need to check these types of links, you might need to use a more advanced tool or write a custom script.

## Excluding Files and Directories

Here's an example of how you can exclude the `node_modules` and `dist` directories:
```t
find . -type d \( -path **/node_modules -o -path **/dist \) -prune -o -name '*.md' -print | xargs markdown-link-check
```


This command works as follows:

* `-type d \( -path ./node_modules -o -path ./dist \) -prune` finds directories that match the specified paths and excludes them from the search.
* `-o -name '*.md' -print` finds files that match the specified name (in this case, '*.md') and prints their paths.
* `xargs markdown-link-check` takes the printed paths and passes them as arguments to `markdown-link-check`.

You can replace `./node_modules` and `./dist` with the paths to the directories you want to exclude. If you want to exclude more directories, you can add them to the `-path` option with `-o -path ./your_directory`.

Please note that the paths should be relative to the current directory. If you run the command from a different directory, you might need to adjust the paths accordingly.


## Create an alias in `~.aliases`:
```t
alias link-check = "find . -type d \( -path **/node_modules -o -path **/dist \) -prune -o -name '*.md' -print | xargs markdown-link-check"
```



## Command I run to save out to a file:
```t
touch ./target/markdown-link-check.txt
find . -type d \( -path **/node_modules -o -path **/dist \) -prune -o -name '*.md' -print | xargs markdown-link-check > ./target/markdown-link-check.txt
```

Or:

```t
touch ./target/markdown-link-check.txt
find . -type d \( -path **/node_modules -o -path **/dist \) -prune -o -name '*.md' -print | xargs -I {} bash -c "markdown-link-check {} >> ./target/markdown-link-check.txt"
```

> NOTE: will display "ERROR: 1 dead links found!" messages but is still saving data to the outpuyt file.