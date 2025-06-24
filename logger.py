import logging
import os

def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(log_dir, "bot.log"),
        level=logging.INFO,  # ⬅ Only log INFO and above (ignores ERROR)
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # # Remove default stderr handler to suppress errors in terminal
    # root_logger = logging.getLogger()
    # for handler in root_logger.handlers:
    #     if isinstance(handler, logging.StreamHandler):
    #         root_logger.removeHandler(handler)
