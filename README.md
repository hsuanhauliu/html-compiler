# HTML Compiler

A simple and lightweight html compiling program. The purpose of this program is to combine several html files into one, allowing the users to manage their content better.

## How It Works
The program recursively looks for tags that has a specific class (m_component) and replace the current tag with the html file specified in the id.
For example,

```
<!-- will be replaced by the content of header.html file>
<div id="header" class="m_component"></div>

<!-- will be replaced by the content of content.html file>
<div id="content" class="m_component"></div>
```

The user needs to input which html file to start as the root file. Consider a directory tree like this:

```
.
+-- index.html
+-- header.html
+-- content.html
+-- content
|   +-- block_1.html
|   +-- block_2.html
```

Say my index.html is my root file, it might contain tags such as

```
<div id="header" class="m_component"></div>
<div id="content" class="m_component"></div>
```

My content.html might contain tags such as

```
<div id="content/block_1" class="m_component"></div>
<div id="content/block_2" class="m_component"></div>
```

Note that the filename in the id does not need to have the html extension, and is a relative path to the file. The default name for the compiled file is "output.html".

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

See [here](requirements.txt) for a complete list of required packages.
- Python >= 3.7
- BeautifulSoup >= 4.8.1


### Installation

A step by step series of examples that tell you how to get a development env running.

```
# Install all packages.
pip install -r requirements.txt

# Build from source.
git clone https://github.com/hsuanhauliu/html-compiler.git
cd html-compiler
pip install .
```

### Usage

#### CLI

To use the program, simply type

```
html-compiler <root-filename> [-o output]
```

Example:
```
html-compiler index.html
```
