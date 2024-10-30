import optuna


class GlobalHyperparameterInitializer:
    def __init__(self, config):
        optimizer_config = config['hyperparameter_optimizer']
        self.storage_url = optimizer_config['storage_url']
        self.study_name = optimizer_config['study_name']
        self.direction = optimizer_config['direction']

    def initialize_study(self):
        try:
            optuna.delete_study(study_name=self.study_name, storage=self.storage_url)
            print(f"Study '{self.study_name}' deleted successfully.")
        except KeyError:
            print(f"Study '{self.study_name}' creating a new one.")

        study = optuna.create_study(
            study_name=self.study_name,
            direction=self.direction,
            storage=self.storage_url,
            load_if_exists=True
        )
        print(f"Study '{self.study_name}' has been successfully created.")
        return study
