import pytest
from config import UartConfing
from parsers import ModbusParser, NMEAParser
from device import UartDevice
from recorder import Recorder


#test de configuracion uart
def test_valid_baudrate():
    cfg = UartConfing(9600)
    assert cfg.baudrate == 9600

def test_invalid_baudrate():
    with pytest.raises(ValueError):
        UartConfing(12345)

#test de traductor 
def test_modbus_parser():
    parser = ModbusParser()
    result = parser.encode("HOLA")
    assert result == b"HOLA"

def test_nmea_parser():
    parser= NMEAParser()
    result = parser.encode("DATA")
    assert result.endswith(b"\r\n")

#test device
def test_device_send_and_recive():
    cfg = UartConfing(9600)
    parser =ModbusParser()
    device = UartDevice(cfg, parser)
    sent = device.send("PING")
    received = device.receive(sent)
    assert received == "PING"


#test de escritura 
def test_recorder_saves(tmp_path):
    file = tmp_path / "log.jsonl"
    recorder = Recorder(str(file))
    recorder.save({"msg": "test"})
    content = file.read_text().strip()
    assert content == '{"msg": "test"}'

