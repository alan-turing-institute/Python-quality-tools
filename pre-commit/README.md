# You ~could have invented~ probably did invent pre-commit

## What to test

Sometimes we want to run a check or two on our code as we develop. To that end, it isn't unusual to have a [script](./tests.sh) of some kind to run checks.

I'm going to claim, without much further justification, that the best time to run checks on your code is immediately before a commit.

That's fine. We can add it to our [.git/hooks/](.git/hooks/) `pre-commit` file so that it runs before a commit.

```shell
exec ./pre-commit/tests.sh
```
