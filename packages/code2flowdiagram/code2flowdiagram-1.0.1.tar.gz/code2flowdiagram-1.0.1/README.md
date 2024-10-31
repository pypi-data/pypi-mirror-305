<div style="padding: 20px; background: #333333; margin-bottom: 20px;">

❗ **Important Note:**

All credit of this code goes to the original creator which can be found at https://github.com/scottrogowski/code2flow

I have made a small change which includes the Graphviz libraries in the package so as to not rely on having Graphviz installed.

The version of Graphviz is the latest at the time of this commit. The files downloaded can be found at https://graphviz.org/download/

The downloaded files are stored in the code2flowdiagram/graphviz folder.

In order to publish the package on PyPi I have renamed the package to code2flowdiagram.

</div>

![Version 2.5.1](https://img.shields.io/badge/version-2.5.1-brightgreen) ![Build passing](https://img.shields.io/badge/build-passing-brightgreen) ![Coverage 100%](https://img.shields.io/badge/coverage-100%25-brightgreen) ![License MIT](https://img.shields.io/badge/license-MIT-green])

code2flowdiagram generates [call graphs](https://en.wikipedia.org/wiki/Call_graph) for dynamic programming language. code2flowdiagram supports Python, JavaScript, Ruby, and PHP.

The basic algorithm is simple:

1. Translate your source files into ASTs.
1. Find all function definitions.
1. Determine where those functions are called.
1. Connect the dots.

code2flowdiagram is useful for:

- Untangling spaghetti code.
- Identifying orphaned functions.
- Getting new developers up to speed.

code2flowdiagram provides a _pretty good estimate_ of your project's structure. No algorithm can generate a perfect call graph for a [dynamic language](https://en.wikipedia.org/wiki/Dynamic_programming_language) – even less so if that language is [duck-typed](https://en.wikipedia.org/wiki/Duck_typing). See the known limitations in the section below.

_(Below: code2flowdiagram running against a subset of itself `code2flowdiagram code2flowdiagram/engine.py code2flowdiagram/python.py --target-function=code2flowdiagram --downstream-depth=3`)_

![code2flowdiagram running against a subset of itself](https://raw.githubusercontent.com/scottrogowski/code2flowdiagram/master/assets/code2flowdiagram_output.png)

## Installation

```bash
pip3 install code2flowdiagram
```

If you don't have it already, you will also need to install graphviz. Installation instructions can be found [here](https://graphviz.org/download/).

Additionally, depending on the language you want to parse, you may need to install additional dependencies:

- JavaScript: [Acorn](https://www.npmjs.com/package/acorn)
- Ruby: [Parser](https://github.com/whitequark/parser)
- PHP: [PHP-Parser](https://github.com/nikic/PHP-Parser)
- Python: No extra dependencies needed

## Usage

To generate a DOT file, run something like:

```bash
code2flowdiagram mypythonfile.py
```

Or, for Javascript:

```bash
code2flowdiagram myjavascriptfile.js
```

You can specify multiple files or import directories:

```bash
code2flowdiagram project/directory/source_a.js project/directory/source_b.js
```

```bash
code2flowdiagram project/directory/*.js
```

```bash
code2flowdiagram project/directory --language js
```

To pull out a subset of the graph, try something like:

```bash
code2flowdiagram mypythonfile.py --target-function my_func --upstream-depth=1 --downstream-depth=1
```

There are a ton of command line options, to see them all, run:

```bash
code2flowdiagram --help
```

## How code2flowdiagram works

code2flowdiagram approximates the structure of projects in dynamic languages. It is _not possible_ to generate a perfect callgraph for a dynamic language.

Detailed algorithm:

1. Generate an AST of the source code
2. Recursively separate groups and nodes. Groups are files, modules, or classes. More precisely, groups are namespaces where functions live. Nodes are the functions themselves.
3. For all nodes, identify function calls in those nodes.
4. For all nodes, identify in-scope variables. Attempt to connect those variables to specific nodes and groups. This is where there is some ambiguity in the algorithm because it is impossible to know the types of variables in dynamic languages. So, instead, heuristics must be used.
5. For all calls in all nodes, attempt to find a match from the in-scope variables. This will be an edge.
6. If a definitive match from in-scope variables cannot be found, attempt to find a single match from all other groups and nodes.
7. Trim orphaned nodes and groups.
8. Output results.

## Why is it impossible to generate a perfect call graph?

Consider this toy example in Python

```python
def func_factory(param):
    if param < .5:
        return func_a
    else:
        return func_b

func = func_factory(important_variable)
func()
```

We have no way of knowing whether `func` will point to `func_a` or `func_b` until runtime. In practice, ambiguity like this is common and is present in most non-trivial applications.

## Known limitations

code2flowdiagram is internally powered by ASTs. Most limitations stem from a token not being named what code2flowdiagram expects it to be named.

- All functions without definitions are skipped. This most often happens when a file is not included.
- Functions with identical names in different namespaces are (loudly) skipped. E.g. If you have two classes with identically named methods, code2flowdiagram cannot distinguish between these and skips them.
- Imported functions from outside your project directory (including from standard libraries) which share names with your defined functions may not be handled correctly. Instead, when you call the imported function, code2flowdiagram will link to your local functions. For example, if you have a function `search()` and call, `import searcher; searcher.search()`, code2flowdiagram may link (incorrectly) to your defined function.
- Anonymous or generated functions are skipped. This includes lambdas and factories.
- If a function is renamed, either explicitly or by being passed around as a parameter, it will be skipped.

## As an imported library

You can work with code2flowdiagram as an imported Python library in much the same way as you work with it
from the CLI.

```python
import code2flowdiagram
code2flowdiagram.code2flowdiagram(['path/to/filea', 'path/to/fileb'], 'path/to/outputfile')
```

The keyword arguments to `code2flowdiagram.code2flowdiagram` are roughly the same as the CLI
parameters. To see all available parameters, refer to the code2flowdiagram function in [engine.py](https://github.com/scottrogowski/code2flowdiagram/blob/master/code2flowdiagram/engine.py).

## How to contribute

1. **Open an issue**: code2flowdiagram is not perfect and there is a lot that can be improved. If you find a problem parsing your source that you can identify with a simplified example, please open an issue.
2. **Create a PR**: Even better, if you have a fix for the issue you identified that passes unit tests, please open a PR.
3. **Add a language**: While dense, each language implementation is between 250-400 lines of code including comments. If you want to implement another language, the existing implementations can be your guide.

## Unit tests

Test coverage is 100%. To run:

```bash
    pip install -r requirements_dev.txt
    make test
```

## License

code2flowdiagram is licensed under the MIT license.
Prior to the rewrite in April 2021, code2flowdiagram was licensed under LGPL. The last commit under that license was 24b2cb854c6a872ba6e17409fbddb6659bf64d4c.
The April 2021 rewrite was substantial, so it's probably reasonable to treat code2flowdiagram as completely MIT-licensed.

## Acknowledgements

- In mid 2021, code2flowdiagram was rewritten, and two new languages were added. This was prompted and financially supported by the [Sider Corporation](https://siderlabs.com/).
- The code2flowdiagram pip name was graciously transferred to this project from [Dheeraj Nair](https://github.com/Dheeraj1998). He was using it for his own (unrelated) [code2flowdiagram](https://github.com/Dheeraj1998/code2flowdiagram) project.
- Many others have contributed through bug fixes, cleanups, and identifying issues. Thank you!!!

## Unrelated projects

The name, "code2flowdiagram", has been used for several unrelated projects. Specifically, the domain, code2flowdiagram.com, has no association with this project. I've never heard anything from them and it doesn't appear like they use anything from here.

## Feedback / Issues / Contact

If you have an issue using code2flowdiagram or a feature request, please post it in the issues tab. In general, I don't provide help over email. Answering a question publicly helps way more people. For everything else, please do email! scottmrogowski@gmail.com

## Feature Requests

Email me. Usually, I'm spread thin across a lot of projects, so I will, unfortunately, turn down most requests. However, I am open to paid development for compelling features.
