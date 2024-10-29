import re
import random

def transform_graph_spec(graph_spec: str) -> str:
    lines = graph_spec.split("\n")
    transformed_lines = []

    for line in lines:
        # Remove comments from the line
        line = line.split('#')[0].strip()
        
        if not line or line[0] in ["-", "/"]:
            continue
        if "=>" in line and not line[0].isspace():
            parts = line.split("=>")
            if parts[0].strip():
                transformed_lines.append(parts[0].strip())
                transformed_lines.append(f"  => {parts[1].strip()}")
            else:
                transformed_lines.append(line)
        else:
            transformed_lines.append(line)

    return "\n".join(transformed_lines)


def parse_string(input_string):
    pattern = r"\[(\w+)\((\w+) in (\w+)\)\]"
    match = re.match(pattern, input_string)

    if match:
        function, var_name, state_field = match.groups()
        return function, var_name, state_field
    else:
        raise ValueError("String format is incorrect")


def parse_graph_spec(graph_spec):
    graph_spec = transform_graph_spec(graph_spec)
    TRUE_FN = "true_fn"
    graph = {}
    current_node = None
    state = None
    start_node = None

    for line in graph_spec.strip().split("\n"):
        line = line.strip()
        if not line:
            continue

        if "=>" in line:
            if line.startswith("=>"):
                condition = TRUE_FN
                destination = line.split("=>")[1].strip()
                graph[current_node]["edges"].append(
                    {"condition": condition, "destination": destination}
                )
            else:
                parts = line.split("=>")
                condition = parts[0].strip()
                destination = parts[1].strip()
                graph[current_node]["edges"].append(
                    {"condition": condition, "destination": destination}
                )
        elif "(" in line:
            node_info = line.split("(")
            current_node = node_info[0].strip()
            start_node = current_node
            state = node_info[1].strip(")")
            graph[current_node] = {"state": state, "edges": []}
        else:
            current_node = line
            graph[current_node] = {"state": state, "edges": []}
    return graph, start_node


def all_true_fn(edges):
    return all(edge["condition"] == "true_fn" for edge in edges)


def mk_conditions(node_name, node_dict):
    edges = node_dict["edges"]
    state_type = node_dict["state"]

    # Special case: single 'true_fn' condition
    if all_true_fn(edges):
        return ""

    function_body = [f"def after_{node_name}(state: {state_type}):"]

    for i, edge in enumerate(edges):
        condition = edge["condition"]
        destination = edge["destination"]

        if "," in destination:
            # Split the destination by commas and strip spaces
            destinations = [d.strip() for d in destination.split(",")]
            # Format the return statement with a list
            return_statement = f"return {destinations}"
        else:
            # Format the return statement with a single value
            return_statement = f"return '{destination}'"

        if condition == "true_fn":
            function_body.append(f"    {return_statement}")
            break  # Exit the loop as this is always true
        elif i == 0:
            function_body.append(f"    if {condition}(state):")
        else:
            function_body.append(f"    elif {condition}(state):")

        function_body.append(f"        {return_statement}")

    # Only add the else clause if we didn't encounter 'true_fn'
    if condition != "true_fn":
        if len(edges) > 1:
            function_body.append("    else:")
            function_body.append('        raise ValueError("No destination")')
        else:
            function_body.append("    return END")
    function_body.append("")

    return "\n".join(function_body)


def mk_conditional_edges(graph_name, node_name, node_dict):
    edges = node_dict["edges"]

    # Case 1: parallel output
    if all_true_fn(edges):
        edge_code = ""
        for edge in edges:
            destination = edge["destination"]
            if destination == "END":
                edge_code += f"{graph_name}.add_edge('{node_name}', END)\n"
            elif "," in destination:
                data = destination.split(",")
                for x in data:
                    x = x.strip()
                    edge_code += f"{graph_name}.add_edge('{node_name}', '{x}')\n"
            elif "[" in destination:
                function, var_name, state_field = parse_string(destination)
                edge_code += f"def after_{node_name}(state):\n"
                edge_code += f"    return [Send('{function}', {{'{var_name}': s}}) for s in state['{state_field}']]\n"
                edge_code += f"{graph_name}.add_conditional_edges('{node_name}', after_{node_name}, ['{function}'])\n"
            else:
                if "," in node_name:
                    nodes = [f"'{n.strip()}'" for n in node_name.split(",")]
                    edge_first_node_name = f"[{','.join(nodes)}]"
                else:
                    edge_first_node_name = (
                        f"'{node_name}'" if node_name != "START" else "START"
                    )
                edge_code += (
                    f"{graph_name}.add_edge({edge_first_node_name}, '{destination}')\n"
                )
        return edge_code.rstrip()

    # Case 2: Multiple conditions
    else:
        # Helper function to create dictionary entries
        def maybe_multiple(s):
            if "," in s:
                data = s.split(",")
                quoted = [f"'{x.strip()}'" for x in data]
                return "[" + ",".join(quoted) + "]"
            else:
                return f"'{s}'"

        def mk_entry(edge):
            if edge["destination"] == "END":
                return f"'{edge['destination']}': END"
            else:
                return f"'{edge['destination']}': {maybe_multiple(edge['destination'])}"

        # Create the dictionary string
        dict_entries = ", ".join([mk_entry(e) for e in edges])
        # If there's a single edge with a condition, dict needs END: END
        if len(edges) == 1 and edges[0]["condition"] != "true_fn":
            dict_entries += ", END: END"
        node_dict_str = f"{node_name}_dict = {{{dict_entries}}}"
        multiple = any("," in edge["destination"] for edge in edges)
        if multiple:
            # not really understanding, but it seems that in this case, we just have a list of
            # nodes instead of a dict for third parameter
            s = set()
            for edge in edges:
                destinations = edge["destination"].split(",")
                for dest in destinations:
                    s.add(dest.strip())
            node_dict_str = f"{node_name}_dict = {list(s)}"

        # Create the add_conditional_edges call
        add_edges_str = f"{graph_name}.add_conditional_edges('{node_name}', after_{node_name}, {node_name}_dict)"

        return f"{node_dict_str}\n{add_edges_str}\n"


