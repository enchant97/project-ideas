---
title: "Contributing"
---
Contributions are welcome, however ensure you have read and accepted the guidelines and terms.

## Contribution Agreement
By submitting a pull request you agree to these terms:
- You own the full rights to the contribution before submitting
- You accept your contributions will be submitted under the licenses shown in the `LICENSE.txt` file
- You grant the project owner (Leo Spratt / @enchant97) non-exclusive, transferable and irrevocable right to sub-license, distribute and sell the contributions


## Guidelines
These guidelines mostly target general contributions, certain project maintainers may be granted extra permissions.

- You accept the terms of the contribution agreement (shown above)
- Changes must target the "pre" branch, **do not** target 'main'
- Suggestions for new projects, may not be accepted
- Text must be in English UK/US
- Example implementations ideally be cross platform (amd64, arm64)
- Example implementations should have comments
- Keep code readable, well formatted, etc
- Follow directory naming scheme
- Code must work
- Don't commit system files (e.g. node_modules)
- Contributions must be suitable for all ages (no NSFW content allowed)
- Making grammar, spelling and other minor changes will not get your name listed in the credits or entitle you to add yourself as the author of any projects/example solutions, although these fixes are greatly appreciated

### New Project
- Use the "new-proj" script to create a new project. This will create a markdown file and create the implementation folder. *Running this script with no arguments will output the usage guide*
- Keep your document in draft mode until it's been marked as completed
- Ensure all sections are completed and there is at least one example implementation
- If your project gets merged your name will be added in the contributors list

### Editing A Project
- Ensure changes make sense
- Overall project requirements should not be changed, unless it has been approved


## Build Requirements
- [Hugo](https://gohugo.io/installation/) >= V0.100.0 extended
- Make
- Bash
- Installed Theme: `make install-theme`


## Tools
Make is used to allow certain tools/programs to be quickly used.

Get available commands by running:

```
make help
```

To aid the creation of new projects a script is provided:

```
./new-proj <complexity> <name>
```
