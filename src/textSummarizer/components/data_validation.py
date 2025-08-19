import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True  # assume all good unless we find missing files

            # Path to check
            data_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            all_files = os.listdir(data_path)

            # check if all required files are present
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    logger.error(f"Missing required file: {required_file}")
                    break  # no need to continue checking

            # save status once
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation completed. Status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.exception("Error occurred during validation.")
            raise e
