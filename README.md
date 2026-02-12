# ClusteringRealities - Candidate Selector 👑

## About the Project
**ClusteringRealities** is a Python application developed to optimize the casting process for a fictional reality show produced by the "RealidadeInfeliz" company.

Developed as the second project for the **Programming 2** course at the Faculty of Sciences of the University of Lisbon (2022/2023), the goal was to implement a **clustering algorithm** from scratch (without external libraries like `scikit-learn`) to group candidates based on similar characteristics.

## The Challenge
The production team has thousands of applicants with various nobility titles or celebrity statuses (e.g., Duke, TikTok Star, Plebeian). The software groups these candidates to find the most representative "exemplar" for each category, ensuring a diverse cast for the show.

## Features
* **Custom Clustering:** Implementation of a clustering algorithm (k-cluster style) adapted from the course manual.
* **Euclidean Distance:** Calculates similarity between candidates based on a numerical hierarchy of titles.
* **Exemplar Identification:** Identifies the "centroid" or most typical candidate within each formed group.
* **Data Parsing:** Processes input files containing candidate lineage and title hierarchy values.

## Technologies & Constraints
* **Language:** Python 3
* **Constraints:** STRICTLY FORBIDDEN to use external data science libraries (scikit-learn, SciPy, Pyclustering). The logic was implemented using standard libraries and manual algorithm construction.

## Usage
The program is executed via the command line.

### Command Syntax
```bash
python3 clusteringRealities.py <k> <titles_file> <input_file>
