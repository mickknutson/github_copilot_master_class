# My Java Project

This is a simple Java project using Maven for dependency management. The project is set up with a package structure of `com.baselogic.copilot.demo`.

## Prerequisites

- Java 11
- Maven

## Dependencies

- JUnit Jupiter for unit testing (version 5.0 or later)

## Plugins

- Surefire plugin for running tests

## Building the Project

To build the project, navigate to the project directory and run the following command:

```
mvn clean install
```

This will compile the code, run the tests, and package the project.

## Running the Project

To run the project, use the following command:

```
mvn exec:java -Dexec.mainClass="com.baselogic.copilot.demo.App"
```

## Running the Tests

To run the tests, use the following command:

```
mvn test
```

This will run all the tests in the project.