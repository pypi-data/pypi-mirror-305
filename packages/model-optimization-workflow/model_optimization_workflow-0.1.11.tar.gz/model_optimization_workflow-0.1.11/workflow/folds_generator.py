import json
import os
from datetime import datetime

from common.common import prepare_directory


class FoldsGenerator:
    def __init__(self, config, n_folds, run_directory):
        self.n_folds = n_folds
        self.run_directory = run_directory
        self.folds_directory = os.path.join(self.run_directory, 'folds')
        prepare_directory(self.folds_directory)
        self.config = config
        self.day_from = int(self.config['provider']['day_from'].timestamp() * 1000)
        self.day_to = int(self.config['provider']['day_to'].timestamp() * 1000)

    def generate(self, datasets):
        total_time = self.day_to - self.day_from
        fold_size = total_time // self.n_folds

        dataset_size = len(datasets)
        fold_sizes = []

        for i in range(self.n_folds):
            fold_start = self.day_from + fold_size * i
            fold_end = fold_start + fold_size
            fold_path = os.path.join(self.folds_directory, f'{i}')
            os.makedirs(fold_path, exist_ok=True)
            fold_data = [data for data in datasets if fold_start <= data['t_from'] < fold_end]
            fold_data = sorted(fold_data, key=lambda x: x['t_from'])

            fold_sizes.append(len(fold_data))

            for idx, data in enumerate(fold_data):
                filename = f'data_{idx + 1}.json'
                file_path = os.path.join(fold_path, filename)
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=1)

        print(
            f"process-{os.getpid()}, time: {datetime.now()}, total dataset size: {dataset_size}, Number of folds: {self.n_folds}, Fold sizes: {fold_sizes}")
