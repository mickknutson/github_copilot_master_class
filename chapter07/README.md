# GitHub Advanced Security (GHAS) Tutorial

GitHub Advanced Security (GHAS) is a suite of tools designed to improve the security posture of your codebases hosted on GitHub. GHAS helps in identifying, managing, and mitigating security risks throughout the software development lifecycle. This tutorial will guide you through the key features of GHAS and show you how to use them effectively.

## Prerequisites
- A GitHub account
- Access to a repository where you have admin rights (GHAS features are available for GitHub Enterprise and GitHub.com under specific plans)

## 1. Enabling GitHub Advanced Security
First, you need to enable GHAS for your organization or repository, depending on your GitHub plan and preferences.

### For Organizations:
- Navigate to your organization's settings.
- Click on "Security" in the left sidebar.
- Select "Advanced Security" and follow the prompts to enable it.

### For Individual Repositories:
- Go to the repository settings.
- Under "Security & analysis", you'll find options to enable features of GHAS.

## 2. Features of GHAS

### Code Scanning
Code scanning automatically scans every git push to your repository for vulnerabilities.

#### Setting Up Code Scanning:
- Navigate to the "Security" tab of your repository.
- Click on "Code scanning alerts".
- Set up code scanning by following the setup wizard, which may include adding a GitHub Actions workflow file to your repository.

### Secret Scanning
Secret scanning looks for exposed secrets in your repository, such as API keys and tokens, to prevent unauthorized access.

#### Enabling Secret Scanning:
- For most plans, secret scanning is enabled by default once GHAS is active.
- You can view alerts under the "Security" tab of your repository.

### Dependency Review
Dependency review helps you review your project's dependencies for known vulnerabilities when you open a pull request.

#### Using Dependency Review:
- This feature is automatically enabled with GHAS.
- When opening or reviewing a pull request, check the "Files changed" tab for a dependency review report.
  
#### Utilizing Dependency Insights
- Dependency Graph: Ensure the Dependency Graph is enabled in your repository's settings to track dependencies.
- View Dependency Alerts: Check the "Security" tab for any alerts related to your dependencies. Update or replace vulnerable dependencies as recommended.

### Security Overview
Get an overview of the security status across all your repositories in an organization.

#### Accessing Security Overview:
- Navigate to your organization's "Security" tab.
- Here, you'll see an overview of all security alerts and vulnerabilities across your repositories.

## 3. Best Practices for Using GHAS
- **Regularly Review Security Alerts:** Make it a habit to check and address security alerts promptly.
- **Integrate Security into CI/CD:** Use GitHub Actions to integrate security checks into your continuous integration and deployment pipelines.
- **Educate Your Team:** Ensure that all contributors understand the importance of security practices and how to use GHAS features.
- **Leverage Community and Documentation:** GitHub has a wealth of documentation and a community forum where you can learn more and ask questions.

## Conclusion
GitHub Advanced Security provides powerful tools to enhance the security of your software. By integrating GHAS into your development workflow, you can proactively identify and mitigate security risks, ultimately building more secure applications. Remember, security is an ongoing process, and tools like GHAS are here to help you along the way.



---

#### [../back](../README.md)
