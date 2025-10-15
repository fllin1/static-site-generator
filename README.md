# Static Site Generator

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square)

A Python-based static site generator built from scratch, similar to Hugo, Jekyll, or Gatsby.

## About

This project is a static site generator developed as part of the [Boot.dev Static Site Generator course](https://www.boot.dev/courses/build-static-site-generator-python). It demonstrates how SEO and performance-optimized static site generators work under the hood, applying object-oriented and functional programming concepts to build a tangible web development tool.

## Features

- **Markdown to HTML conversion**: Parse `.md` files and convert them to static HTML pages
- **Template system**: Apply customizable templates to generate consistent layouts
- **Static file handling**: Process and copy static assets (CSS, images, etc.)
- **File I/O operations**: Read source content and write generated HTML files
- **Content management**: Organize and structure website content efficiently

## Requirements

- Python 3.11+

## Installation

### Using uv (recommended)

```bash
# Install dependencies from pyproject.toml and uv.lock
uv sync
```

This will automatically create a virtual environment and install all dependencies specified in your `pyproject.toml` file.

### Manual setup

If you need to create the environment manually:

```bash
# Create a virtual environment with uv
uv venv --python 3.12

# Install dependencies
uv sync
```

## Usage

```bash
# Generate static site from source content
./build.sh # On Bash
```

The generator will:
1. Read Markdown files from the content directory
2. Parse and convert them to HTML
3. Apply templates for consistent styling
4. Output the generated static site to the public directory

## Project Structure

```
.
├── content/          # Source Markdown files
├── static/           # Static assets (CSS, images)
├── template.html     # HTML template
├── public/           # Generated static site output
└── main.py           # Main generator script
```

## How It Works

The static site generator follows a content-to-HTML pipeline:

1. **Content Parsing**: Reads Markdown files from the content directory
2. **Markdown Processing**: Converts Markdown syntax to HTML elements
3. **Template Application**: Injects processed content into HTML templates
4. **Static Asset Management**: Copies static files to the output directory
5. **Site Generation**: Writes final HTML pages to the public directory

## Learning Outcomes

This project demonstrates:
- Object-oriented design patterns in Python
- Functional programming techniques
- File system operations and I/O
- Text parsing and transformation
- Content templating systems
- Understanding of static site generation workflows

## Acknowledgments

This project was created following the guided tutorial from [Boot.dev](https://www.boot.dev/courses/build-static-site-generator-python), taught by Lane Wagner.

## License

This is an educational project. Please refer to the course materials for usage guidelines.
