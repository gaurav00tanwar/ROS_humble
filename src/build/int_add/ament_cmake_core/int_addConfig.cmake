# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_int_add_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED int_add_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(int_add_FOUND FALSE)
  elseif(NOT int_add_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(int_add_FOUND FALSE)
  endif()
  return()
endif()
set(_int_add_CONFIG_INCLUDED TRUE)

# output package information
if(NOT int_add_FIND_QUIETLY)
  message(STATUS "Found int_add: 0.0.0 (${int_add_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'int_add' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${int_add_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(int_add_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${int_add_DIR}/${_extra}")
endforeach()
