# Kubiya SDK

Kubiya SDK is a powerful Python library for creating, managing, and executing workflows and tools. It provides a flexible and intuitive interface for defining complex workflows, integrating various tools, and managing their execution.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Key Concepts](#key-concepts)
- [Creating Workflows](#creating-workflows)
- [Defining Tools](#defining-tools)
- [Executing Workflows](#executing-workflows)
- [Visualization](#visualization)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Key Concepts
- **Teammates**: AI-powered virtual workers to whom you can delegate technical operations tasks.
- **Tools**: Reusable functions that can be integrated into workflows and teammate agents.
- **Workflows**: Sequences of steps that process and transform data.
- **Steps**: Individual units of work within a workflow.
- **State**: The data passed between steps in a workflow.


## Installation

To install the Kubiya SDK, use pip:

```bash
pip install kubiya-sdk
```

if you want you can install with extra server command to set up an API server for the SDK

```bash
pip install kubiya-sdk[server]
```

## Quick Start

### Creates a tool
Here's a simple example how to create a new tool.

Use kubiya cli `init` command and create a basic template.

```bash
kubiya init
````
It creates a new folder with the following structure needed for the tool.

```bash
/my-new-amazing-tool
│
├── /tools
│   ├── /function_tool
│   │   ├── main.py       # example for function tool
│   │
│   ├── /hello_world_tool # example for basic tool
│   │   ├── main.py
│   │   └── tool_def
│   └──
│
```

After you finish editing your tools you can use `bundle` command to scan and bundle yours Kubiya's tools in the project

```bash
kubiya bundle
```
The command will scan for tools in the project, check if there are some errors and create an `kubiya_bundle.json` file in the root folder.
example of the output:
```bash
Python Version: 3.11.10
Tools Discovered: 2
                            Tools Summary
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┓
┃ Tool Name                      ┃ Args ┃ Env Vars ┃ Secrets ┃ Files ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━┩
│ test_123                       │  3   │    0     │    0    │   1   │
│ say_hello                      │  1   │    0     │    0    │   1   │
└────────────────────────────────┴──────┴──────────┴─────────┴───────┘
No Errors
```

Now you can create a new resource via https://kubiya.ai and integrate them with your teammate agent :)

## API Reference

For detailed API documentation, please refer to our [API Reference](https://docs.kubiya.ai/api-reference).

## Examples

### Complex Workflow Example

Here's an example of a more complex workflow that demonstrates various features of the Kubiya SDK:

```python
from kubiya_sdk.workflows import StatefulWorkflow
from kubiya_sdk.tools import register_tool

@register_tool(name="DataFetcher", description="Fetches data from an API")
async def fetch_data(api_url: str) -> dict:
    # Simulated API call
    return {"data": f"Data from {api_url}"}

@register_tool(name="DataProcessor", description="Processes fetched data")
def process_data(data: str) -> dict:
    return {"processed_data": f"Processed: {data}"}

workflow = StatefulWorkflow("ComplexWorkflow")

@workflow.step("fetch_step")
async def fetch_step(state):
    tool = workflow.get_tool("DataFetcher")
    result = await tool.execute(api_url=state["api_url"])
    return {"fetched_data": result["data"]}

@workflow.step("process_step")
def process_step(state):
    tool = workflow.get_tool("DataProcessor")
    result = tool.execute(data=state["fetched_data"])
    return {"processed_data": result["processed_data"]}

@workflow.step("decision_step")
def decision_step(state):
    data_length = len(state["processed_data"])
    return {"data_length": data_length}

@workflow.step("short_data_step")
def short_data_step(state):
    return {"result": f"Short data: {state['processed_data']}"}

@workflow.step("long_data_step")
def long_data_step(state):
    return {"result": f"Long data: {state['processed_data'][:50]}..."}

workflow.add_edge("fetch_step", "process_step")
workflow.add_edge("process_step", "decision_step")
workflow.add_condition("decision_step", "state['data_length'] < 50", "short_data_step")
workflow.add_condition("decision_step", "state['data_length'] >= 50", "long_data_step")

# Execution
result = await workflow.run({"api_url": "https://api.example.com/data"})
print(result)
```

This example demonstrates:
- Tool registration and usage
- Multiple workflow steps
- Conditional branching based on state
- Asynchronous operations

## Contributing

We welcome contributions to the Kubiya SDK! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

Kubiya SDK is released under the [MIT License](LICENSE).
