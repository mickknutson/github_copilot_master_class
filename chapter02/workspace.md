# `@workspace` Scope
The `@workspace` scope allows you to interact with Github Copilot specifically with the current `workspace` in your ide.



## Prompting for workspace details for a specific language (JavaScript)
`/createWorkspace`:

```text
/createWorkspace for javascript project using Jest
```

> NOTICE The above prompt. Copilot returns a description of the steps and result for a Maven oriented project, but suggests to use a Maven Archetype on the Terminal.

Using this prompt will leverage the IDE to create the proposed project and even ask the root directory the new project should be created in:
`@workspace /new`:
```text
@workspace /new initialize a JavaScript project using the Jest module called my-js-project
```
> NOTE: This is not the correct structure for a project that uses Jest for testing. This gives a better example:
```t
how do i initialize a javascipt project that uses Jest module called my-js-project
```

---
## Prompting for workspace details for a Python project
```text
@workspace /new scaffolding for a Python using the Pytest modules project called my-python-project
how do i initialize a Python project using the Pytest module called my-python-project
```

---

## Prompting for workspace details for a Java project 
```text
@workspace what is the proper project structure for a Java Project
```
```text
@workspace /new scaffolding for a Java Project
```
---

## Prompting for workspace details for a Java project using Maven
`@workspace /new` with more project details:
```text
@workspace /new Java Project using Maven with the package structure of com.baselogic.copilot.demo
```





---

#### [./back](./README.md)
