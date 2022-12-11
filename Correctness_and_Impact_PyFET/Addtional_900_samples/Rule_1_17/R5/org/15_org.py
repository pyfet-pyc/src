def test_fetch_dont_override_existing_layout(
    static_fetch_data, without_warnings
):
    with open(without_warnings.config.version_info_file, 'w') as stream:
        existing_layout = {
            'last_warned_date': FIXED_DATE,
            'last_fetched_date': FIXED_DATE,
            'last_released_versions': {BUILD_CHANNEL: LOWEST_VERSION},
        }
        json.dump(existing_layout, stream)

    http('fetch_updates', '--daemon', env=without_warnings)

    # The "last updated at" field should not be modified, but the
    # rest need to be updated.
    assert version_data['last_warned_date'] == FIXED_DATE
    assert version_data['last_fetched_date'] != FIXED_DATE
    assert (
        version_data['last_released_versions'][BUILD_CHANNEL]
        == HIGHEST_VERSION
    )