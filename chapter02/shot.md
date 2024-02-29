# Chapter 02.02: Shot Prompting

Shot prompting is a concept in the field of artificial intelligence, particularly in the context of large language models like GPT (Generative Pre-trained Transformer), which involves providing the model with a small number of examples (or "shots") to guide its responses in a specific direction or to perform a particular task. These examples serve as a context or a prompt that the model uses to understand the task at hand better and generate more accurate or relevant responses. The term "shot" in this context refers to the number of examples provided: few-shot, one-shot, or zero-shot prompting, with each indicating the number of examples given to the model before it generates a response. Few-shot prompting, for example, gives the model several examples to learn from, enhancing its ability to predict or generate responses aligned with the provided context or examples.

This technique is particularly useful for tasks where explicit programming of every possible scenario is impractical. By demonstrating a task with a few examples, the model can infer the desired output format or the type of content expected. Shot prompting leverages the model's pre-trained knowledge, enabling it to apply learned patterns to new, similar tasks. This approach is versatile, supporting a wide range of applications from text generation to more complex problem-solving tasks, making it a powerful tool in the AI toolkit for adapting models to specific needs without extensive retraining.


## Zero Shot Prompting

In zero-shot prompting, the model uses its general inference ability to interpret the task based on the provided instructions alone, aiming to produce a relevant output or solve the problem without prior exposure to similar tasks.

For example, in software development, a zero-shot prompt to a model could be
```t
Write a Python function to convert a CSV file to a JSON file
```

without providing any examples of how to do it. The model would need to rely on its pre-existing knowledge of Python, CSV, and JSON formats to generate the code. 

Another example might be asking the model to:
```t
Generate SQL queries to create a database schema for an e-commerce platform
```

where the model has to infer the typical requirements of an e-commerce platform (like users, products, orders) and produce the corresponding SQL commands, all without any direct examples of the schema. These scenarios demonstrate the power of zero-shot prompting in enabling AI models to assist in software development tasks by generating code, solving problems, or providing insights based on the model's generalized understanding and reasoning capabilities.

## One Shot Prompting

One-shot prompting is particularly useful in software development for generating code, solving problems, or providing specific insights where direct examples or templates can significantly enhance the model's ability to produce relevant and accurate outputs.

**Example 1: Generating a Regular Expression for Email Validation**
1. Provide the model with an example regular expression for validating a phone number, explaining its components briefly.
2. Ask the model to generate a regular expression for validating an email address, using the structure of the provided example as a guideline. The model would analyze the example's pattern and apply a similar approach to construct an email validation pattern, considering common elements like usernames, the "@" symbol, domain names, and top-level domains.

**Example 2: Writing a Function to Calculate Fibonacci Numbers**
1. Show the model a simple example of a Python function that calculates the factorial of a number, highlighting the recursive approach used in the function.
2. Request the model to write a function to calculate Fibonacci numbers using recursion, inspired by the structure and logic of the factorial function. The model would utilize the understanding of recursion from the example to devise a function that generates Fibonacci numbers, applying the concept of adding the two preceding numbers in the sequence to produce the next number.



## Multiple Shot Prompting

In software development, multiple shot prompting can be particularly useful for code generation, debugging, or creating documentation, as it allows the model to draw from a richer set of examples to produce more precise and contextually appropriate results.

### Example: Generating API Endpoint Documentation
1. Provide the model with several examples of API endpoint documentation, each describing different endpoints (e.g., for creating a user, fetching a product list, updating a product detail). Each example should include the HTTP method, URL path, request parameters, and a brief description.
   
**Example: Creating a User**

```t
HTTP Method: POST
URL Path: /api/users/create
Request Parameters: 
    - username (string, required): The desired username for the new user. 
    - email (string, required): The email address for the new user. 
    - password (string, required): The password for the new user account.

Description: This endpoint is used to create a new user account in the system. It requires a username, email, and password to be provided in the request. On success, it returns the ID of the newly created user.

```

2. Ask the model to generate documentation for a new API endpoint that allows searching for users by name. The model would use the structure and format of the provided examples to produce a detailed documentation snippet, including the new endpoint's purpose, usage, and parameters.

**Example Documentation Task: Searching for Users by Name Endpoint**

```t
Documentation Task: Searching for Users by Name Endpoint

HTTP Method: Clearly indicate whether this endpoint uses GET, POST, or another method, based on its functionality and the best practices for RESTful API design.

URL Path: Specify the endpoints URL path, incorporating placeholders or variables as needed to represent dynamic segments relevant to user searches.

Request Parameters: List and describe all parameters accepted by this endpoint, distinguishing between required and optional parameters. For a search functionality, this might include parameters like name for the users name to search for, and potentially other filters or pagination controls.

Description: Provide a detailed description of the endpoint, emphasizing its utility in enabling clients to find users by name. Mention any special behavior, such as case sensitivity, partial matches, or how results are ordered. This section should give developers a clear understanding of how and when to use the endpoint, along with any expected response format and content.
```


---

## Exercises:
* [Shot prompting](./02.02.1/instructions.md)

---

#### [../back](./README.md)
