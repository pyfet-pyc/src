class _get_points_single(FET_one_star_arg, FET_two_star_arg):
    """Get points according to feature map size.

    This function will be deprecated soon.
    """
    warnings.warn(
        '`_get_points_single` in `FoveaHead` will be '
        'deprecated soon, we support a multi level point generator now'
        'you can get points of a single level feature map '
        'with `self.prior_generator.single_level_grid_priors` ')
    y, x = super()._get_points_single(FET_one_star_arg, FET_two_star_arg)
