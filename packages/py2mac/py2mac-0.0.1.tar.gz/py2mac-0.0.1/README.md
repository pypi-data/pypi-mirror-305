# Py2Mac

A Python Interface to macOS Accessibility API for **UI Automation** and **AI Agents**.

## Overview

**Py2Mac** was developed with the primary goal of enabling seamless **data extraction**, **automation**, and the
creation of **autonomous AI agents** that can directly interact with the computer via macOS Accessibility APIs. This
package simplifies integration with the macOS Accessibility API, making it more accessible from Python. Additionally,
Py2Mac includes tools for data cleanup and processing to improve data quality for large language models (LLMs) and
integrates with [LangChain](https://github.com/langchain-ai/langchain) for building AI Agents capable of interacting with UIs.

One of Py2Mac's key advantages is its reliance on the text-based accessibility tree, which allows it to interact with
the UI without needing vision-language models (VLMs). By leveraging the same accessibility tools that allow individuals
with disabilities to use a computer, Py2Mac enables UI interaction solely through text and accessibility data, making it
compatible with any LLM, including open-source models. This approach illustrates the rationale behind the package: if
accessibility tools can support effective computer use, an AI agent should also be able to interact with the UI
independently of VLMs, providing a flexible solution for building autonomous agents.

## Features

* UI Interaction: Access and manipulate UI elements programmatically.
* Data Processing: Clean and process data to make it more suitable for LLM integrations.
* LangChain Integration: Use LangChain tools and examples to build AI Agents capable of interacting with the computer.

## Installation

```
pip install py2mac
```

## Getting Started

### Prerequisites

* macOS System with accessibility permissions enabled for your Python interpreter.
* Python 3.11+ installed on your system.

### Enabling Accessibility Permissions

* Open `System Preferences > Security & Privacy > Privacy tab`.
* Select Accessibility from the left panel.
* Click the lock icon to make changes and enter your password.
* Click the + button and add your Python interpreter (e.g., /usr/local/bin/python3).

## IMPORTANT: Disclaimer

**Full System Access**: This package grants access to system applications and data, including the ability to read data
from applications, interact with their user interfaces, and access minimized or backgrounded apps. Exercise caution to
prevent unintentional exposure of sensitive information or unintended actions, especially when using the package with an
AI agent or automation.

**Data Privacy**: Avoid leaking personal or sensitive information, such as passwords or private files, especially when
integrating with external services or APIs.

**Require User Confirmation**: For safety and control, no action should be executed by AI agents or automations without
explicit user confirmation.

## Basic Usage

### Accessing Running Applications

```python
from py2mac.application import get_running_applications

# Get all running applications
apps = get_running_applications()
for app in apps:
    print(app.localized_name, app.pid)
```

### Interacting with the Frontmost Application

```python
from py2mac.application import Application

# Get the frontmost application (the one currently in focus)
app = Application.from_frontmost_app()
print(f"Interacting with: {app.localized_name}")

# Refresh the UI element tree
app.refresh_ui_tree()

# Access the root UI element
root_element = app.root_ui_element
```

## Working with UI Elements

### Exploring UI Elements

```python
# Convert the UI tree to a dictionary
ui_tree = root_element.asdict()
print(ui_tree)
```

### Accessing Specific UI Elements

```python
# Get a UI element by its unique ID
element_id = 'AXButton__OK__123456789'  # Replace with the actual ID
ui_element = app.get_ui_element(element_id)

# Print element attributes
print(ui_element.AXTitle)
print(ui_element.AXRole)
```

### Performing Actions on UI Elements

```python
# Perform an action (e.g., press a button)
try:
    ui_element.AXPress()
    print("Action performed successfully.")
except UIActionError as e:
    print(f"Failed to perform action: {e}")
```

## Building AI Agents

Py2Mac allows you to create AI agents that can observe and interact with macOS applications.

```python
from py2mac.application import Application

# Get the frontmost application
app = Application.from_frontmost_app()

# Observe the application's UI
app.refresh_ui_tree()
ui_tree = app.root_ui_element.asdict()

# Use an AI model to decide on actions (pseudo-code)
from your_ai_module import YourAIAgent

agent = YourAIAgent()
action = agent.decide_action(ui_tree)

# Perform the action
ui_element = app.get_ui_element(action['element_id'])
getattr(ui_element, action['action_name'])()
```

Note: Replace your_ai_module and YourAIAgent with your actual AI implementation.

### Data Processing for LLMs

Clean and process UI data to make it more suitable for LLMs.

```python
from py2mac.data_processing import clean_ui_data

# Obtain the raw UI data
raw_data = app.root_ui_element.asdict()

# Clean the data
clean_data = clean_ui_data(raw_data)
# Now `clean_data` is optimized for LLM input
```

## LangChain Integration

TODO

## Examples

For more examples, explore the [examples](/examples) directory.

## Contributing

Contributions are welcome! To contribute:

* Fork the repository.
* Create a new branch (git checkout -b feature/YourFeature).
* Commit your changes (git commit -am 'Add your feature').
* Push to the branch (git push origin feature/YourFeature).
* Open a pull request.

## Roadmap

- [ ] Improve performance.
- [ ] Improve clean_ui_data - make configurable.
- [ ] Improve clean_ui_data - add more processing options.

Thank you for using Py2Mac! We hope this package helps you develop macOS UI automation and AI agents.
