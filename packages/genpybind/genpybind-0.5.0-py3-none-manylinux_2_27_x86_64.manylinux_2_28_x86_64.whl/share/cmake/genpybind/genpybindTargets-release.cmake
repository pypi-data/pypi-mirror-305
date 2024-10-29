#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "genpybind::genpybind-tool" for configuration "Release"
set_property(TARGET genpybind::genpybind-tool APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(genpybind::genpybind-tool PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/genpybind-tool"
  )

list(APPEND _cmake_import_check_targets genpybind::genpybind-tool )
list(APPEND _cmake_import_check_files_for_genpybind::genpybind-tool "${_IMPORT_PREFIX}/bin/genpybind-tool" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
