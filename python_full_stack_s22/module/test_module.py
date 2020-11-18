# import glance.db.models
# glance.db.models.register_models('mysql1')

# from glance.db import models
# models.register_models('mysql2')

# from glance.db.models import register_models
# register_models('mysql3')

#glance/__init__.py
from . import cmd

#glance/cmd/__init__.py
from . import manage