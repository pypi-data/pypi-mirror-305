from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from netbox_svm import views
from netbox_svm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense

urlpatterns = [
    # SoftwareProduct
    path("software-products/", views.SoftwareProductListView.as_view(), name="softwareproduct_list"),
    path("software-products/add/", views.SoftwareProductEditView.as_view(), name="softwareproduct_add"),
    path(
        "software-products/delete/", views.SoftwareProductBulkDeleteView.as_view(), name="softwareproduct_bulk_delete"
    ),
    path("software-products/<int:pk>/", views.SoftwareProductView.as_view(), name="softwareproduct"),
    path(
        "software-products/<int:pk>/delete/", views.SoftwareProductDeleteView.as_view(), name="softwareproduct_delete"
    ),
    path("software-products/<int:pk>/edit/", views.SoftwareProductEditView.as_view(), name="softwareproduct_edit"),
    path(
        "software-products/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwareproduct_changelog",
        kwargs={"model": SoftwareProduct},
    ),
    # SoftwareProductVersion
    path("versions/", views.SoftwareProductVersionListView.as_view(), name="softwareproductversion_list"),
    path("versions/add/", views.SoftwareProductVersionEditView.as_view(), name="softwareproductversion_add"),
    path(
        "versions/delete/",
        views.SoftwareProductVersionBulkDeleteView.as_view(),
        name="softwareproductversion_bulk_delete",
    ),
    path("versions/<int:pk>/", views.SoftwareProductVersionView.as_view(), name="softwareproductversion"),
    path(
        "versions/<int:pk>/delete/",
        views.SoftwareProductVersionDeleteView.as_view(),
        name="softwareproductversion_delete",
    ),
    path("versions/<int:pk>/edit/", views.SoftwareProductVersionEditView.as_view(), name="softwareproductversion_edit"),
    path(
        "versions/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwareproductversion_changelog",
        kwargs={"model": SoftwareProductVersion},
    ),

    ## SoftwareProductVersion -> Installation
    path('versions/<int:pk>/installations/', views.SwVersionInstallView.as_view(), name='softwareproductversion_softwareproductinstallation'),
    # path('versions/<int:pk>/installations/add/', views.ProjectAddIPAddressView.as_view(), name='project_add_ipaddress'),
    # path('versions/<int:pk>/installations/remove/', views.ProjectRemoveIPAddressView.as_view(), name='project_remove_ipaddress')


    # SoftwareProductInstallation
    path(
        "installations/",
        views.SoftwareProductInstallationListView.as_view(),
        name="softwareproductinstallation_list",
    ),
    path(
        "installations/add/",
        views.SoftwareProductInstallationEditView.as_view(),
        name="softwareproductinstallation_add",
    ),
    path(
        "installations/delete/",
        views.SoftwareProductInstallationBulkDeleteView.as_view(),
        name="softwareproductinstallation_bulk_delete",
    ),
    path(
        "installations/<int:pk>/",
        views.SoftwareProductInstallationView.as_view(),
        name="softwareproductinstallation",
    ),
    path(
        "installations/<int:pk>/delete/",
        views.SoftwareProductInstallationDeleteView.as_view(),
        name="softwareproductinstallation_delete",
    ),
    path(
        "installations/<int:pk>/edit/",
        views.SoftwareProductInstallationEditView.as_view(),
        name="softwareproductinstallation_edit",
    ),
    path(
        "installations/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwareproductinstallation_changelog",
        kwargs={"model": SoftwareProductInstallation},
    ),

    path(
        "installations/<int:pk>/contact/",
        views.SoftwareProductInstallationContactView.as_view(),
        name="softwareproductinstallation_contact"
    ),
    path(
        "installations/<int:pk>/contact/add/",
        views.SoftwareProductInstallationAddContactView.as_view(),
        name="softwareproductinstallation_add_contact"
    ),
    path(
        "installations/<int:pk>/contact/remove/",
        views.SoftwareProductInstallationRemoveContactView.as_view(),
        name="softwareproductinstallation_remove_contact"
    ),
    # SoftwareLicense
    path("licenses/", views.SoftwareLicenseListView.as_view(), name="softwarelicense_list"),
    path("licenses/add/", views.SoftwareLicenseEditView.as_view(), name="softwarelicense_add"),
    path("licenses/delete/", views.SoftwareLicenseBulkDeleteView.as_view(), name="softwarelicense_bulk_delete"),
    path("licenses/<int:pk>/", views.SoftwareLicenseView.as_view(), name="softwarelicense"),
    path("licenses/<int:pk>/delete/", views.SoftwareLicenseDeleteView.as_view(), name="softwarelicense_delete"),
    path("licenses/<int:pk>/edit/", views.SoftwareLicenseEditView.as_view(), name="softwarelicense_edit"),
    path(
        "licenses/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="softwarelicense_changelog",
        kwargs={"model": SoftwareLicense},
    ),
]
