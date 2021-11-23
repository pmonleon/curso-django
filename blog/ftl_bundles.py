from django_ftl.bundles import Bundle
from django_ftl import activate



main = Bundle(['blog/main.ftl'])

activate("es")