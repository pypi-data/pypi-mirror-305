[![PyPI](https://img.shields.io/pypi/v/freshdeps.svg?style=flat-square&color=rgb(24,114,110,0.8))](https://pypi.python.org/pypi/freshdeps/)
[![Python Version](https://img.shields.io/pypi/pyversions/freshdeps.svg?style=flat-square&color=rgb(14,90,166,0.8))](https://pypi.python.org/pypi/freshdeps/)

# FreshDeps

FreshDeps is a Python tool designed to keep your project's dependencies up-to-date by automatically updating your requirements.txt file from requirements.in.

It integrates with GitLab to create merge requests (MRs) for dependency updates, ensuring that you always have fresh and secure dependencies in your project.

- [Features](#features)
- [Installation](#installation)
- [Usage GitLab CI](#usage-gitlab-ci)

## Features
- Automatically updates Python dependencies using pip-compile.
- Creates GitLab merge requests with updated dependencies.
- Supports assigning MRs to specific users.
- Prevents duplicate or conflicting MRs by checking existing ones.
- Allows multiple open MRs if needed.

## Installation

You can install FreshDeps via pip:

```shell
pip install freshdeps
```


## Usage GitLab CI

#### To use FreshDeps add [job](https://docs.gitlab.com/ee/ci/jobs/) and create [scheduled pipeline](https://docs.gitlab.com/ee/ci/pipelines/schedules.html):


```yml
stages:
 - update-dependencies

variables:
 PIP_INDEX_URL: "https://pypi.org/simple"
 GITLAB_URL: "https://gitlab.com"
 GITLAB_PROJECT_ID: $CI_PROJECT_ID
 GITLAB_PRIVATE_TOKEN: $CI_JOB_TOKEN
 GITLAB_DEFAULT_BRANCH: "main"

update_dependencies:
 stage: update-dependencies
 image: python:3.9-slim
 script:
   - pip install freshdeps pip-tools
   - fresh-deps requirements.in --output-file requirements.txt \
       --pypi-index-url=$PIP_INDEX_URL \
       --gitlab-url=$GITLAB_URL \
       --gitlab-project-id=$GITLAB_PROJECT_ID \
       --gitlab-private-token=$GITLAB_PRIVATE_TOKEN \
       --gitlab-default-branch=$GITLAB_DEFAULT_BRANCH

only:
   - schedules   # This job will only run on scheduled pipelines (you can adjust this as needed)
```


#### Command-line Arguments:

| Argument | Description |
|-------------|-------------|
| `requirements_in`  | Path to the input file (`.in`) containing unpinned requirements.  |
| `--output-file`  | Path to output file (`.txt`) where pinned requirements will be written.  |
| `--pypi-index-url`  | PyPI index URL (default: https://pypi.org/simple). |
| `--gitlab-url`  | The URL of your GitLab instance (default: https://gitlab.com). |
| `--gitlab-project-id`  | The ID of the GitLab project where MRs should be created. |
| `--gitlab-private-token`  | Your private token for authenticating with GitLab API. |
| `--gitlab-assignee`  | Username of a user who should be assigned to review the MR (optional). |
| `--gitlab-default-branch`  | Default branch name in your repository (default: main). |
| `--gitlab-allow-multiple-mrs`  | Allow multiple open merge requests at once (optional flag). |

#### Handling Merge Requests:

- If there are no changes detected between current and newly generated dependency files, no MR will be created.

- If an MR already exists for similar changes, FreshDeps prevents creating duplicates unless explicitly allowed via flags.

