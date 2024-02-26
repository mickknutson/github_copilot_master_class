# Java and Maven Instructions

The following are instructions for Java exercise 

## Outline
This exercise contains two directories:
- `lab` contains starter files if any are needed. Might be empty. This is the directory you should perform all your work in. The project and files might not run, and might fail compilation until the lab has been completed. _(See instructions below)_

- `solution` contains completed, and runnable files. Do not perform work in this directory.


---
## Exercise Instructions

1. Open Copilot Chat
2. Use the following prompt to create a base JavaScript project:
```t
@workspace /new Java Project using Maven
Use Java version 11
Add JUnit Jupiter dependencies for Junit 5 unit testing
Add Surefire plugin for running tests
Use version '[5.0,)' of org.junit.jupiter
Package structure of com.baselogic.copilot.demo
Name the project my-java-project
```







6. Listing the included dependencies of the generated project. In the terminal in the project root, execute the following command:

```text
mvn dependency:tree
```

The output should look similiar to the following:
```
[INFO] com.baselogic.copilot.demo:my-java-project:jar:1.0-SNAPSHOT
[INFO] +- org.junit.jupiter:junit-jupiter-api:jar:5.10.2:test
[INFO] |  +- org.opentest4j:opentest4j:jar:1.3.0:test
[INFO] |  +- org.junit.platform:junit-platform-commons:jar:1.10.2:test
[INFO] |  \- org.apiguardian:apiguardian-api:jar:1.1.2:test
[INFO] \- org.junit.jupiter:junit-jupiter-engine:jar:5.10.2:test
[INFO]    \- org.junit.platform:junit-platform-engine:jar:1.10.2:test
```
> Hint: the version of `junit-jupiter-api` should be `5.10.2`, or the latest version.
> You can verify the latest version on the website _`mvnrepository.com`_


--- 
# Notes
> When using shorter, less descriptive prompting such as:
> `@workspace /new Java Project using Maven and Junit with the package structure of com.baselogic.copilot.demo`
1. The `pom.xml` has issues with `dependency` declaration that will not work and must be corrected for the build to work at all.
2. The generated unit test class will not compile and must be mostly rewritten in order to compile and to work.
3. Had to be very specific in order to get consistant output

---

#### [../back](../README.md)
