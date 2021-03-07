# Configuration
> Set tokens


## Export directly

Set the values once off.

```sh
$ export CONSUMER_KEY=abc
$ export CONSUMER_SECRET=def
$ export ACCESS_KEY=ghi
$ export ACCESS_SECRET=jkl
```

Or

## Export from dotenv file

Store the values in an ignored dotenv file.

Create a file from the template, then fill in the new file.

```sh
$ cp .env.local.template .env.local
```

Now load the values from the dotenv file.

```sh
$ export $(< .env.local)
```

Test:

```sh
$ bash -c 'echo $CONSUMER_KEY'
abcdefghi
```


Now you can continue to [Usage](usage.md) doc.
