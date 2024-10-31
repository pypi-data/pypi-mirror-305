import os
import json
import click
import ollama

CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".cliborg_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    else:
        return {"model": "llama3.1"}  # Default config

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

def ask_ollama(question, model):
    try:
        response = ollama.generate(model=model, prompt=question)
        return response['response']
    except Exception as e:
        return f"Error: {e}"

@click.group()
def cli():
    """Cliborg - A command-line interface for querying Ollama models."""
    pass

@cli.command()
@click.argument("question", required=False)
def ask(question):
    """Ask a question to the model."""
    if not question:
        click.echo("Please provide a question. Usage: cliborg ask 'your question'")
        return
    
    config = load_config()
    model = config.get("model", "llama3.1")
    answer = ask_ollama(question, model)
    click.echo(f"Answer: {answer}")

@cli.command()
@click.argument("model_name", required=True)
def config(model_name):
    """Configure the default model."""
    configure_model(model_name)
    click.echo(f"Configuration updated: model set to {model_name}")

@cli.command()
def show_config():
    """Show the current configuration."""
    config = load_config()
    click.echo(f"Current configuration: {json.dumps(config, indent=4)}")

def configure_model(model_name):
    config = load_config()
    config["model"] = model_name
    save_config(config)

if __name__ == "__main__":
    cli()
