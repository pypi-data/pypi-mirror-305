import llm
import click
import os
from pathlib import Path
import toml
from importlib import resources
from typing import List, Optional

# Update these lines to use just the filename
DEFAULT_FEW_SHOT_PROMPT_FILE = "few_shot_prompt.xml"
MODEL_FEW_SHOT_PROMPT_FILE = "few_shot_prompt.xml"
UTILITY_FEW_SHOT_PROMPT_FILE = "few_shot_prompt.xml"
# print the path of DEFAULT_FEW_SHOT_PROMPT_FILE
print(DEFAULT_FEW_SHOT_PROMPT_FILE)
def read_few_shot_prompt(file_name: str) -> str:
    """
    Read the content of a few-shot prompt file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The content of the file, or an empty string if the file is not found.
    """
    try:
        return resources.read_text("llm_plugin_generator", file_name)
    except FileNotFoundError:
        click.echo(f"Warning: Few-shot prompt file not found: {file_name}.")
        return ""

def write_main_python_file(content: str, output_dir: Path, filename: str) -> None:
    """
    Write the content to a Python file in the specified output directory.

    Args:
        content (str): The content to write to the file.
        output_dir (Path): The directory where the file should be written.
        filename (str): The name of the file to create.
    """
    main_file = output_dir / filename
    with main_file.open("w") as f:
        f.write(content)
    click.echo(f"Main Python file written to {main_file}")

def write_readme(content: str, output_dir: Path) -> None:
    """
    Write the content to a README.md file in the specified output directory.

    Args:
        content (str): The content to write to the README file.
        output_dir (Path): The directory where the file should be written.
    """
    readme_file = output_dir / "README.md"
    with readme_file.open("w") as f:
        f.write(content)
    click.echo(f"README file written to {readme_file}")

def write_pyproject_toml(content: str, output_dir: Path) -> None:
    """
    Write the content to a pyproject.toml file in the specified output directory.

    Args:
        content (str): The content to write to the pyproject.toml file.
        output_dir (Path): The directory where the file should be written.
    """
    pyproject_file = output_dir / "pyproject.toml"
    with pyproject_file.open("w") as f:
        f.write(content)
    click.echo(f"pyproject.toml file written to {pyproject_file}")

def extract_plugin_name(pyproject_content: str) -> str:
    """
    Extract the plugin name from the pyproject.toml content.

    Args:
        pyproject_content (str): The content of the pyproject.toml file.

    Returns:
        str: The extracted plugin name, converted to snake_case.
    """
    try:
        pyproject_dict = toml.loads(pyproject_content)
        name = pyproject_dict['project']['name']
        # Convert kebab-case to snake_case
        return name.replace('-', '_')
    except:
        # If parsing fails, return a default name
        return "plugin"

@llm.hookimpl
def register_commands(cli: click.Group) -> None:
    """
    Register the generate_plugin command with the LLM CLI.

    Args:
        cli (click.Group): The CLI group to which the command should be added.
    """
    @cli.command()
    @click.argument("prompt", required=False)
    @click.argument("input_files", nargs=-1, type=click.Path(exists=True))
    @click.option("--output-dir", type=click.Path(), default=".", help="Directory to save generated plugin files")
    @click.option("--type", default="default", type=click.Choice(["default", "model", "utility"]), help="Type of plugin to generate")
    @click.option("--model", "-m", help="Model to use")
    def generate_plugin(prompt: Optional[str], input_files: List[str], output_dir: str, type: str, model: Optional[str]) -> None:
        """Generate a new LLM plugin based on examples and a prompt or README file(s)."""
        # Select the appropriate few-shot prompt file based on the type
        if type == "model":
            few_shot_file = MODEL_FEW_SHOT_PROMPT_FILE
        elif type == "utility":
            few_shot_file = UTILITY_FEW_SHOT_PROMPT_FILE
        else:
            few_shot_file = DEFAULT_FEW_SHOT_PROMPT_FILE

        few_shot_prompt = read_few_shot_prompt(few_shot_file)
        
        input_content = ""
        for input_file in input_files:
            with open(input_file, "r") as f:
                input_content += f"""Content from {input_file}:
{f.read()}

"""
        if prompt:
            print(f"Prompt: {prompt}")
            input_content += f"""Additional prompt:
{prompt}
"""

        if not input_content:
            input_content = click.prompt("Enter your plugin description or requirements")
        
        llm_model = llm.get_model(model)
        response = llm_model.prompt(
            f"""Generate a new LLM plugin based on the following few-shot examples and the given input:
Few-shot examples:
{few_shot_prompt}

Input:
{input_content}

Generate the plugin code, including the main plugin file, README.md, and pyproject.toml. 
Ensure the generated plugin follows best practices and is fully functional. 
Provide the content for each file separately, enclosed in XML tags like <plugin_py>, <readme_md>, and <pyproject_toml>."""
        )
        
        generated_plugin = response.text()
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        plugin_py_content = extract_content(generated_plugin, "plugin_py")
        readme_content = extract_content(generated_plugin, "readme_md")
        pyproject_content = extract_content(generated_plugin, "pyproject_toml")
        
        # Extract the plugin name from pyproject.toml
        plugin_name = extract_plugin_name(pyproject_content)
        
        # Use the extracted name for the main Python file
        write_main_python_file(plugin_py_content, output_path, f"{plugin_name}.py")
        write_readme(readme_content, output_path)
        write_pyproject_toml(pyproject_content, output_path)
        
        click.echo("Plugin generation completed.")

def extract_content(text: str, tag: str) -> str:
    """
    Extract content enclosed in XML-like tags from a string.

    Args:
        text (str): The text to search for tagged content.
        tag (str): The tag name to look for.

    Returns:
        str: The content between the opening and closing tags, or an empty string if not found.
    """
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    start = text.find(start_tag) + len(start_tag)
    end = text.find(end_tag)
    return text[start:end].strip() if start != -1 and end != -1 else ""

@llm.hookimpl
def register_models(register):
    pass  # No custom models to register for this plugin

@llm.hookimpl
def register_prompts(register):
    pass  # No custom prompts to register for this plugin
