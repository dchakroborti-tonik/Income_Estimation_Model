
def plot_residuals(y_true, y_pred, title='Residual Plot'):
    """
    Create a residual plot to visualize model errors with type conversion
    
    Parameters:
    - y_true: True target values
    - y_pred: Predicted target values
    - title: Plot title
    """
    # Convert to numpy float arrays to ensure type compatibility
    y_true_float = np.array(y_true, dtype=float)
    y_pred_float = np.array(y_pred, dtype=float)
    
    residuals = y_true_float - y_pred_float
    
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred_float, residuals, alpha=0.5)
    plt.hlines(y=0, xmin=y_pred_float.min(), xmax=y_pred_float.max(), color='r', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title(title)
    plt.tight_layout()
    plt.show()
    
