product package
===============

Subpackages
-----------

Submodules
-----------

product.admin module
--------------------

.. autoclass:: product.admin.ProductAdmin
   :members:


   :ivar list_display: A tuple specifying the fields to display in the admin list view. By default, it includes 'title', 'price', and 'quantity'.

product.apps module
--------------------

.. autoclass:: product.apps.ProductConfig
   :members:


   :ivar default_auto_field: The default database field for AutoField, set to 'django.db.models.BigAutoField'.
   :ivar name: The name of the app, which is 'product'.

product.models module
---------------------

.. autoclass:: product.models.Product
   :members:

   This class represents a product in the e-commerce application.

   :ivar title: The title or name of the product, limited to a maximum of 200 characters.
   :ivar description: A detailed description of the product.
   :ivar price: The price of the product, with a maximum of 10 digits and 2 decimal places.
   :ivar quantity: The quantity of the product in stock, represented as a positive integer.

product.tests module
---------------------

product.urls module
--------------------

.. data:: product.urls.app_name

   Important URLs listed to easily connect the Django project when navigating the webpage.

product.views module
---------------------

.. autoclass:: product.views.ProductDetailView
   :members:

   Displays a more detailed view of the product in a separate webpage.

   :ivar context_object_name: The name used to reference the product object in the template.
   :ivar model: An alias of Product.
   :ivar template_name: The name of the HTML template used for rendering the detailed view.

.. autofunction:: product.views.online_shop

   Fetches a list of products from a database and generates it on the online shop webpage.

.. autofunction:: product.views.your_signup_view

   Handles user registration
