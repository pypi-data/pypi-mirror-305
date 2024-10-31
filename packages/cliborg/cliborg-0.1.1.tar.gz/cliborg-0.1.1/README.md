
# Cliborg - A Command-Line Interface for Ollama Models

Cliborg is a simple command-line tool that lets you interact with locally hosted Ollama language models. You can ask questions to the model, configure the default model, and manage your preferences via a configuration file.

## Installation

To install Cliborg, make sure you have [Ollama](https://ollama.com) and `click` installed on your system.

```bash
pip install click ollama
```

## Usage

Once installed, you can use Cliborg to interact with your Ollama models. The following commands are available:

### Ask a Question

You can ask questions directly to the model by using the `ask` command:

```bash
cliborg ask "What is the capital of Japan?"
```

### Configure Default Model

To set the default model for future queries, use the `config` command:

```bash
cliborg config llama3.1
```

### Show Configuration

To view the current configuration, including the model being used:

```bash
cliborg show_config
```

## Configuration

Cliborg stores its configuration in a `.cliborg_config.json` file located in the user's home directory. This file allows you to save preferences like the default model, which is used across sessions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
