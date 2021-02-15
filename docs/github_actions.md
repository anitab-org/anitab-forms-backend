# GitHub Actions

The purpose of using GitHub actions is to run tests and QA-checks.

## Configuration

There is currently one environment variable needed for configuring the GitHub actions. Details are mentioned below:

1. `ZULIP_API_KEY`: This secret variable is needed to run tests. This is the API key that we get from zulip to access ZULIP API. The content of this secret variable is like this :
    ```
    [api]
    email=example@example.com
    key=********************************************
    site=https://anitab-org.zulipchat.com
    ```
