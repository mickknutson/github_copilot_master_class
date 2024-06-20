# `@workspace` Scope
The `@workspace` scope allows you to interact with Github Copilot specifically with the current `workspace` in your ide.


# JavaScript
## Prompting for workspace details for a specific language (JavaScript)
`/createWorkspace`:
find . -type f -name '*.cs'find . -type f -name '*.cs'
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

# Python
## Prompting for workspace details for a Python project
```text
@workspace /new initialize a Python project using the Pytest module called my-python-project
```

# Java

## Prompting to create a Java 11 project using Maven
**@workspace**
```text
@workspace create a Java Project using Maven
```

**@workspace /new**
```text
@workspace /new scaffolding for a Java 11 Project using Maven
```


**@workspace /createWorkspace**
```text
@workspace /createWorkspace for a Java 11 Project using Maven
```
---

## Prompting for workspace details for a Java project using Maven
`@workspace /new` with more project details:
```text
@workspace /new Java Project using Maven
Use Java version 11
Add JUnit Jupiter dependencies for Junit 5 unit testing
Add Surefire plugin for running tests
Use version '[5.0,)' of 'org.junit.jupiter'
Package structure of 'com.baselogic.copilot.demo'
Name the project 'my-java-project'
```
> See notes below

---
# Notes

### Issues with Java prompting
> When using shorter, less descriptive prompting such as:
> `@workspace /new Java Project using Maven and Junit with the package structure of com.baselogic.copilot.demo`
1. The `pom.xml` has issues with `dependency` declaration that will not work and must be corrected for the build to work at all.
2. The generated unit test class will not compile and must be mostly rewritten in order to compile and to work.
3. Had to be very specific in order to get consistant output



---

#### [./back](./README.md)
