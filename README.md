# KnowledgeGraphed

KnowledgeGraphed is an in-development, experimental knowledge graph generator. It converts text data in a `.txt` file to a knowledge graph using NetworkX and spaCy.

**STRICTLY EXPERIMENTAL, DO NOT USE IN PRODUCTION**

_Hack Club Arcade Reviewers, see [here](#arcade-reviewers)_

_Found a bug? Want a new feature? [Create an issue!](https://github.com/CragglesG/KnowledgeGraphed/issues/new) (Please check for an existing one first to avoid duplicates!)_

_Want to contribute? You can find good first issues [here](https://github.com/CragglesG/KnowledgeGraphed/contribute)._

## Table of Contents
- [Installation](#installation)
- [Commands](#commands)
- [Bugs & Limitations](#bugs-&-limitations)

## Installation
_KnowledgeGraphed only supports Linux at this time_

**Prerequisites:**
- Python 3 & pip
- Gephi
- Matplotlib
- NetworkX
- pydot

To quick-install KnowledgeGraphed into `~/.KnowledgeGraphed`, run the following command:

```
wget https://github.com/CragglesG/KnowledgeGraphed/blob/main/linux-install/install.sh && chmod +x install.sh && ./install.sh
```
Want to see what's happening under the hood? Take a look at the [install file](https://github.com/CragglesG/KnowledgeGraphed/blob/main/linux-install/install.sh).

## Commands

Once you've installed KnowledgeGraphed, you can use the three commands `kg-make`, `kg-extend`, and `kg-view` to make, extend, and view your knowledge graph.

### `kg-make`

`kg-make` is used to create a new knowledge graph from a text file. It will completely overwrite any existing knowledge graphs.

_Tip: When inputting a file, you must provide the full path._

### `kg-extend`
**USE WITH CAUTION, DOES NOT FUNCTION AS YOU MAY EXPECT**

`kg-extend` is used to extend an existing knowledge graph with a text file. It will error out if it cannot find an existing knowledge graph to extend.

_Tip: As with `kg-make`, you must provide the full path to the text file._

### `kg-view`

`kg-view` is used to view an existing knowledge graph. It uses `pydot`, `gephi`, and `matplotlib` to achieve this.

## Bugs & Limitations

As KnowledgeGraphed is still in-development and experimental, it has many bugs and limitations. Below is a non-exhaustive list of known issues and areas for improvement:
- `kg-extend` is buggy and does not function as desired
- `kg-view` can only display labels on nodes
- All knowledge graph information is stored unencrypted
- Testing of features is limited

<br><br><br><br><br><br><br>

#### Arcade Reviewers

When making KnowledgeGraphed, I used no AI. All of the code in KnowledgeGraphed is written by me, but I did use [this StackOverflow answer](https://stackoverflow.com/a/18522941) to assist me with the creation of `view.py` (I used it only as a guide).

**Thanks for reviewing my project!**

