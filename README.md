# TaxiFlow
---

In this project, I aimed to build a data engineering and machine learning workflow which processes and cleans data to be used as training data by an XGBoost regression model. MLFlow is used as well for model tracking and hyperparameter tuning. The final model would be deployed to an ECS cluster on AWS.

</br></br>
### High Level Architecture
---
<img width="1028" height="357" alt="Screenshot 2025-08-29 141721" src="https://github.com/user-attachments/assets/0278daab-f9dd-4506-9b6f-62bf8029baf3" />

</br>

This is done through a multi-cloud approach where Azure is used for preparing and storing the data using Azure Databricks along with Azure Data Lake Store. The data first passes through a medallion architecture implemented in ETL.ipynb, and the final gold layer data gets used as the training data for the XGBoost model, with all model runs being tracked with MLFLow. Finally, AWS is used for model deployment.

</br></br>
### Conclusion
---

This project served to offer experience working with the machine learning capabilities of Databricks through MLFlow and the pyspark.ml library.


