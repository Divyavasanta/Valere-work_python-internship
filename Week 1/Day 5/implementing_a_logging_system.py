import logging

logging.basicConfig(filename="file_1.log", level=logging.DEBUG,
                    format='%(asctime)s %(message)s')


def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            logging.info("File read successfully")

    except FileNotFoundError:
        logging.error("File not found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


parse_file(r"I:\Valere Internship\Week 1\Day 5\sample.txt")
