# EXAMPLE TRANSFORMATION FOR DENESTING A NODE
# De-nest each list node up to record level
def denest_list_nodes(this_json, data_key, list_nodes):
    new_json = this_json
    i = 0
    for record in list(this_json.get(data_key, [])):
        for list_node in list_nodes:
            this_node = record.get(list_node, {}).get(list_node, [])
            if not this_node == []:
                new_json[data_key][i][list_node] = this_node
            else:
                new_json[data_key][i].pop(list_node)
        i = i + 1
    return new_json


# Run other transforms, as needed: denest_list_nodes, transform_conversation_parts
def transform_json(this_json, stream_name, data_key):
    new_json = this_json

    # ADD TRANSFORMATIONS

    return new_json