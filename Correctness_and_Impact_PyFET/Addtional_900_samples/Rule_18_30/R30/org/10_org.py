class SubredditJsonTemplate(ThingJsonTemplate):
    _data_attrs_ = ThingJsonTemplate.data_attrs(
        accounts_active="accounts_active_count",
        banner_img="banner_img",
        banner_size="banner_size",
        collapse_deleted_comments="collapse_deleted_comments",
        comment_score_hide_mins="comment_score_hide_mins",
        community_rules="community_rules",
        description="description",
        description_html="description_html",
        display_name="name",
        header_img="header",
        header_size="header_size",
        header_title="header_title",
        icon_img="icon_img",
        icon_size="icon_size",
        # key_color="key_color",
        lang="lang",
        over18="over_18",
        public_description="public_description",
        public_description_html="public_description_html",
        public_traffic="public_traffic",
        # related_subreddits="related_subreddits",
        hide_ads="hide_ads",
        quarantine="quarantine",
        show_media="show_media",
        show_media_preview="show_media_preview",
        submission_type="link_type",
        submit_link_label="submit_link_label",
        submit_text_label="submit_text_label",
        submit_text="submit_text",
        submit_text_html="submit_text_html",
        subreddit_type="type",
        subscribers="_ups",
        suggested_comment_sort="suggested_comment_sort",
        title="title",
        url="path",
        user_is_banned="is_banned",
        user_is_muted="is_muted",
        user_is_contributor="is_contributor",
        user_is_moderator="is_moderator",
        user_is_subscriber="is_subscriber",
        user_sr_theme_enabled="user_sr_style_enabled",
        wiki_enabled="wiki_enabled",
    )

    # subreddit *attributes* (right side of the equals)
    # that are accessible even if the user can't view the subreddit
    _public_attrs = {
        "_id36",
        # subreddit ID with prefix
        "_fullname",
        # Creation date
        "created",
        "created_utc",
        # Canonically-cased subreddit name
        "name",
        # Canonical subreddit URL, relative to reddit.com
        "path",
        # Text shown on the access denied page
        "public_description",
        "public_description_html",
        # Title shown in search
        "title",
        # Type of subreddit, so people know that it's private
        "type",
    }