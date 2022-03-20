"""
<?php
/**
 * Front to the WordPress application. This file doesn't do anything, but loads
 * wp-blog-header.php which does and tells WordPress to load the theme.
 *
 * @package WordPress
 */
"""
"""
/**
 * Tells WordPress to load the WordPress theme and output it.
 *
 * @var bool
 */
"""
define( "WP_USE_THEMES", true )
const WP_USE_THEMES = True

# /** Loads the WordPress Environment and Template */
from . import wp_blog_header
# require __DIR__ . '/wp-blog-header.php'
