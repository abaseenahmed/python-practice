import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, roc_auc_score, confusion_matrix)
import matplotlib.pyplot as plt
import seaborn as sns

def validate_dataset(df):
    """Perform comprehensive dataset validation"""
    
    print("\n" + "="*50)
    print("📊 DATASET VALIDATION")
    print("="*50)
    
    # Basic info
    print(f"\n📋 Dataset shape: {df.shape}")
    print(f"\n📋 Columns: {df.columns.tolist()}")
    
    # Data types
    print("\n📋 Data types:")
    print(df.dtypes)
    
    # Missing values
    print("\n📋 Missing values:")
    print(df.isna().sum())
    
    # Duplicates
    duplicates = df.duplicated().sum()
    print(f"\n📋 Duplicate rows: {duplicates}")
    
    # Descriptive statistics
    print("\n📋 Descriptive statistics:")
    print(df.describe())
    
    # Target distribution
    if 'high_value_customer' in df.columns:
        target_dist = df['high_value_customer'].value_counts()
        print(f"\n📋 Target distribution:\n{target_dist}")
        print(f"   Percentage: {target_dist[1]/(target_dist[0]+target_dist[1])*100:.2f}%")
    
    return df

def perform_eda(df):
    """Perform exploratory data analysis"""
    
    print("\n" + "="*50)
    print("🔍 EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    # Correlation matrix for numerical features
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('../data/processed/correlation_matrix.png', dpi=150)
    plt.show()
    
    # Feature distributions
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    axes = axes.flatten()
    
    for i, col in enumerate(numeric_cols[:9]):
        df[col].hist(bins=30, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig('../data/processed/feature_distributions.png', dpi=150)
    plt.show()
    
    # Target analysis
    if 'high_value_customer' in df.columns:
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Target distribution
        df['high_value_customer'].value_counts().plot(kind='bar', ax=axes[0])
        axes[0].set_title('High Value Customer Distribution')
        axes[0].set_xlabel('High Value Customer')
        axes[0].set_ylabel('Count')
        
        # Compare features by target
        features_to_compare = ['total_spent', 'total_orders', 'average_order_value']
        df_melted = pd.melt(df, id_vars=['high_value_customer'], 
                           value_vars=features_to_compare)
        
        sns.boxplot(x='variable', y='value', hue='high_value_customer', 
                   data=df_melted, ax=axes[1])
        axes[1].set_title('Features by Customer Type')
        axes[1].set_xlabel('Feature')
        axes[1].set_ylabel('Value')
        
        plt.tight_layout()
        plt.savefig('../data/processed/target_analysis.png', dpi=150)
        plt.show()

def prepare_ml_data(df):
    """Prepare data for ML modeling"""
    
    print("\n" + "="*50)
    print("🤖 PREPARING ML DATA")
    print("="*50)
    
    # Handle missing values
    df = df.dropna()
    
    # Identify features and target
    X = df.drop(['customer_id', 'high_value_customer'], axis=1)
    y = df['high_value_customer']
    
    # Encode categorical variables
    categorical_cols = X.select_dtypes(include=['object']).columns
    label_encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        label_encoders[col] = le
    
    # Scale numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"✅ Training set: {X_train.shape}")
    print(f"✅ Test set: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test, X_scaled, y

def train_and_evaluate_models(X_train, X_test, y_train, y_test, X_scaled, y):
    """Train and evaluate ML models"""
    
    print("\n" + "="*50)
    print("🚀 MODEL TRAINING AND EVALUATION")
    print("="*50)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\n📊 Training {name}...")
        
        # Train
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
        
        # Evaluate
        results[name] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred),
            'roc_auc': roc_auc_score(y_test, y_prob),
            'confusion_matrix': confusion_matrix(y_test, y_pred)
        }
        
        print(f"   Accuracy: {results[name]['accuracy']:.4f}")
        print(f"   Precision: {results[name]['precision']:.4f}")
        print(f"   Recall: {results[name]['recall']:.4f}")
        print(f"   F1-Score: {results[name]['f1']:.4f}")
        print(f"   ROC-AUC: {results[name]['roc_auc']:.4f}")
    
    # Plot results
    plot_model_comparison(results)
    plot_confusion_matrices(results)
    
    # Feature importance (Random Forest)
    if 'Random Forest' in models:
        rf_model = models['Random Forest']
        importances = pd.DataFrame({
            'feature': X_train.columns,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\n📋 Top 10 Most Important Features:")
        print(importances.head(10))
        
        # Plot feature importance
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=importances.head(10))
        plt.title('Top 10 Feature Importances - Random Forest')
        plt.tight_layout()
        plt.savefig('../data/processed/feature_importance.png', dpi=150)
        plt.show()
    
    return results

def plot_model_comparison(results):
    """Plot model comparison"""
    metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(metrics))
    width = 0.35
    
    for i, (name, scores) in enumerate(results.items()):
        values = [scores[m] for m in metrics]
        ax.bar(x + i*width, values, width, label=name)
    
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Score')
    ax.set_title('Model Performance Comparison')
    ax.set_xticks(x + width/2)
    ax.set_xticklabels(metrics)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../data/processed/model_comparison.png', dpi=150)
    plt.show()

def plot_confusion_matrices(results):
    """Plot confusion matrices"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for i, (name, scores) in enumerate(results.items()):
        cm = scores['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i])
        axes[i].set_title(f'Confusion Matrix - {name}')
        axes[i].set_xlabel('Predicted')
        axes[i].set_ylabel('Actual')
    
    plt.tight_layout()
    plt.savefig('../data/processed/confusion_matrices.png', dpi=150)
    plt.show()

def main():
    """Main execution function"""
    print("🚀 Starting ML Pipeline...")
    
    # Load data
    df = pd.read_csv('../data/processed/ml_dataset.csv')
    
    # Validate
    df = validate_dataset(df)
    
    # EDA
    perform_eda(df)
    
    # Prepare ML data
    X_train, X_test, y_train, y_test, X_scaled, y = prepare_ml_data(df)
    
    # Train and evaluate models
    results = train_and_evaluate_models(
        X_train, X_test, y_train, y_test, X_scaled, y
    )
    
    # Summary
    print("\n" + "="*50)
    print("✅ PIPELINE COMPLETE!")
    print("="*50)
    print("\n📋 Results Summary:")
    for name, scores in results.items():
        print(f"\n{name}:")
        print(f"   Best Accuracy: {scores['accuracy']:.4f}")
        print(f"   Best F1-Score: {scores['f1']:.4f}")
    
    # Save results summary
    results_df = pd.DataFrame({
        'Model': results.keys(),
        'Accuracy': [scores['accuracy'] for scores in results.values()],
        'F1-Score': [scores['f1'] for scores in results.values()],
        'ROC-AUC': [scores['roc_auc'] for scores in results.values()]
    })
    results_df.to_csv('../data/processed/model_results.csv', index=False)
    print(f"\n✅ Results saved to data/processed/model_results.csv")

if __name__ == "__main__":
    main()