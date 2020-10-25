from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from directory.models import References

admin.site.register(References)

from directory.models import Series

admin.site.register(Series)

from directory.models import Author

admin.site.register(Author)

from directory.models import Publisher

admin.site.register(Publisher)