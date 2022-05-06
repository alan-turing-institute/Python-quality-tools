# You ~could have invented~ probably did invent Pre-Commit

## How and when should we run tests?

Sometimes we want to run a check or two on our code as we develop. To that end, it isn't unusual to have a [script](./tests.sh) of some kind to run checks.

I'm going to claim, without much further justification, that the best time to run checks on your code is immediately before a commit.

That's fine. We can add it to our [.git/hooks/](.git/hooks/) `pre-commit` file so that it runs before a commit.

```shell
exec ./pre-commit/tests.sh
```

### Questions

1. Is this the right time to run tests?
2. If so, haven't we already solved the problem with the hooks file?

### Answers

1. It's arguable better to do it live as you code but that's not always possible.
2. Some things to think about:
   1. How do you share your pre-commit hooks and make it easy to install them?
   2. How do you test your staged changes and not your working directory?
   3. How are you going to run `mdl`, the best Markdown linter, which happens to be written in Ruby? Will you do [what I did](https://github.com/alan-turing-institute/rcp-ea-management-functions/blob/f56c685df0fc1afd72641a8d60b7bf25678b4911/status_function/run_tests.sh#L38)?

## How do we use Pre-Commit?

1. `brew install pre-commit`
2. `pre-commit sample-config > pre-commit-config.yaml`
3. `pre-commit install`
4. `pre-commit run [hook-id]`

You'll notice that the `repo` entry is a URL. There you will find the hooks defined in an installable Python repo.

You can also simply run a local command so we can call [tests.sh](./tests.sh) using Pre-Commit.

Alternatively, we could remove our dev-dependency on flake8 all together and use the <https://github.com/pycqa/flake8> hook.

We can also add hooks in other languages, as long as we have them installed. If we don't, hooks are often available in Docker flavours too (and you can write your own if one isn't). There is a big list [on the Pre-Commit website](https://pre-commit.com/hooks.html).

## How do we run Pre-Commit in a GH Action?

We probably want to run Pre-Commit in an Action in case devs forget to run pre-commit install.
We could use [pre-commit/action](https://github.com/pre-commit/action) but it is deprecated and recommends [pre-commit.ci](https://pre-commit.com/). Instead of either of those, we'll write a simple shell equivalent.
