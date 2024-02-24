# `@workspace` Scope
The `@workspace` scope allows you to interact with Github Copilot specifically with the current `workspace` in your ide.


## Exercises
Open Github Copilot Chat
![Open GitHub Copilot Chat](../docs/images/chapter.02.open-cpc.jpg)

### Prompting for workspace details for a specific language (JavaScript)
```text
cd ~/chapter02/02.01.1/
```
```text
/createWorkspace for javascript project using jest
```

### You can even create Scaffolding for project
```text
cd ~/chapter02/02.01.1/
```

```text
@workspace /new node scaffolding for javascript project using jest
```

---

### Prompting for workspace details for a Java project 
```text
@workspace what is the proper project structure for a Java Project
```
```text
@workspace /new Java Project
```
---

### Prompting for workspace details for a Java project using Maven
```text
@workspace create a Java Project using the latest version of Maven
```
verse:
```text
@workspace /new Java Project using the latest version of Maven
```
---

### Prompting for workspace details for a Python project
```text
@workspace /new python project
```



---

#### [./back](./README.md)
