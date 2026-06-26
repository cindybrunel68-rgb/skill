from pathlib import Path
import importlib.util
import tempfile


def load_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "run_analysis.py"
    spec = importlib.util.spec_from_file_location("run_analysis", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_generate_report_creates_file():
    module = load_module()
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "report.md"
        report = module.generate_analysis_report(Path(__file__).resolve().parents[4], output_path)

        assert output_path.exists()
        assert "GENERAL STATE" in report
        assert "BUGS AND ERRORS" in report
