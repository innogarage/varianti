
DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = "$g962jf5ih49wt03*#opp(k)c2gn0*lqy$ri_c(wkf83)qa#m!"
NEVERCACHE_KEY = "$$w0u2@z64=1n94q4$#14w*7wf1bzhgg!#d816aux0vu(fonmz"


DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}