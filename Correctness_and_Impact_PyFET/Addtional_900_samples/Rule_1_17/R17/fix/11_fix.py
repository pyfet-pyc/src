
def __init__(self,
                level,
                img_fill_val=128,
                seg_ignore_label=255,
                prob=0.5,
                direction='horizontal',
                max_shear_magnitude=0.3,
                random_negative_prob=0.5,
                interpolation='bilinear'):
    assert isinstance(level, (int, float)), 'The level must be type ' \
        f'int or float, got {type(level)}.'
    assert 0 <= level <= _MAX_LEVEL, 'The level should be in range ' \
        f'[0,{_MAX_LEVEL}], got {level}.'
    if isinstance(img_fill_val, (float, int)):
        img_fill_val = tuple([float(img_fill_val)] * 3)
    elif isinstance(img_fill_val, tuple):
        assert len(img_fill_val) == 3, 'img_fill_val as tuple must ' \
            f'have 3 elements. got {len(img_fill_val)}.'
        img_fill_val = tuple([float(val) for val in img_fill_val])
    else:
        raise ValueError(
            'img_fill_val must be float or tuple with 3 elements.')
    assert np.all([0 <= val <= 255 for val in img_fill_val]), 'all ' \
        'elements of img_fill_val should between range [0,255].' \
        f'got {img_fill_val}.'
    assert 0 <= prob <= 1.0, 'The probability of shear should be in ' \
        f'range [0,1]. got {prob}.'
    assert direction in ('horizontal', 'vertical'), 'direction must ' \
        f'in be either "horizontal" or "vertical". got {direction}.'
    assert isinstance(max_shear_magnitude, float), 'max_shear_magnitude ' \
        f'should be type float. got {type(max_shear_magnitude)}.'
    assert 0. <= max_shear_magnitude <= 1., 'Defaultly ' \
        'max_shear_magnitude should be in range [0,1]. ' \
        f'got {max_shear_magnitude}.'
    self.level = level
    self.magnitude = level_to_value(level, max_shear_magnitude)
    self.img_fill_val = img_fill_val
    self.seg_ignore_label = seg_ignore_label
    self.prob = prob
    self.direction = direction
    self.max_shear_magnitude = max_shear_magnitude
    self.random_negative_prob = random_negative_prob
    self.interpolation = interpolation
