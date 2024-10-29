def calculate_net_profit(revenue, costs):
    """Calculate net profit."""
    return revenue - costs

def calculate_roi(net_profit, costs):
    """Calculate ROI."""
    if costs == 0:
        return 0.0
    return (net_profit / costs) * 100