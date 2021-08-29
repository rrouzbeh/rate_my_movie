
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MOVIE",
    settings_files=['settings.yaml', '.secrets.yaml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
