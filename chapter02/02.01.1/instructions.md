# Instructions

The following are instructions for shit sections exercise 

## Outline
This exercise contains two directories:
- `lab` contains starter files if any are needed. Might be empty. This is the directory you should perform all your work in. The project and files might not run, and might fail compilation until the lab has been completed. _(See instructions below)_

- `solution` contains completed, and runnable files. Do not perform work in this directory.


---
## Exercise Instructions

1. Open Copilot Chat
2. Use the following prompt to create a base JavaScript project:
```t
how do i initialize a javascipt project that uses Jest module called my-js-project
```






3. Copilot chat will describe the project layout and display a `Create Workspace` button. Click the `Create Workspace` button and choose `~/lab` as the _Parent Directory_ for the new project.

4. The new project will be created and the IDE will open the `~/lab/my-jest-project` directory as the parent and you will be in the newly created project.

5. Inspect the `./src/index.js` and `./test/index.test.js` files.

6. Open `./src/index.js` and put the following text at the beginning of the file:

```text
// Describe: This is a simple hello world program
```

7. Open Copilot (_Ctrl+ Enter_ or _Cmd+i_) and add the following prompt:

```text
/ create a hello world function that returns a string
/ that says "Hello, World!"
/ export the function so that it can be used in other files
```

8. Copilot should generate the following:

```text
function helloWorld() {
  return "Hello, World!";
}

module.exports = helloWorld;
```

9. Open `./src/index.js` and open Copilot and enter the prompt `/tests`. You should get a refactor preview. Accept the suggestion and you should get the following in `./test/index.test.js`:
```text
const { helloWorld } = require('../src/index');

test('helloWorld function returns the correct greeting', () => {
  const result = helloWorld();
  expect(result).toBe('Hello, world!');
});
```

10. Open a terminal to the root directory and run the `npm test` to execute the tests and the code.

> You might see the following error on the terminal:
```
sh: jest: command not found
```

14. If you do, open Copilot and enter the following prompt:
```t
@terminal /explain jest: command not found
```

> This will describe, in detail, what is causing the error, and the ways to correct the error.

15. Install Jest:
```t
npm install jest
```

15. Rerun the tests:
```t
npm test
```
> 

---

#### [../back](../README.md)
