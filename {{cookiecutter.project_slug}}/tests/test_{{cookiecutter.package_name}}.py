from {{ cookiecutter.package_name }}.cli import main


def test_main():
    main([])
