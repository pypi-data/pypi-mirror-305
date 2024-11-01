from .software_license import (
    SoftwareLicenseListView,
    SoftwareLicenseView,
    SoftwareLicenseEditView,
    SoftwareLicenseDeleteView,
    SoftwareLicenseBulkDeleteView,
)
from .software_product import (
    SoftwareProductListView,
    SoftwareProductView,
    SoftwareProductEditView,
    SoftwareProductDeleteView,
    SoftwareProductBulkDeleteView,
)
from .software_product_installation import (
    SoftwareProductInstallationListView,
    SoftwareProductInstallationView,
    SoftwareProductInstallationEditView,
    SoftwareProductInstallationDeleteView,
    SoftwareProductInstallationBulkDeleteView,
    SoftwareProductInstallationContactView,
    SoftwareProductInstallationAddContactView,
    SoftwareProductInstallationRemoveContactView
)
from .software_product_version import (
    SoftwareProductVersionListView,
    SoftwareProductVersionView,
    SoftwareProductVersionEditView,
    SoftwareProductVersionDeleteView,
    SoftwareProductVersionBulkDeleteView,
)

from .version_viewtab_software_installation import (
    SwVersionInstallView,
)