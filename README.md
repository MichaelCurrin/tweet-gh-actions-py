# Tweet with GitHub Actions
> Post a tweet message using a button in GitHub Actions

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/tweet-gh-actions-py?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/tweet-gh-actions-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Python - >=3.6](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - tweepy](https://img.shields.io/badge/dependency-tweepy-blue)](https://pypi.org/project/tweepy)

[![Made with GH Actions](https://img.shields.io/badge/CI-GitHub_Actions-blue?logo=github-actions&logoColor=white)](https://github.com/features/actions)


## About

- This is a template project - get a copy and then customize it for your needs.
- This project can post a tweet to your Twitter account using a cloud runner on GitHub.
- It runs using [GitHub Actions](https://michaelcurrin.github.io/dev-resources/resources/ci-cd/github-actions/) and a manual trigger - [Workflow dispatch](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/ci-cd/github-actions/triggers.html#workflow-dispatch). See [tweet.yml](/.github/workflows/tweet.yml) workflow file.
- The flow does not rely on any Actions specialized around Twitter. It uses a generic Python setup action and your own logic.
- This comes with a short Python script - [tweet.py](/tweepy.py).


## Disclaimer

Tweeting using API requests and code requires registering a dev account on Twitter, which means filling in an application form and getting approval from Twitter's team.


## Use cases
> How you could use this project

- Tweet your GitHub repo URL or website URL on a deploy (like a merge to master or a release is created).
- Generate a random tweet message from a file of possible messages and tweet it daily.
- Just for fun, enter a message directly in GitHub Actions (though you're limited on the input which only accepts a single line of input - unless you adapted the Python script to convert `"\n"` text into an actual line break).
- Copy the code to run somewhere else. Like on your web server, a Lambda, an automated task or a manual script. Just avoid running tweet logic on a frontend (like with JS) and you'd unsafely expose your credentials, while running server side is fine.


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

Only an admin user of ths repo can Tweet using it. But if you copy this repo to your own account and have Twitter API credentials at hand, you can start tweeting with GitHub too.

Get a copy of this project:

<div align="center">

[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/tweet-gh-actions-py/generate)

</div>

Next, customize the secrets on GitHub as per the [docs](/docs).

Then run the workflow on GitHub to post a tweet using text that you enter.

### Customize

You can customize this project with your own logic. 

Such as to generate a random message, based on a text file of possible messages.

You could make the workflow run daily by setting up a [Schedule](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/ci-cd/github-actions/triggers.html#trigger-on-a-schedule) trigger.

Or you could tweet whenever you deploy or create a GitHub release. Though, if you are adding tweeting logic to an existing project, then instead of using this project, you might want to use a tweet-related Action from the [GitHub Actions marketplace](https://github.com/marketplace). Which means you just need a few lines in a workflow and don't need a whole Python script.


## Documentation

<div align="center">

[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
