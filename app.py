import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

name = str(input("Enter your name: "))
last_name = str(input("Enter your last name: "))
logger.info("User input received: %s %s", name, last_name)