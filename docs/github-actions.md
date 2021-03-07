# GitHub Actions


## Create repo

Get a copy of this repo using the button on [README](/README.md). As a template or fork.


## Set secrets

Ensure you have a Twitter dev account setup and have generated tokens for your Twitter app - see [Generate tokens](generate-tokens.md) doc.


Go to your repo's _Settings_.

Go to the _Secrets_ tab.

Create 4 secrets named as follows:

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_KEY`
- `ACCESS_SECRET`

You make a secret by clicking _New repository secret_ on the _Secrets_ tab, entering a name above and pasting a copied value.


## Run your workflow

Go to your repo's _Actions_ tab.

Select the workflow name under Workflows.

> How to run the GitHub Actions workflow manually to create a tweet

Click _Run workflow_ button on the right:

<img src="/docs/_media/workflow-1.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

Enter your message:

<img src="/docs/_media/workflow-2.png" alt="Workflow screenshot" title="Workflow screenshot" width="400" />

Check the output in the log:

<img src="/docs/_media/workflow-3.png" alt="Workflow screenshot" title="Workflow screenshot" width="600" />

View the profile on Twitter and see the new tweet added:

<img src="/docs/_media/created-tweet.png" alt="Tweet screenshot" title="Tweet screenshot" width="500" />

In this case, I posted for my [@WhoopiGoldbot](https://twitter.com/whoopigoldbot) bot account.
