=====
Django Recyclebin
=====

Django Recyclebin is a Django app to create recyclebin functionality in your project. you will be able to temporarily delete, restore and permanently delete data.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "recyclebin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'recyclebin',
    ]

2. import SoftDeleteMixin ''from recyclebin.models import SoftDeleteMixin''

3. Inherit your model with SoftDeleteMixin

        ``class Mymodel(SoftDeleteMixin)``

4. Run ``python manage.py makemigrations``  and ``python manage.py migrate``.

5. import recyclebin functions ``from recyclebin.functions import get_deleted_items, restore, permanent_delete``

6. How to temporarily delete.
    you don't need to do anything. after inheriting your model with SoftDeleteMixin. your regular .delete() method will temporarily delete objects

7. How to view deleted items 
    create a list of models
    from myapp.models import Model1, Model2, Model3...
    li = [Model1, Model2, Model3...]
     ``get_deleted_items(li)``

    ''This function will return serialized response that will contain model_name, name, pk, deleted_by, deleted_at''
    
    YOUR MODEL MUST HAVE NAME FIELD OTHERWISE NONE WILL BE RETURNED INSTEAD OF NAME

8. How to restore
    pass restore function model name and id. model name must be string and id an integer
    ``restore(model1, 1)``

9. How to permanently delete
    pass permanent_delete function model name and id. model name must be string and id an integer
    ``permanent_delete(model1, 1)``