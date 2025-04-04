from django.contrib import admin
from .models import Patient  # Ensure only the right models are imported

# Import other models safely
# try:
#     from doctors.models import Doctor
#     from mappings.models import Mapping
#     admin.site.register(Doctor)
#     admin.site.register(Mapping)
# except ImportError:
#     print("WARNING: Doctor or Mapping model could not be imported. Check for circular imports!")

admin.site.register(Patient)
