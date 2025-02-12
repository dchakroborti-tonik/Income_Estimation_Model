
def plot_actual_vs_predicted(y_true, y_pred, title='Actual vs Predicted Values'):
    """
    Create a scatter plot of actual vs predicted values
    
    Parameters:
    - y_true: True target values
    - y_pred: Predicted target values
    - title: Plot title
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(title)
    plt.tight_layout()
    plt.show()
