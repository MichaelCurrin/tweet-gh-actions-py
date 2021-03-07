# Tweet with GitHub Actions
> Post a tweet to your Twitter account using GitHub Actions

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/tweet-gh-actions-py?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/tweet-gh-actions-py/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)


## About

This project doesn't rely on any Actions specialized around Twitter. Just a generic Python setup action.

<div align="center">

[![Use this template](https://img.shields.io/badge/Generate-Use_this_template-2ea44f?style=for-the-badge)](https://github.com/MichaelCurrin/tweet-gh-actions-py/generate)

</div>


## Development
> Local setup for easy testing

### Install

Recommended - run this in a virtual environment using Python 3.

```sh
$ pip install -r requirements.txt
```

### Configure

```sh
$ export CONSUMER_KEY=abc CONSUMER_SECRET=def ACCESS_KEY=ghi ACCESS_SECRET=jkl
```

### Run

```sh
$ python tweet.py
```

```sh
$ python tweet.py 'Line 1
Line 2

#tweepy #twitterapi #python'
```



## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
