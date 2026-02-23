import logging
import sys


def setup_logging(default_level=logging.INFO):
    """Configure logging with better override protection"""

    # 1. Define the format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # 2. Use force=True to ensure our config sticks
    logging.basicConfig(
        level=default_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ],
        force=True
    )

    # 3. Use a dict-based config if things get complex,
    # but for simple scripts, this 'force' approach is the safest fix.
    logging.getLogger("uvicorn.access").propagate = True


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Logging is configured correctly!")