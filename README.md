# KnowledgeGraphed

KnowledgeGraphed is an experimental knowledge graph generator. It converts text data in a `.txt` file to a knowledge graph using NetworkX and spaCy.

**STRICTLY EXPERIMENTAL, DO NOT USE IN PRODUCTION**

_Found a bug? Want a new feature? [Create an issue!](https://github.com/CragglesG/KnowledgeGraphed/issues/new) (Please check for an existing one first to avoid duplicates!)_

_Want to contribute? You can find good first issues [here](https://github.com/CragglesG/KnowledgeGraphed/contribute)._

![Demo Image](https://cloud-occozlw00-hack-club-bot.vercel.app/0image.png)

_A simple demo of `kg-view`_

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
**USE WITH CAUTION, MAY NOT FUNCTION AS YOU EXPECT**

`kg-extend` is used to extend an existing knowledge graph with a text file. It will error out if it cannot find an existing knowledge graph to extend.

_Tip: As with `kg-make`, you must provide the full path to the text file._

### `kg-view`

`kg-view` is used to view an existing knowledge graph. It uses pydot, gephi, and matplotlib to achieve this.

## Bugs & Limitations

As KnowledgeGraphed is only experimental, it has many bugs and limitations. Below is a non-exhaustive list of known issues and areas for improvement:
- `kg-extend` is buggy and does not function as desired
- `kg-view` can only display labels on nodes, not edges
- All knowledge graph information is stored unencrypted
- Testing of features is limited
