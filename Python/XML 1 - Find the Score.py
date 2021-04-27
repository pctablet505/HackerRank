def get_attr_number(node):
    out = len(node.attrib)
    return out + sum((get_attr_number(child) for child in node))
