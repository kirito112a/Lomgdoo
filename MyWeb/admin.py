from django.contrib import admin
from. models import category, consumer , enturpreneur,product_and_service,question,answer, sentiment,survey, trial ,type,language
from django.db import connection
print(connection.queries)

admin.site.register(category)
admin.site.register(type)
admin.site.register(trial)
admin.site.register(consumer)
admin.site.register(enturpreneur)
admin.site.register(product_and_service)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(survey)
admin.site.register(sentiment)
admin.site.register(language)


# โชว์ใน admin
