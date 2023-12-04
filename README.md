# FormCheck: Weightlifting Form Assessment Project

**VERY MUCH UNDER CONSTRUCTION :)**

## Overview

FormCheck is an open-source machine learning and computer vision project designed for assessing people's form during weightlifting exercises. The project comprises two main components: lift classification and form issue identification.

### Key Features

- **Lift Classification:** Classify different types of weightlifting exercises (e.g., squat, press) using machine learning models.
- **Form Issue Identification:** Identify potential issues with lifting form, such as back rounding or knees collapsing.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies (listed in requirements.txt)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samson-bakos/FormCheck.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the main application:

   ```bash
   python main.py
   ```

2. Follow on-screen instructions to input video files or use the webcam for real-time assessment.

## Data Collection

### Collecting Data

- To build or extend the dataset, follow the guidelines in the [Data Collection](./docs/data-collection.md) documentation.

### Annotation

- Manually annotate the dataset with labels for both lift classification and form issues.

## Model Training

- Refer to [Model Training](./docs/model-training.md) documentation for details on training the machine learning models.

## Contributing

Contributions are welcome! Follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

