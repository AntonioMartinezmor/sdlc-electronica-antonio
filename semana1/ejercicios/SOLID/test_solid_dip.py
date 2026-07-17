import pytest 
import os 
from solid_dip import GoodDataProcessor, GoodTxtLogger, GoodConsoleLogger

def test_processor_with_logger() -> None: 
    log_file = "log_bueno.txt"
    if os.path.exists(log_file):
        os.remove(log_file)
    
    txt_logger = GoodTxtLogger()
    processor = GoodDataProcessor(logger= txt_logger)
    processor.process(45.2)
    assert os.path.exists(log_file) is True
    os.remove(log_file)

def test_processor_with_console_logger(capsys: pytest.CaptureFixture) -> None:
    console_logger= GoodConsoleLogger()
    processor = GoodDataProcessor(logger=console_logger)
    processor.process(10.0)
    captured = capsys.readouterr()
    assert "acceso a la consola: 10.0 procesado" in captured.out