import os

from common.common import prepare_directory, random_string

from configs.config_loader import ConfigLoader
from provider.datasets_provider import DatasetsProvider
from report.report import RunReport
from workflow.folds_generator import FoldsGenerator
from workflow.folds_window import FoldsWindow


class RunProcessor:
    def __init__(self, params):
        self.config = ConfigLoader().get_config()
        self.params = params
        self.root = self.config['workflow']['root_path']
        self.run_id = f'run_{random_string()}'
        self.run_directory = f'{self.root}/runs/{self.run_id}'
        prepare_directory(self.run_directory)
        print(f"process-{os.getpid()}, init run id: {self.run_id}")

    def _generate_folds(self, params, all_datasets):
        FoldsGenerator(
            n_folds=params['total_folds'],
            run_directory=self.run_directory
        ).generate(all_datasets)

    def _generate_dataset(self):
        return DatasetsProvider(self.params).generate_dataset()

    def _get_window_size(self):
        model_containers = self.config['workflow']['model_containers']
        fold_to_values = [
            container['parameters']['fold_to']
            for container in model_containers
            if 'fold_to' in container['parameters']
        ]
        return max(fold_to_values) + 1

    def _generate_folds_windows(self):
        windows = []
        window_size = self._get_window_size()
        folds = list(range(self.params['total_folds']))
        for i in range(len(folds) - window_size + 1):
            windows.append(
                FoldsWindow(config=self.config, params=self.params, window_folds_schema=folds[i:i + window_size],
                            root_directory=self.run_directory))
        return windows

    def run_process(self):
        datasets = self._generate_dataset()
        self._generate_folds(self.params, datasets)
        fold_windows = self._generate_folds_windows()

        windows_reports = []
        for window in fold_windows:
            windows_reports.append(window.execute())

        return RunReport(run_id=self.run_id, params=self.params, windows_reports=windows_reports)
