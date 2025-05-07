# Contributing to TwinCAT Dynamic Collections

Thank you for your interest in contributing to this project!

This repository follows the **Git Flow workflow**. Please review the guidelines below to ensure smooth collaboration and effective contributions to the TwinCAT Dynamic Collections library.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Forking the Repository](#forking-the-repository)
   - [Cloning Your Fork](#cloning-your-fork)
   - [Setting Up Remotes](#setting-up-remotes)
2. [Branching Strategy](#branching-strategy)
   - [Feature Branches](#feature-branches)
   - [Bug Fixes](#bug-fixes)
   - [Chores](#chores)
   - [Hotfixes](#hotfixes)
3. [Making Changes](#making-changes)
   - [TwinCAT Project Conventions](#twincat-project-conventions)
   - [Commit Messages](#commit-messages)
4. [Keeping Your Fork Updated](#keeping-your-fork-updated)
5. [Submitting Your Changes](#submitting-your-changes)
   - [Pull Requests](#pull-requests)
6. [Review Process](#review-process)
7. [Attribution](#attribution)

## Getting Started

### Forking the Repository

Begin by forking the main repository to your GitHub account. This creates a personal copy where you can make changes without affecting the original project.

### Cloning Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/your-username/TwinCat-Dynamic-Collections.git
````

Navigate into the project directory:

```bash
cd TwinCat-Dynamic-Collections
```

### Setting Up Remotes

Add the original repository as the upstream remote:

```bash
git remote add upstream https://github.com/fisothemes/TwinCat-Dynamic-Collections.git
```

Verify your remotes:

```bash
git remote -v
```

You should see:

```
origin    https://github.com/your-username/TwinCat-Dynamic-Collections.git (fetch)
origin    https://github.com/your-username/TwinCat-Dynamic-Collections.git (push)
upstream  https://github.com/fisothemes/TwinCat-Dynamic-Collections.git (fetch)
upstream  https://github.com/fisothemes/TwinCat-Dynamic-Collections.git (push)
```

## Branching Strategy

This project uses the **Git Flow** model, with clearly defined prefixes for different types of work.

### Feature Branches

Use for new functionality:

```bash
git checkout develop
git pull upstream develop
git checkout -b feature/short-description
```

### Bug Fixes

Use for fixes to existing functionality:

```bash
git checkout develop
git pull upstream develop
git checkout -b fix/short-description
```

### Chores

Use for maintenance or clean-up tasks (e.g., documentation, versioning changes):

```bash
git checkout develop
git pull upstream develop
git checkout -b chore/short-description
```

### Hotfixes

For urgent fixes that must go directly into `master`:

```bash
git checkout master
git pull upstream master
git checkout -b hotfix/short-description
```

## Making Changes

### TwinCAT Project Conventions

* Keep changes to `.plcproj`, or `.tsproj` files minimal and purposeful to avoid unnecessary diff noise.
* If modifying or adding tests in the test project, keep variable declarations aligned and consistent.
* Maintain compatibility with TwinCAT 3.1 4024.x build environments and ensure `.library` versioning reflects [SemVer](https://semver.org/).

### Commit Messages

Use conventional commit prefixes:

* `feat:` for new features
* `fix:` for bug fixes
* `chore:` for maintenance
* `docs:` for documentation
* `style:` for formatting
* `refactor:` for code restructuring

Example:

```
fix: unpin tc2_utilities and update version numbers for v1.0.7
```

Commit message structure:

* **Title**: approx. 60 characters max, imperative mood (e.g., "Add", not "Added")
* **Body**: optional, wrap at 80 characters, explain *what* was change and *why*.

For more, see [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).

## Keeping Your Fork Updated

Regularly sync your fork with the upstream repo:

```bash
git checkout develop
git fetch upstream
git merge upstream/develop
git push origin develop
```

Likewise, for `master`:

```bash
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

## Submitting Your Changes

### Pull Requests

1. Push your branch to your fork:

   ```bash
   git push origin your-branch-name
   ```

2. Go to the GitHub repo:
   [https://github.com/fisothemes/TwinCat-Dynamic-Collections](https://github.com/fisothemes/TwinCat-Dynamic-Collections)

3. Click **"Compare & pull request"**

4. Provide a clear title and a description that explains what the PR does, why it's needed, and any related issues (e.g., "Closes #12")

5. Target the `develop` branch, unless it’s a hotfix (in which case, target `master`)

## Review Process

Your pull request will be reviewed by maintainers. You may be asked to make changes for consistency, correctness, or clarity.

Once approved, the PR will be merged and included in the next release cycle (or immediately, if it’s a hotfix).

## Attribution

This guide is based on best practices from the open-source community and adapted specifically for TwinCAT library development in this repository.

For questions or suggestions, please open an issue or discussion.