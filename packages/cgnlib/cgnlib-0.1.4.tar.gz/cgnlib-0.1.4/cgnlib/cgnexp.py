import csv
from cgnlib import cgnlib

class cgnexp:
    """
    A class to conduct experiments on community detection using different centrality measures.
    
    This class acts as a wrapper for the `cgnlib` class, providing functionality to load 
    a graph dataset, run community detection experiments using various centrality metrics, 
    and report the results.

    Attributes:
        file (str): The path to the graph file.
        graph_data (cgnlib): An instance of the `cgnlib` class to handle graph operations.
        results (list of dict): A list of dictionaries storing the results of the experiments.
    """
    
    def __init__(self, file):
        """
        Initializes the cgnexp class with the graph dataset.

        Args:
            file (str): The path to the graph file.
        """
        self.file = file
        self.graph_data = cgnlib(file)
        self.results = []
    
    def run_experiments(self, metrics=None, save_images=False):
        """
        Runs community detection experiments for the specified centrality metrics.

        This method executes the `detect_gn` method from the `cgnlib` class for each centrality 
        measure and collects modularity, average conductance, minimum conductance, 
        maximum conductance, coverage, and the number of communities detected.
        Optionally saves visualizations of the best communities.

        Args:
            metrics (list of str): A list of centrality metrics to be tested. If None, a default list is used.
            save_images (bool): If True, saves visualizations of the best communities 
                                for each centrality metric. Default is False.
        
        If a metric is unsupported, it is skipped with an error message.
        """
        if metrics is None:
            metrics = ['closeness', 'betweenness', 'pagerank', 'degree', 'bary']
        
        for metric in metrics:
            try:
                print(f"Running experiment with {metric} centrality...")
                communities = self.graph_data.detect_gn(method=metric)
                quality_metrics = self.graph_data.evaluate_community_quality()
                modularity = quality_metrics.get("Modularity")
                average_conductance = quality_metrics.get("Average Conductance")
                min_conductance = quality_metrics.get("Min Conductance")
                max_conductance = quality_metrics.get("Max Conductance")
                coverage = quality_metrics.get("Coverage")
                num_communities = len(communities)
                
                self.results.append({
                    'Centrality Metric': metric,
                    'Modularity': modularity,
                    'Average Conductance': average_conductance,
                    'Min Conductance': min_conductance,
                    'Max Conductance': max_conductance,
                    'Coverage': coverage,
                    'Number of Communities': num_communities
                })
                
                if save_images:
                    image_filename = f"{self.file.split('.')[0]}_{metric}.png"
                    self.graph_data.visualize_best_communities(image_filename)
                    print(f"Image saved as {image_filename}")
            except ValueError as e:
                print(f"Error: {e}. Skipping {metric} centrality.")

    def print_results(self):
        """
        Prints the results of the experiments to the console.

        The results include centrality metrics, modularity, average conductance, minimum conductance,
        maximum conductance, coverage, and the number of communities detected for each centrality measure tested.
        """
        for result in self.results:
            print(f"Centrality Metric: {result['Centrality Metric']}")
            print(f"Modularity: {result['Modularity']}")
            print(f"Average Conductance: {result['Average Conductance']}")
            print(f"Min Conductance: {result['Min Conductance']}")
            print(f"Max Conductance: {result['Max Conductance']}")
            print(f"Coverage: {result['Coverage']}")
            print(f"Number of Communities: {result['Number of Communities']}")
            print()
    
    def export_results_to_csv(self, filename='experiment_results.csv'):
        """
        Exports the results of the experiments to a CSV file.

        Args:
            filename (str): The name of the file to save the results to. Defaults to 'experiment_results.csv'.
        
        The CSV file will contain columns for 'Centrality Metric', 'Modularity', 'Average Conductance',
        'Min Conductance', 'Max Conductance', 'Coverage', and 'Number of Communities'.
        """
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Centrality Metric', 'Modularity', 'Average Conductance', 'Min Conductance',
                          'Max Conductance', 'Coverage', 'Number of Communities']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for result in self.results:
                writer.writerow(result)
        print(f"Results exported to {filename}")

if __name__ == '__main__':
    # User can specify a list of centrality metrics to test, or leave as None to use the default list
    exp = cgnexp('hdy.graph')
    exp.run_experiments(metrics=['closeness', 'load', 'betweenness', 'degree', 'subgraph', 'algebraic'], save_images=True)
    exp.print_results()
    exp.export_results_to_csv('experiment_results.csv')
