# (c) https://github.com/dev-cafe/autocmake/blob/master/AUTHORS.md
# licensed under BSD-3: https://github.com/dev-cafe/autocmake/blob/master/LICENSE

#.rst:
#
# Adds sccache support.
# The user should export the appropriate environment variables to
# tweak the program's behaviour, as described in its manpage.
# Notice that some additional compiler flags might be needed in order
# to avoid unnecessary warnings.
#
# Variables defined::
#
#   SCCACHE_FOUND
#
# autocmake.yml configuration::
#
#   docopt: "--sccache=<USE_SCCACHE> Toggle use of sccache <ON/OFF> [default: ON]."
#   define: "'-DUSE_SCCACHE={0}'.format(arguments['--sccache'])"

if(USE_SCCACHE)
    find_program(SCCACHE_FOUND sccache)
    if(SCCACHE_FOUND)
        set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE sccache)
        set_property(GLOBAL PROPERTY RULE_LAUNCH_LINK sccache)
        message(STATUS "Compiling with sccache")
    else()
        message(STATUS "sccache not available")
    endif()
endif()
