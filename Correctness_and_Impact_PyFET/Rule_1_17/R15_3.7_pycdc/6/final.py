# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)


def setUp(self):
    super(TestMetricsCorrectnessSingleIO, self).setUp()
    self.x = np.asarray([
        [
            1],
        [
            2],
        [
            3],
        [
            4]])
    self.y = np.asarray([
        [
            2],
        [
            4],
        [
            6],
        [
            8]])
    self.sample_weight = np.asarray([
        2,
        3,
        4,
        5])
    self.class_weight = (lambda .0: [ (i, 1) for i in .0 ])(range(10))
    self.class_weight = dict(self.class_weight)
    self.class_weight.update({
        2: 2,
        4: 3,
        6: 4,
        8: 5 })
    wmse = 'mean_squared_error_2'
    self.expected_fit_result_with_weights = {
        'loss': [
            32.5,
            32.5],
        wmse: [
            9.286,
            9.286],
        'mean_squared_error': [
            7.5,
            7.5] }
    self.expected_fit_result = {
        'loss': [
            7.5,
            7.5],
        wmse: [
            7.5,
            7.5],
        'mean_squared_error': [
            7.5,
            7.5] }
    self.expected_batch_result_with_weights = [
        32.5,
        7.5,
        9.286]
    self.expected_batch_result = [
        7.5,
        7.5,
        7.5]

