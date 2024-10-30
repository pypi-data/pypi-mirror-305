import pytest
import typer

from usethis._interface.browse import pypi


class TestPyPI:
    def test_message(self, capfd: pytest.CaptureFixture[str]):
        # Act
        pypi(package="numpy", browser=False)

        # Assert
        output = capfd.readouterr().out

        assert "☐ Open URL <https://pypi.org/project/numpy/>." in output

    def test_open_in_browser(self, monkeypatch):
        # Arrange
        class MockLaunch:
            def __init__(self):
                self.url = None

            def __call__(self, url):
                self.url = url

        mock_launch = MockLaunch()
        monkeypatch.setattr(typer, "launch", mock_launch)

        # Act
        pypi(package="numpy", browser=True)

        # Assert
        assert mock_launch.url == "https://pypi.org/project/numpy/"
