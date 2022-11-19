---
title: "Contributing"
---

## Guidelines
Contributions are welcome, however follow these guidelines:

- Suggestions for new projects, may not be accepted
- Text must be in English UK/US
- Example implementations in other languages
- Example implementations without extra dependencies
- Example implementations ideally be cross platform (amd64, arm64)
- Example implementations should have comments
- Keep code readable, well formatted, etc
- Follow directory naming scheme
- Code must work
- Grammar fixes allowed
- Don't commit system files (e.g. node_modules)
- Contributions must be suitable for all ages (no NFSW content allowed)
- Contributions must be your own work (you own the rights)
- Contributions must be under the specified license (found in LICENSE.txt)
- Changes should target the "pre" branch

### New Project
- Use the "new-proj" script to create a new project. This will create a markdown file and create the implementation folder. *Running this script with no arguments will output the usage guide*
- Keep your document in draft mode until it's been marked as completed
- Ensure all sections are completed and there is at least one example implementation
- If your project gets merged your name will be added in the contributors list

### Editing A Project
- Ensure changes make sense
- Overall project requirements should not be changed, unless it has been approved


## Build Requirements
- Understood the contributing guide
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
