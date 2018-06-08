from ..online_reservoir_sampling import online_reservoir_sampling


def test_online_reservoir_sampling():
    sample_size = 10
    num_data_points = 100
    reservoir = online_reservoir_sampling(sample_size)
    next(reservoir)

    for i in range(num_data_points):
        data_count, samples = reservoir.send(i)

    assert data_count == num_data_points
    assert len(samples) == sample_size