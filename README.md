# Tweet with GitHub Actions
> Post a tweet message using a button in GitHub Actions

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/tweet-gh-actions-py?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/tweet-gh-actions-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Python - >=3.6](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - tweepy](https://img.shields.io/badge/dependency-tweepy-blue)](https://pypi.org/project/tweepy)

[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github-actions&logoColor=white)](https://github.com/features/actions)


## About

- This project can post a tweet to your Twitter account using a cloud runner.
- This comes with a short Python script - [tweet.py](/tweepy.py).
- It runs using [GitHub Actions](https://michaelcurrin.github.io/dev-resources/resources/ci-cd/github-actions/) and a manual trigger - [Workflow dispatch](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/ci-cd/github-actions/triggers.html#workflow-dispatch). See [tweet.yml](/.github/workflows/tweet.yml) workflow file.
- The flow does not rely on any Actions specialized around Twitter. It just uses generic Python setup action.
- This is a template project - get a copy and then extend it for your needs.


## Sample usage
> How to run the GitHub Actions workflow manually to create a tweet

_Note: Only administrators of this repo can run the workflow. But the Actions logs are public if you want to see the history of runs._

Click _Run workflow_ button on the right:

<img src="/docs/_media/workflow-1.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

Enter your message:

<img src="/docs/_media/workflow-2.png" alt="Workflow screenshot" title="Workflow screenshot" width="400" />

Check the output in the log:

<img src="/docs/_media/workflow-3.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

View the profile on Twitter and see the new tweet added:

<img src="/docs/_media/created-tweet.png" alt="Tweet screenshot" title="Tweet screenshot" width="500" />



## Start tweeting from your own repo

Get a copy of this project.

<div align="center">

[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/tweet-gh-actions-py/generate)

</div>

Customize the secrets on GitHub as per the [docs](/docs).

Then run the workflow on GitHub to post a tweet using text that you enter.

### Customize

You can customize this project with your own logic. 

Such as to generate a random message, based on a text file of possible messages.

You could make the workflow run daily by setting up a [Schedule](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/ci-cd/github-actions/triggers.html#trigger-on-a-schedule) trigger.

Or you could tweet whenever you deploy or create a GitHub release. Though if you are adding tweeting logic to an existing project, you might want to use a tweet-related Action from the GitHub Actions marketplace. That means you just need a few lines in a workflow and don't need the whole Python script.


## Documentation

<div align="center">

[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
