{% if cookiecutter.use_boost == "y" %}
find_package( Boost 1.58 COMPONENTS program_options system log REQUIRED )
include_directories( ${Boost_INCLUDE_DIR} )
{% endif %}

set({{cookiecutter.exe_name|upper}}_SRCFILES
    "{{cookiecutter.exe_name}}.cpp"
)

SOURCE_GROUP("Source Files" FILES {{'${'}}{{cookiecutter.exe_name|upper}}_SRCFILES{{'}'}})

add_executable({{cookiecutter.exe_name}}
    {{'${'}}{{cookiecutter.exe_name|upper}}_SRCFILES{{'}'}}
    ${GLOBAL_SRCFILES}
    ${GLOBAL_HDRFILES}
)

{% if cookiecutter.use_boost == "y" %}
target_link_libraries(uhd-sensor  ${Boost_LIBRARIES})
{% endif %}

install(TARGETS {{cookiecutter.exe_name}} DESTINATION bin)
