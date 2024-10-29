from setuptools import find_namespace_packages, setup

setup(
    name='sam-djtools',
    long_description_content_type="text/markdown",
    python_requires=">=3",
    setup_requires=['setuptools_scm'],
    description='1. sam_tools.utils, 2. Primary key based form navigation to explore next/prev records.',
    url="https://github.com/humblesami/sam-djtools.git",
    include_package_data=True,
    packages=find_namespace_packages(include=["sam_tools.*"]),
    package_data={
        "sam_tools": [
            "templates/admin/change_form.html",
            "static/sam_tools/change_form_prev_next.js"
        ]
    }
)
