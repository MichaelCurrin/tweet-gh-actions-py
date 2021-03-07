# Tweet with GitHub Actions
> Post a tweet to your Twitter account using GitHub Actions

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/tweet-gh-actions-py?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/tweet-gh-actions-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Python - >=3.6](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - tweepy](https://img.shields.io/badge/dependency-tweepy-blue)](https://pypi.org/project/tweepy)

[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github-actions&logoColor=white)](https://github.com/features/actions)


## About

This is a template project which demonstrates how to use a short Python script to post a tweet to your Twitter account using [GitHub Actions](https://michaelcurrin.github.io/dev-resources/resources/ci-cd/github-actions/).

The flow doesn't rely on any Actions specialized around Twitter. Just a generic Python setup action. See [tweet.yml](/.github/workflows/tweet.yml) workflow file.


## Copy this template

Get a copy of this repo. Then run the workflow on GitHub to post a tweet using text that you enter.

<div align="center">

[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/tweet-gh-actions-py/generate)

</div>

Then customize such with your own logic. Such as to generate a random message daily based on a text file of possible messages. This can be done using `cron` in the workflow.


## Sample usage
> How to run the GitHub Actions workflow manually to create a tweet

Click _Run workflow_ button on the right:

<img src="/docs/_media/workflow-1.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

Enter your message:

<img src="/docs/_media/workflow-2.png" alt="Workflow screenshot" title="Workflow screenshot" width="400" />

Check the output in the log:

<img src="/docs/_media/workflow-3.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

View the profile on Twitter and see the new tweet added:

<img src="/docs/_media/created-tweet.png" alt="Tweet screenshot" title="Tweet screenshot" width="500" />


## Documentation

<div align="center">

[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
