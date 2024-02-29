# Open AI Whisper Exercises

The following are instructions for an exercise that uses Python with `panda`, `seaborn` and `matplotlib`.

## Outline
This exercise contains two directories:
- `lab` contains starter files if any are needed. Might be empty. This is the directory you should perform all your work in. The project and files might not run, and might fail compilation until the lab has been completed. _(See instructions below)_

- `solution` contains completed, and runnable files. Do not perform work in this directory.


---
## Exercise Instructions

1. Open Copilot Chat

2. Create a new Python files named `housing_data_demo.py`

3. Add the following description:
```
# Describe: Function to create a univariate and bivariate analysis on dataset.
```

4. Use copilot to generate a fnction using the following prompt:

```t
Create a function to perform a univariate and bivariate analysis on HousingData.csv and present the outcomes as visual using Seaborn.
```

5. There are three packages that might not be installed. Ask Copilot Chat how to install those packages and following the instructions to install the packages.
```t
how do i install the python package pandas
```

6. Right-click on the Python script and select `Run Python File in Terminal`.

7. The output `png` files should be located in the `./tmp` directory.


--- 
# Notes
> * Initial code that copilot generated was outdated:
```
You tried to access openai.Audio, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
```

> * Need to get an api_keyn for this to work:

'openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable'


---

#### [../back](../README.md)
