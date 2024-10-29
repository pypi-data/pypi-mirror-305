try:
    from .torch import jrmpc, initialize_cluster_centers, jrmpc_single_view_fixed_model, parallel_jrmpc_single_view_fixed_model
except (ModuleNotFoundError, ImportError):
    from .numpy import jrmpc, initialize_cluster_centers
