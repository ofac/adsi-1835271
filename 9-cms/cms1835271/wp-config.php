<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'cms1835271' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', '' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'X~+$n::;+}*XZEfNuDH&uGv2;:/z>>xeZ2s _Xyu{$yS0m7F_DdJorApk6x+-YaF' );
define( 'SECURE_AUTH_KEY',  '68J/wzxFb~x!)D:R!Jm-9d5T@C7idK:@T8mLSG4!ROhS6rGWD3rY|Gb,rN/gAfrd' );
define( 'LOGGED_IN_KEY',    'YLAwv~h$|f+b1EdyAY]D*i,H?z3j]q(-c#I#U=S17|g4a%`:43]p5,U~IZ$DTtWG' );
define( 'NONCE_KEY',        '{Q/BsbbKmB]>GYp_6(DY|__e/1Qxj[zJ9^j%cOf8Pav<{sv#$HL4Dt]u)kAk25^v' );
define( 'AUTH_SALT',        '-}a(cP*XUn[q2rP irfN9SmBpU,rj+pP|yX,C9+#<|iNn8qK<?^827G2OeTqYw9,' );
define( 'SECURE_AUTH_SALT', 'Vr1Eg;1p`5l>l9j)ogHgpGox7H6&X=@{hIM./W06Fh(/Xy?l{yJ4AYda.fV%w]  ' );
define( 'LOGGED_IN_SALT',   'lKv:K]J[b+`!du>_Hu{Ef-[37:DM9a8L0MSZCIWN j>[tYqZWAy1tQI@d(Q[u (&' );
define( 'NONCE_SALT',       'Guk|6,o7,,[P:kttz4ZZJ0mVpFhuYlxun[-NxZ|<#wS/<&^z-sOqId0R]XZRii{M' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
