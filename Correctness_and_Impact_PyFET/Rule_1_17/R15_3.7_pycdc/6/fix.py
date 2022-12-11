def setUp(self):
    super(TestMetricsCorrectnessSingleIO, self).setUp()
    self.x = np.asarray([[1.0], [2.0], [3.0], [4.0]])
    self.y = np.asarray([[2.0], [4.0], [6.0], [8.0]])
    self.sample_weight = np.asarray([2.0, 3.0, 4.0, 5.0])
    self.class_weight = [(i, 1) for i in range(10)]
    self.class_weight = dict(self.class_weight)
    self.class_weight.update({2: 2, 4: 3, 6: 4, 8: 5})

    # y_true = [[2.], [4.], [6.], [8.]], y_pred = [[3.], [6.], [9.], [12.]]

    # Metric:
    #   Total = ((3 - 2)^2 + (6 - 4)^2) + ((9 - 6)^2 + (12 - 8)^2) = 30,
    #   Count = 2 + 2
    #   Result = 7.5

    # Weighted metric:
    #   Total = ((3 - 2)^2 * 2  + (6 - 4)^2 * 3) +
    #           ((9 - 6)^2 * 4 + (12 - 8)^2 * 5)
    #         = 130
    #   Count = (2 + 3) + (4 + 5)
    #   Result = 9.2857141

    # Total loss with weights:
    #   Total = ((3 - 2)^2 * 2  + (6 - 4)^2 * 3) +
    #           ((9 - 6)^2 * 4 + (12 - 8)^2 * 5)
    #         = 130,
    #   Count = 2 + 2
    #   Result = 32.5

    # Total loss without weights:
    #   Total = ((3 - 2)^2 + (6 - 4)^2) +
    #           ((9 - 6)^2 + (12 - 8)^2)
    #         = 30,
    #   Count = 2 + 2
    #   Result = 7.5

    wmse = "mean_squared_error_2"

    self.expected_fit_result_with_weights = {
        "mean_squared_error": [7.5, 7.5],
        wmse: [9.286, 9.286],
        "loss": [32.5, 32.5],
    }

    self.expected_fit_result = {
        "mean_squared_error": [7.5, 7.5],
        wmse: [7.5, 7.5],
        "loss": [7.5, 7.5],
    }

    # In the order: 'loss', 'mean_squared_error', 'mean_squared_error_2'
    self.expected_batch_result_with_weights = [32.5, 7.5, 9.286]
    self.expected_batch_result = [7.5, 7.5, 7.5]