# lateflat

**lateflat** is a command-line tool to flatten a LaTeX project into a single root directory, simplifying organization for project submission.

## Features
- Merges all files in a LaTeX project into a single directory.
- Updates `\include` and `\input` paths for compatibility in the flattened structure.
- Supports easy integration into CI/CD pipelines for automated submission preparations.

## Installation
Requires Python 3.7 or higher. Install using:

```bash
pip install lateflat
```

## Usage
To flatten a LaTeX project (including the article file named main.tex):

```bash
lateflat <path_to_your_latex_project>
```

This will organize all files in <path_to_your_latex_project> into a single main article file along with supplementary files (such as images, .sty, .cls, and .bib) in a submission-ready directory.

Additionally, it can output a zipped version of the flattened project directory if needed, making it easy to submit as a single article file along with supplementary files.

## License

This project is licensed under the terms of the Apache License. See [LICENSE](LICENSE) for details.

## Contributing

Feel free to contribute! Fork the repository, make a pull request, or open an issue to discuss potential features.

## Contact

Maintainer: [Nkzono99](mailto:j-nakazono@stu.kobe-u.ac.jp)

Repository: [GitHub - lateflat](https://github.com/Nkzono99/lateflat)
