"""Version information for this package."""

### IMPORTS
### ============================================================================
## Standard Library

## Installed

## Application

### CONSTANTS
### ============================================================================
## Version Information - DO NOT EDIT
## -----------------------------------------------------------------------------
# These variables will be set during the build process. Do not attempt to edit.
PACKAGE_VERSION = "1.0.2"
BUILD_VERSION = "1.0.2.dev1730195420"
BUILD_GIT_HASH = "4a0c23c952b9c479aa3c3ef9215ac195d2fd3e77"
BUILD_GIT_HASH_SHORT = "4a0c23c"
BUILD_GIT_BRANCH = "nhairs-issue-6"
BUILD_TIMESTAMP = 1730195420
BUILD_DATETIME = datetime.datetime.utcfromtimestamp(1730195420)

## Version Information Strings
## -----------------------------------------------------------------------------
VERSION_INFO_SHORT = f"{BUILD_VERSION}"
VERSION_INFO = f"{PACKAGE_VERSION} ({BUILD_VERSION})"
VERSION_INFO_LONG = (
    f"{PACKAGE_VERSION} ({BUILD_VERSION}) ({BUILD_GIT_BRANCH}@{BUILD_GIT_HASH_SHORT})"
)
VERSION_INFO_FULL = (
    f"{PACKAGE_VERSION} ({BUILD_VERSION})\n"
    f"{BUILD_GIT_BRANCH}@{BUILD_GIT_HASH}\n"
    f"Built: {BUILD_DATETIME}"
)
