import os
import pathlib
from log_writer.logger import WriteLogger


def test_write_logger():
    base_dir = pathlib.Path(__file__).parent.parent
    logger = WriteLogger(base_dir)

    # Test info method
    info_message = "This is an info message."
    logger.info(info_message)
    info_file_path = os.path.join(base_dir, "logs/info.log")
    with open(info_file_path) as f:
        content = f.read()
        assert info_message in content
        os.remove(info_file_path)

    # Test error method
    error_message = "This is an error message."
    logger.error(error_message)
    error_file_path = os.path.join(base_dir, "logs/error.log")
    with open(error_file_path) as f:
        content = f.read()
        assert error_message in content
        os.remove(error_file_path)
    os.rmdir(os.path.join(base_dir, "logs"))


