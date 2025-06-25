import logging


logging.basicConfig(filename="file_1.log",
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s'
                    )


def parse_file(file_path):
    logging.info(f"Starting to parse file: {file_path}")

    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                logging.debug(f"Line {i}: {line.strip()}")
            logging.info("File read and parsed successfully.")

    except FileNotFoundError:
        logging.error("File not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.debug("Finished file parsing.")


parse_file(r"I:\Valere Internship\Week 1\Day 5\sample.txt")
