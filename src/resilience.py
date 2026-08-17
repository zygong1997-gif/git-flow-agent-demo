def calculate_resilience(network_size, failed_nodes):
    """
    Simple resilience metric example.
    Higher value means stronger resilience.
    """
    if network_size == 0:
        return 0

    resilience = 1 - failed_nodes / network_size

    return max(resilience, 0)