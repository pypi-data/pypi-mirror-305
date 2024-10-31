# Contributing to django-drf-utils

## Commit Message Guidelines

This project follows the [Angular commit message guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-guidelines)
for its commit messages.

### Template

Fields shown in `[square brackets]` are optional.

```
type[(scope)]: subject line - max 100 characters

[body] - extended description of commit that can stretch over
multiple lines. Max 100 character per line.

[footer] - links to issues with (Closes #, Fixes #, Relates #) and BREAKING CHANGE:
```

### Examples

```
feat(projects): limit names to only contain lowercase alphanumeric characters

Validates project names in the frontend and backend to only allow
lowercase alphanumeric characters.
Having project names only consisting of lowercase alphanumeric characters
makes them more consistent, more easily readable and easier to remember.

BREAKING CHANGE: It is no longer possible to use any other characters in
project names than lowercase alphanumeric characters.

Handling it through a database migration instead of making this a breaking change was considered,
however we thought it would be preferrable to keep displaying the previous name until the project
is edited for the first time, where the validation enforces the correct naming scheme.
This allows users to choose which name fits best, without risking automatically migrating to
a name that is not suitable.

To migrate, edit the projects which have names including characters that
are not allowed, and save them with a new name which only includes
alphanumeric characters.


Closes #7, #123, Related #23
```

```
fix(frontend/DataTransfer): ensure adding a data transfer only adds it once

Previously, adding a data transfer resulted in the newly added DTR to show up twice in the table
of data transfers.


Closes #141
```

```
docs(CONTRIBUTING): add examples of conventional commit messages

Add a few examples of conventional commit messages to CONTRIBUTING.md, so that people don't have
to click on the "Angular commit message guidelines" link to read the full specifications.
Add a concise summary of the guidelines to provider a reminder of the main types and keywords.


Closes #114, #139
```

### Type and keywords summary

**Type:** the following types are allowed. Only types shown in **bold** are automatically added to
the changelog (and those containing the `BREAKING CHANGE: ` keyword):

- **feat**: new feature
- **fix**: bug fix
- build: changes that affect the build system or external dependencies.
- ci: changes to CI configuration files and scripts.
- docs: documentation only changes
- perf: code change that improves performance.
- refactor: code change that neither fixes a bug nor adds a feature
- style: change in code formatting only (no effect on functionality).
- test: change in unittest files only.

**Scope:**

- name of the file/functionality/workflow affected by the commit.
- if the change only affects the frontend or the backend, the scope can be prefixed by
  `frontend/` or `backend/`, respectively.

**Subject line:**

- one line description of commit with max 100 characters.
- use the imperative form, e.g. "add new feature" instead of "adds new feature" or
  "added a new feature".
- no "." at the end of subject line.

**body:**

- Extended description of commit that can stretch over multiple lines.
- Max 100 characters per line.
- Explain things such as what problem the commit addresses, background info on why the change
  was made, alternative implementations that were tested but didn't work out.

**footer:**

- Reference to git issue with `Closes/Close`, `Fixes/Fix`, `Related`.
- Location for `BREAKING CHANGE: ` keyword. Add this keyword followed by a description of what
  the commit breaks, why it was necessary, and how users should port their code to adapt to the
  new version.

### Commit messages and auto-versioning

The following rules are applied by the auto-versioning system to modify the version number when a
new commit is pushed to the `main` branch:

- Keyword `BREAKING CHANGE: `: increases the new major digit, e.g. 1.1.1 -> 2.0.0
- Type `feat`: increases the minor version digit, e.g. 1.1.1 -> 1.2.0
- Type `fix`: increases the patch digit, e.g. 1.1.1 -> 1.1.2

**Note:** an exception to the behavior of `BREAKING CHANGE: ` is for pre-release versions (i.e.
0.x.x). In that case, a `BREAKING CHANGE: ` keyword increases the minor digit rather than the
major digit. For more details, see the
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) and the
[semantic versioning](https://semver.org/spec/v2.0.0.html) specifications.
