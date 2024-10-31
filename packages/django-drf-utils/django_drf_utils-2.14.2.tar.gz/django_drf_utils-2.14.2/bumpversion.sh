#!/usr/bin/env bash

set -e

HELP="Bump package version and update CHANGELOG.

Note: run this script from the root of the repository.

Requirements: git-cliff >= 2.2.0

Usage: bumpversion.sh [OPTIONS] <PACKAGE>

Options:
  -n, --dry-run     Run script without making any changes.
  -c, --custom      Custom version number to use. If not specified, the script
                    will infer the version number based on the commits content
                    since the last release.
  -h, --help        Display this help message.

Examples:
  bumpversion.sh
  bumpversion.sh --dry-run
"

dry_run=false
cliff_config=".cliff.toml"
version_new=""

while [[ $# -gt 0 ]]; do
  case $1 in
    -n | --dry-run)
      dry_run=true
      shift
      ;;
    -h | --help)
      echo "$HELP"
      exit 0
      ;;
    -c | --custom)
      if [ -z "$2" ]; then
        echo "💥 Missing version number" >&2
        echo "$HELP"
        exit 1
      fi
      version_new="$2"
      shift
      shift
      ;;
    -? | --*)
      echo "💥 Unsupported flag: $1" >&2
      echo "$HELP"
      exit 1
      ;;
  esac
done

# The `sed` in-place command behaves differently between the BSD (MacOS) and GNU (Linux)
# implementations. This makes the command portable.
# Default case for Linux sed, just use "-i"
case "$(uname)" in
  Darwin*) sedi=(-i "") ;; # For MacOS, use two parameters
  *) sedi=(-i) ;;
esac

pyproject_toml="pyproject.toml"
changelog_file="CHANGELOG.md"
version_current="$(sed -n 's/^version = "\([0-9a-z\.\-]*\)"$/\1/p' "${pyproject_toml}")"
REPO_URL="$(sed -n 's|^Repository = "\(.*\)"$|\1|p' "${pyproject_toml}")"
export REPO_URL
echo "📌 Current version: ${version_current}" >&2

# Infer the new version number if not provided by the user.
if [ -z "$version_new" ]; then
  version_new=$(git cliff -c "$cliff_config" --bumped-version | cut -d'/' -f2)
fi

commit_msg="chore(release): ${version_new}"
files_to_commit=("${changelog_file}" "${pyproject_toml}")

echo "📦 Bumping to version $version_new" >&2
if [ "$dry_run" = false ]; then
  sed "${sedi[@]}" "s/\(^ *version = \"\)[0-9\.]*[a-z0-9\.\-]*\"\$/\1$version_new\"/" "${pyproject_toml}"
fi

echo "📜 Generating changelog" >&2
echo
# Print the changelog to stdout
git cliff -c "$cliff_config" -u --tag "${version_new}" >&2
echo
if [ "$dry_run" = false ]; then
  # Update the changelog file
  git cliff -c "$cliff_config" -u -p "${changelog_file}" --tag "${version_new}"
  echo
  git add "${files_to_commit[@]}"
  git commit -q -m "$commit_msg"
  git tag -a "$version_new" -m "$commit_msg"
else
  echo "🚧 Dry run: Would have commited: ${files_to_commit[*]}" >&2
fi
echo "🖊️  New commit: $commit_msg" >&2
echo "🏷️  New tag: $version_new" >&2
echo "🚀 Version bumped to: $version_new" >&2
if [ "$dry_run" = false ]; then
  echo "👷 You can now push the new version, using: git push origin $(git branch --show-current)" >&2
  echo "👷 If you also want to trigger a new release, instead use: git push --follow-tags origin $(git branch --show-current)" >&2
else
  echo "🚧 Dry run: completed" >&2
fi

# Print the new version on stdout, in case the user wants to retrieve this
# value for further usage by the shell.
echo "$version_new"
