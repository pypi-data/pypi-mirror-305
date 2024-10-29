cmake_minimum_required(VERSION 3.12)
project("bark_cpp")

function(bark_cpp_python_install target)
    install(
        TARGETS ${target}
        LIBRARY DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bark_cpp/lib
        RUNTIME DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bark_cpp/lib
        ARCHIVE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bark_cpp/lib
        FRAMEWORK DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bark_cpp/lib
        RESOURCE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/bark_cpp/lib
    )
    install(
        TARGETS ${target}
        LIBRARY DESTINATION ${SKBUILD_PLATLIB_DIR}/bark_cpp/lib
        RUNTIME DESTINATION ${SKBUILD_PLATLIB_DIR}/bark_cpp/lib
        ARCHIVE DESTINATION ${SKBUILD_PLATLIB_DIR}/bark_cpp/lib
        FRAMEWORK DESTINATION ${SKBUILD_PLATLIB_DIR}/bark_cpp/lib
        RESOURCE DESTINATION ${SKBUILD_PLATLIB_DIR}/bark_cpp/lib
    )
    set_target_properties(${target} PROPERTIES
        INSTALL_RPATH "$ORIGIN"
        BUILD_WITH_INSTALL_RPATH TRUE
    )
    if(UNIX)
        if(APPLE)
            set_target_properties(${target} PROPERTIES
                INSTALL_RPATH "@loader_path"
                BUILD_WITH_INSTALL_RPATH TRUE
            )
        else()
            set_target_properties(${target} PROPERTIES
                INSTALL_RPATH "$ORIGIN"
                BUILD_WITH_INSTALL_RPATH TRUE
            )
        endif()
    endif()
endfunction()

# DEPRECATED SOON
# Work-around solution to bypass the only-build type STATIC in bark.cpp and encodec.cpp.
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/vendor_cmakes/bark.cpp/CMakeLists.txt"
    "${CMAKE_CURRENT_SOURCE_DIR}/vendor/bark.cpp/CMakeLists.txt"
    COPYONLY
)
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/vendor_cmakes/encodec.cpp/CMakeLists.txt"
    "${CMAKE_CURRENT_SOURCE_DIR}/vendor/bark.cpp/encodec.cpp/CMakeLists.txt"
    COPYONLY
)

set(BUILD_SHARED_LIBS ON)
set(BARK_BUILD_EXAMPLES OFF)
set(CMAKE_SKIP_BUILD_RPATH FALSE)

# When building, don't use the install RPATH already
# (but later on when installing)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)

# Add the automatically determined parts of the RPATH
# which point to directories outside the build tree to the install RPATH
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_SKIP_RPATH FALSE)

if (APPLE AND NOT CMAKE_SYSTEM_PROCESSOR MATCHES "arm64")
    # Need to disable these bark.cpp flags on Apple x86_64,
    # otherwise users may encounter invalid instruction errors
    set(GGML_AVX "Off" CACHE BOOL "ggml: enable AVX" FORCE)
    set(GGML_AVX2 "Off" CACHE BOOL "ggml: enable AVX2" FORCE)
    set(GGML_FMA "Off" CACHE BOOL "gml: enable FMA" FORCE)
    set(GGML_F16C "Off" CACHE BOOL "gml: enable F16C" FORCE)
endif()

if (APPLE)
    set(GGML_METAL_EMBED_LIBRARY "On" CACHE BOOL "bark: embed metal library" FORCE)
endif()

add_subdirectory(vendor/bark.cpp)
bark_cpp_python_install(bark)
bark_cpp_python_install(encodec)
bark_cpp_python_install(ggml)