# Zettelkasten CLI

A bespoke CLI for my Neovim + Obsidian Zettelkasten written in Python.

**Usage**:

```console
[OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `day`: Open daily note or create if it doesn't...
- `new`: Create a new note with the provided title.

## `day`

Open daily note or create if it doesn't exist.

**Usage**:

```console
day [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `new`

Create a new note with the provided title. Will prompt if no title given.
Adds Obsidian markdown link to the daily note.

**Usage**:

```console
new [OPTIONS] [TITLE]
```

**Arguments**:

- `[TITLE]`

**Options**:

- `--vim`: Indicates input is coming from vim. Prevents new file being opened.
- `--help`: Show this message and exit.

## Creating a Release

Push the changes to the repo and create a release with a new tag from the GitHub CLI or from the UI.

The GH Actions workflow handles the rest. It auto-updates the pyproject.toml and pushes to PyPi.