def true_fn(state):
    return True

def gen_node(node_name, state_type):
    return f"""
def {node_name}(state: {state_type}, *, config:Optional[RunnableConfig] = None):
    return {{ 'states': state['states'] + ['{node_name}'], 'last_state': '{node_name}' }}
"""

def gen_nodes(graph):
    nodes = []
    for node_name, node_data in graph.items():
        if node_name != "START":
            state_type = node_data.get('state_type', 'default')
            nodes.append(gen_node(node_name, state_type))
    return "\n".join(nodes)

def find_conditions(node_dict):
    edges = node_dict["edges"]
    conditions = []
    for edge in edges:
        if 'true_fn' != edge["condition"]:
            conditions.append(edge["condition"])
    return conditions


def random_one_or_zero():
    return random.choice([False, True])

def gen_condition(condition, state_type):
    return f"""
def {condition}(state: {state_type}) -> bool:
    return random_one_or_zero()
"""

def gen_conditions(graph_spec):
    graph, start_node = parse_graph_spec(graph_spec)
    conditions = []
    state_type = graph[start_node]["state"]
    for node_name, node_dict in graph.items():
        for condition in find_conditions(node_dict):
            conditions.append(gen_condition(condition, state_type))
    result = "# GENERATED CODE -- used for graph simulation mode"
    return result + "\n".join(conditions) if conditions else "# This graph has no conditional edges"

def mk_state(state_class):
    return f"""
# GENERATED CODE: mock graph state
from typing import Annotated, TypedDict
from langgraph.graph import add_state

class {state_class}(TypedDict):
    states: Annotated[list[str], add_state]
    last_state: str
"""

def gen_state(graph_spec):
    graph, start_node = parse_graph_spec(graph_spec)
    return mk_state(graph[start_node]["state"])

def gen_graph(graph_name, graph_spec, compile_args=None):
    if not graph_spec: return ""
    graph, start_node = parse_graph_spec(graph_spec)
    nodes_added = []

    # Generate the graph state, node definitions, and entry point
    graph_setup = f"# GENERATED code, creates compiled graph: {graph_name}\n"
    graph_setup += """from langgraph.graph import START, END, StateGraph\n""" 

    state_type = graph[start_node]['state']
    graph_setup += f"{graph_name} = StateGraph({state_type})\n"
    if state_type == "MessageGraph":
        graph_setup = f"{graph_name} = MessageGraph()\n"

    for node_name in graph:
        if node_name != "START":
            if "," in node_name:
                node_names = [n.strip() for n in node_name.split(",")]
                for nn in node_names:
                    if nn not in nodes_added:
                        nodes_added.extend(nn)
                        graph_setup += f"{graph_name}.add_node('{nn}', {nn})\n"
            elif node_name not in nodes_added:
                nodes_added.extend(node_name)
                graph_setup += f"{graph_name}.add_node('{node_name}', {node_name})\n"
    if start_node != "START":
        graph_setup += f"\n{graph_name}.set_entry_point('{start_node}')\n\n"

    # Generate the code for edges and conditional edges
    node_code = []
    for node_name, node_dict in graph.items():
        conditions = mk_conditions(node_name, node_dict)
        if conditions:
            node_code.append(conditions)
        conditional_edges = mk_conditional_edges(graph_name, node_name, node_dict)
        if conditional_edges:
            node_code.append(conditional_edges)

    compile_args = compile_args if compile_args else ""
    return (
        graph_setup
        + "\n".join(node_code)
        + "\n\n"
        + f"{graph_name} = {graph_name}.compile({compile_args})"
    )
