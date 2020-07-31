# [START data_model]
def create_data_model(dist_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = dist_matrix
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data
    # [END data_model]
